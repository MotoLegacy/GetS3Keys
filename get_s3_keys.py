#!/usr/bin/env python

# by plasticuproject
# MIT LICENSE

import argparse
import re
import os
import sys


url = ''
assets = []
lastKey = ''
running = True


def run():
    global assets, lastKey, running
    tags = []
    try:
        os.system('wget ' + url + '/?marker=' + lastKey + ' -O 1.html')
        with open('1.html', 'r') as infile:
            for line in infile:
                tags.append(line)
        infile.close()
        ends = (re.findall('(?:<Key>)([\r\s\S]*?)(?:<\/Key>)', tags[1]))
        if len(ends) < 1:
            running = False
        for i in ends:
            assets.append(i)
        lastKey = assets[-1]
    except:
        print('\nBad URL or connection. Or just broken. Whatever.\n')
        try:
            os.remove('1.html')
        except:
            pass
        sys.exit()



banner = ('''
    \nInput an S3 Bucket Domain. Since Bucket requests only return 1000 results at
    a time, this script will log the first 1000 Keys, then use the last Key as a
    marker to retrieve more Keys until all of the bucket Keys have been logged.
    It will then print out a file called S3_Keys.txt containing all of the Key
    URLs.\n''')


def main():
    global url
    parser = argparse.ArgumentParser(description=banner)
    parser.add_argument('domain', type=str, metavar='Domain',
                         help='S3 Bucket domain name (example: test.s3.amazonaws.com)')
    args = parser.parse_args()
    url = args.domain
    try:
        while running:
            run()
        with open('S3_Keys.txt', 'w') as outfile:
            for i in assets:
                outfile.write(url + '/' + i + '\n')
            outfile.close()
        os.remove('1.html')
    except KeyboardInterrupt:
        print('\nSo sorry, me so dum.\n')
        try:
            os.remove('1.html')
        except:
            pass
        sys.exit()
        

if __name__ == '__main__':
    main()
