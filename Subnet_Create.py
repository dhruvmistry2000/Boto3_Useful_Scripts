import boto3

name  = input("Enter the name you want for your subnet = ")
cidr_block = input("Enter the CIDR Block = ")

aws_management_console = boto3.session.Session(profile_name = "default" , region_name='us-east-1')

subnet_console = aws_management_console.client(service_name = "ec2", region_name="us-east-1")

subnet = subnet_console.create_subnet(
        VpcId = 'VPC_ID',
        CidrBlock=cidr_block,
        AvailabilityZone='us-east-1a',
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{'Key': 'Name','Value': f'{name}-1'}]
            },
        ]
)

subnet_id = subnet['Subnet']['SubnetId']
print("The subnet id is ", subnet_id)
