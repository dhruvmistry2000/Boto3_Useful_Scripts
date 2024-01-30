import boto3

subnet_id = input("Enter the Subnet-Id for deletion=")
aws_management_console = boto3.session.Session(profile_name = "default" , region_name='us-east-1')
subnet_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")

subnet = subnet_console.delete_subnet(
        SubnetId=subnet_id
        
)

