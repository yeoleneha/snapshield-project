import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    reservations = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Backup',
                'Values': ['True']
            }
        ]
    )

    snapshot_ids = []

    for reservation in reservations['Reservations']:
        for instance in reservation['Instances']:

            for mapping in instance['BlockDeviceMappings']:

                volume_id = mapping['Ebs']['VolumeId']

                snapshot = ec2.create_snapshot(
                    VolumeId=volume_id,
                    Description=f"SnapShield Backup {datetime.utcnow()}",
                    TagSpecifications=[
                        {
                            'ResourceType':'snapshot',
                            'Tags':[
                                {'Key':'Project','Value':'SnapShield'}
                            ]
                        }
                    ]
                )

                snapshot_ids.append(snapshot['SnapshotId'])

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject='SnapShield Backup Success',
        Message=f'Snapshots Created: {snapshot_ids}'
    )

    return {
        'statusCode':200,
        'body':'Backup Completed'
    }