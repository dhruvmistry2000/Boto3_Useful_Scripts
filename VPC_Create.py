import boto3

aws_management_console = boto3.session.Session(profile_name = "default" , region_name='us-east-1')

vpc_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")
# Create a VPC
vpc = vpc_console.create_vpc(
        CidrBlock='10.0.0.0/20',
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [{'Key': 'Name','Value': 'Dhruv_VPC'}]
            },
        ]
)
