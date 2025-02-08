#!/usr/bin/python
import argparse
#import re
import os
import logging
import boto3
from botocore.exceptions import ClientError
from datetime import date
from constants import S3_BUCKET, S3_KEY, S3_SECRET, REGION, S3_PATH

FILE_NAME ='vmfs_recovery.exe'

#args
parser = argparse.ArgumentParser(usage='%(prog)s logfile granularity method')
parser.add_argument('file_name', nargs='?', help='path to a file to upload', default=FILE_NAME)
parser.add_argument('s3_object_key', nargs='?', help='specify path in S3', default=S3_PATH)
args = parser.parse_args()
file_name = args.file_name
s3_object_key = '/temp/'                                                        #it's virtual folders in S3

def file_size(file_name):
    """Accepts full or relative file path""" #CHECK!
    return os.stat(file_name).st_size

def create_s3_object_key(file_name):
    """Creates a 'path' in S3 along with new filename"""
    today = date.today()
    return today.year+'/'+today+'/'+file_name                                   #Should output smth like: '/2025/2025.02.28/install.exe'

def upload_file(file_name, bucket, s3_object_key):
    """Upload a file to an S3 bucket
    :params:
        file_name: File to upload
        bucket: Bucket to upload to    
    :return: 
        True if file was uploaded, else False
    """
    object_name = s3_object_key+os.path.basename(file_name)
    s3 = boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET, region_name=REGION)
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    print ('Hello there')
    upload_file(file_name, S3_BUCKET, create_s3_object_key(file_name))          #it uses multipart upload automatically, split files to 8MB chunks


if __name__ == '__main__':
  main()