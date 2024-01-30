import boto3

aws_management_console = boto3.session.Session(profile_name = "default")

ec2_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")
result = ec2_console.describe_instances()['Reservations']
for each_instance in result:
        for value in each_instance['Instances']:
                instance_id = value['InstanceId']
                print(instance_id)
