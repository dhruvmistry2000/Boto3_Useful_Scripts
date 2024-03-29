import boto3

No_Instance = int(input("Enter number of instances you want to Deploy = "))

name  = input("Enter the name you want for your EC2 instance = ")
aws_management_console = boto3.session.Session(profile_name="default")

ec2_console = aws_management_console.client(service_name='ec2', region_name='us-east-1')

for i in range(No_Instance):
        print("Starting Instance " , i+1)
        response = ec2_console.run_instances(
                ImageId = 'AMI_ID',
                InstanceType = 't2.micro',
                MaxCount=1,
                MinCount=1,
                KeyName="Key_Name",
                SecurityGroupIds=['Security_Group_ID'],
                TagSpecifications=[
                                {
                                    'ResourceType': 'instance',
                                    'Tags': [{'Key': 'Name','Value': f'{name}-{i+1}'}]
                                },
                            ]
    )
        
        
