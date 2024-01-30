import boto3

vpc_id= input("Enter the VPC id you want to delete= ")
aws_management_console = boto3.session.Session(profile_name = "default" , region_name='us-east-1')

vpc_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")

# Delete a VPC
vpc = vpc_console.delete_vpc(
        VpcId=vpc_id
)
