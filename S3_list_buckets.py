import boto3

aws_management_console = boto3.session.Session(profile_name='default')
# Create an S3 client
s3 = aws_management_console.client(service_name='s3', region_name='us-east-1')

response = s3.list_buckets()

print("List of S3 buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']} (created at {bucket['CreationDate']})")
