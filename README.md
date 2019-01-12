# GetS3Keys

Since AWS S3 Bucket requests only return 1000 results at a time, this script <br />
will log the first 1000 Keys, then use the last Key as a marker to retrieve <br />
more Keys until all of the bucket Keys have been logged. It will then print <br />
out a file called S3_Keys.txt containing all of the Key URLs. <br />


## Requirements

Linux OS <br />
Python 3.6+ <br />
wget <br />


## Usage
```
usage: get_s3_keys.py [-h] Domain

positional arguments:
  Domain      S3 Bucket domain name (example: test.s3.amazonaws.com)

optional arguments:
  -h, --help  show this help message and exit
```
