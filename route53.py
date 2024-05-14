import boto3

def lambda_handler(event, context):
    # Extract instance details from the event
    instance_id = event['detail']['instance-id']
    
    # Connect to EC2 and Route 53 clients
    ec2_client = boto3.client('ec2')
    route53_client = boto3.client('route53')
    
    # Describe the instance to get its tags
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    tags = response['Reservations'][0]['Instances'][0].get('Tags', [])
    
    # Find the subdomain tag
    subdomain = None
    for tag in tags:
        if tag['Key'] == 'Subdomain':
            subdomain = tag['Value']
            break
    
    # If subdomain tag is found, update Route 53 record
    if subdomain:
        instance_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        # Assuming hosted zone ID and domain name are known
        hosted_zone_id = 'YOUR_HOSTED_ZONE_ID'
        domain_name = 'example.com'
        # Update Route 53 record
        route53_client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': f'{subdomain}.{domain_name}',
                            'Type': 'A',
                            'TTL': 300,
                            'ResourceRecords': [{'Value': instance_ip}]
                        }
                    }
                ]
            }
        )
    
    return {
        'statusCode': 200,
        'body': 'Subdomain allocation completed.'
    }
