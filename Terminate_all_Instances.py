# This script Terminates the running instances 

import boto3

aws_management_console = boto3.session.Session(profile_name = "default")

ec2_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")
running_instance = ec2_console.describe_instances()['Reservations']
for each_instance in running_instance:
        for value in each_instance['Instances']:
                Instance_id = value['InstanceId']
                # print(Instance_id)
                print("Terminating Instance with id " , Instance_id)
                response = ec2_console.terminate_instances(InstanceIds = [Instance_id])
                


