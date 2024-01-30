import boto3
import os
bucket_name = input("Enter your bucket: ")
aws_management_console = boto3.session.Session(profile_name='default')

s3_console = aws_management_console.client(service_name='s3', region_name='us-east-1')

path1 =  os.getcwd()
file = 'S3.py'
filename = os.path.join(path1, file)

data = open(filename ,'rb')

s3_console.upload_file(filename, bucket_name, file)