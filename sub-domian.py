import boto3

def get_customer_name(customer_id):
    return "customer_name_from_database"

def create_record_set(hosted_zone_id, sub_domain, instance_id):
    client = boto3.client('route53')
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)

    if not instance.public_ip_address:
        print("No public IP address available for this instance.")
        return

    tags = {tag['Key']: tag['Value'] for tag in instance.tags or []}
    instance_sub_domain = tags.get('SubDomain')

    if instance_sub_domain:
        change_batch = {
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': f"{instance_sub_domain}.{sub_domain}",
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': instance.public_ip_address}]
                    }
                }
            ]
        }

        try:
            response = client.change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch=change_batch
            )
            return response
        except Exception as e:
            print(f"Failed to update DNS record: {e}")
    else:
        print("SubDomain tag not found. Cannot create record set.")

if __name__ == "__main__":
    hosted_zone_id = "YOUR_HOSTED_ZONE_ID"
    sub_domain = "example.com"
    instance_id = "YOUR_INSTANCE_ID"
    customer_id = "CUSTOMER_ID"

    customer_name = get_customer_name(customer_id)

    subdomain = f"{customer_name}.{sub_domain}"

    response = create_record_set(hosted_zone_id, subdomain, instance_id)
    print(response)
    