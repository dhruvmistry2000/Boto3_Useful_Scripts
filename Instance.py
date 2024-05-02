import boto3

aws_management_console = boto3.session.Session(profile_name="default")

ec2_console = aws_management_console.client(service_name='ec2', region_name='us-east-1')

print("Starting Instance ")
response = ec2_console.run_instances(
        ImageId = 'ami-080e1f13689e07408',
        InstanceType = 't2.micro',
        MaxCount=1,
        MinCount=1,
        KeyName="learning",
        SecurityGroupIds=['sg-0282e78957faaf9e0']
        )

# Extract instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Launched instance {instance_id}')

ec2_console.get_waiter('instance_running').wait(InstanceIds=[instance_id])

response = ec2_console.describe_instances(InstanceIds=[instance_id])

public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']

print(f'Public IP address of instance {instance_id}: {public_ip}')