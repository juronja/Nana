import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

# EC2 Instance status check
instances = ec2_client.describe_instance_status()["InstanceStatuses"]

for instance in instances:
    instance_state = instance["InstanceState"]["Name"]
    instance_status = instance["InstanceStatus"]["Status"]
    system_status = instance["SystemStatus"]["Status"]
    print(f"Instance State, Status and system status of {instance["InstanceId"]} are: {instance_state}, {instance_status}, {system_status}")