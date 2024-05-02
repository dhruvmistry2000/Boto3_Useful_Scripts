import boto3
import datetime

def get_recent_instances():
    ec2 = boto3.client('ec2', region_name='your-region')

    # Get current time and calculate 5 minutes ago
    current_time = datetime.datetime.now()
    five_minutes_ago = current_time - datetime.timedelta(seconds=60)

    # Get instances launched in the last 5 minutes
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'launch-time',
                'Values': [five_minutes_ago.strftime('%Y-%m-%dT%H:%M:%S')]
            }
        ]
    )

    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)

    return instances

def get_instance_ips(instances):
    ips = []

    for instance in instances:
        for iface in instance['NetworkInterfaces']:
            ips.append(iface['PrivateIpAddress'])

    return ips

if __name__ == "__main__":
    recent_instances = get_recent_instances()
    instance_ips = get_instance_ips(recent_instances)

    print("IP addresses of instances launched in the last 5 minutes:")
    for ip in instance_ips:
        print(ip)
