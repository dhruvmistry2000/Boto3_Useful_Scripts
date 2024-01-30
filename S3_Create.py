import boto3

aws_management_console = boto3.session.Session(profile_name='default')

s3_console = aws_management_console.client(service_name='s3', region_name='us-east-1')

bucket_create = s3_console.create_bucket(
        Bucket='dhruv-boto3-bucket-no1',
)
print(bucket_create)