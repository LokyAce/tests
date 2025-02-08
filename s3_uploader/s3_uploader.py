#!/usr/bin/python
import argparse
import os
import logging
import json
import datetime
import boto3

from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from datetime import date
from constants import S3_BUCKET, S3_KEY, S3_SECRET, REGION, S3_PATH, FILE_NAME

json_file_name = 'file_list.json'

#args
parser = argparse.ArgumentParser(usage='%(prog)s logfile granularity method')
parser.add_argument('file_name', nargs='?', help='path to a file to upload', default=FILE_NAME)
parser.add_argument('s3_object_key', nargs='?', help='specify path in S3', default=S3_PATH)
args = parser.parse_args()
file_name = args.file_name

config = TransferConfig(
    use_threads=True,  # Enable multithreading
    max_concurrency=4  # Set the maximum number of threads
)



def file_size(file_name):
    """Accepts full or relative file path""" #CHECK!
    return os.stat(file_name).st_size

def create_s3_object_key(file_name):
    """Creates a 'path' in S3 along with new filename"""
    today = date.today()
    f = os.path.basename(file_name)                                                                      #Striping path
    return str(today.year)+'/'+str(today.year)+'.'+str(today.month)+'.'+str(today.day)+'/'+f             #Should output smth like: '/2025/2025.02.28/install.exe'

def upload_file(file_name, bucket, s3_object_key):
    """Uploads a file to an S3 bucket
    :params:
        file_name: File to upload
        bucket: Bucket to upload to    
    :return: 
        True if file was uploaded, else False
    """    
    s3 = boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET, region_name=REGION)
    try:
        response = s3.upload_file(file_name, bucket, s3_object_key, Config=config)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_entire_bucket(bucket):
    """Gets all files from the bucket. Returns JSON-compatible string, which needs to be convertated to the obj"""
    # Create a client
    client = boto3.client('s3', region_name=REGION)

    # Create a reusable Paginator
    paginator = client.get_paginator('list_objects_v2')

    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket=bucket)

    json_elements = []    #Stores dict, will be converted to JSON

    for page in page_iterator:
        for element in page['Contents']:
            if isinstance(element['LastModified'], datetime.datetime):
                    element['LastModified'] = element['LastModified'].isoformat()
            json_elements.append(element)
    return json_elements


def main():
    print ('\n Hello there')
    start_time = datetime.datetime.now(datetime.UTC)
    if upload_file(file_name, S3_BUCKET, create_s3_object_key(file_name)):    #It uses multipart upload automatically, files are split to 8MB chunks, multithread enabled
        print ('\n ', file_name, ' - upload complete in ', str(datetime.datetime.now(datetime.UTC)-start_time), ' sec \n')
    else:
        print (file_name, ' -- upload failed \n')    
    
    json_data = get_entire_bucket(S3_BUCKET)

    with open (json_file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
  main()