import boto3

bucket_name = input("Enter the S3 Bucket name = ")

aws_management_console = boto3.session.Session(profile_name='default')
s3_console = aws_management_console.client(service_name='s3', region_name='us-east-1')

bucket_create = s3_console.delete_bucket(
        Bucket=bucket_name
)
print(bucket_create)