import boto3


name  = input("Enter the name you want for your subnets = ")
vpc_id = input("Enter the VPC ID you want subnets to be created= ")

aws_management_console = boto3.session.Session(profile_name="default", region_name='us-east-1')
subnet_console = aws_management_console.client(service_name="ec2", region_name="us-east-1")

# List of CIDR blocks for your subnets
subnet_cidr_blocks = ['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']

for index, cidr_block in enumerate(subnet_cidr_blocks, start=1):
    subnet = subnet_console.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr_block,
        AvailabilityZone=f'us-east-1a',  # Set the appropriate availability zone
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{'Key': 'Name', 'Value': f'{name}-{index}'}]
            },
        ]
    )

    subnet_id = subnet['Subnet']['SubnetId']
    print(f"Subnet-{index} created with ID: {subnet_id}")
