import boto3

aws_management_console = boto3.session.Session(profile_name="default", region_name='us-east-1')

subnet_console = aws_management_console.client(service_name="ec2", region_name="us-east-1")

subnet_id = ['subnet-02d561ae1f09644fe', 'subnet-04f919083eab819df']

for index, subnetid in enumerate(subnet_id, start=1):
    subnet = subnet_console.delete_subnet(
        SubnetId=subnetid
    )
    print(f"Subnet with id {subnetid} is Deleted")

    
