import boto3

aws_management_console = boto3.session.Session(profile_name="default")

ec2_console = aws_management_console.client(service_name='ec2', region_name='us-east-1')

response = ec2_console.terminate_instances(
        InstanceIds = ['i-0b58bef01cf422ee4']
)