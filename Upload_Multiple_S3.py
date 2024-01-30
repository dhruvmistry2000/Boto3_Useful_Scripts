import boto3
import os

bucket_name = input("Enter your bucket: ")
aws_management_console = boto3.session.Session(profile_name='default')

s3_console = aws_management_console.client(service_name='s3', region_name='us-east-1')

path1 = os.getcwd()
# files = os.listdir(path1)
extension = '.py'
files = [file for file in os.listdir(path1) if file.endswith(extension)]

for file in files:
    try:
        print(f"Uploading {file}...")
        s3_console.upload_file(os.path.join(path1, file), bucket_name, file)
        print(f"Upload successful: {file}")
    except Exception as e:
        print(f"Error uploading {file}: {e}")

print("Upload completed.")
