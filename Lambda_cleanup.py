import boto3
from datetime import datetime, timezone

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    snapshots = ec2.describe_snapshots(
        OwnerIds=['self']
    )

    for snapshot in snapshots['Snapshots']:

        tags = snapshot.get('Tags', [])

        is_project_snapshot = any(
            tag['Key'] == 'Project'
            and tag['Value'] == 'SnapShield'
            for tag in tags
        )

        if not is_project_snapshot:
            continue

        age = (
            datetime.now(timezone.utc)
            - snapshot['StartTime']
        ).days

        if age > 7:

            ec2.delete_snapshot(
                SnapshotId=snapshot['SnapshotId']
            )

            print(
                f"Deleted: {snapshot['SnapshotId']}"
            )

    return "Cleanup Completed"