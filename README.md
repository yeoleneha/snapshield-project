# SnapShield - Automated EC2 Backup System------------

## Project Overview

SnapShield is an AWS-based automated backup solution that creates EBS snapshots of EC2 instances using AWS Lambda and EventBridge Scheduler.

The project automates backup creation, sends email notifications through Amazon SNS, stores execution logs in CloudWatch, and automatically deletes old snapshots to optimize storage costs.

---

## AWS Services Used

* Amazon EC2
* Amazon EBS
* AWS Lambda
* Amazon EventBridge Scheduler
* Amazon SNS
* Amazon CloudWatch
* AWS IAM

---

## Architecture

EC2 Instance
↓
EBS Volume
↓
Lambda Backup Function
↓
EBS Snapshot
↓
SNS Email Notification

EventBridge Scheduler
↓
Triggers Lambda Daily

Cleanup Lambda
↓
Deletes Snapshots Older Than 7 Days

CloudWatch
↓
Monitoring and Logs

---

## Features

* Automated EBS Snapshot Creation
* Daily Scheduled Backups
* SNS Email Notifications
* CloudWatch Monitoring
* Automatic Snapshot Cleanup
* Cost Optimization
* Disaster Recovery Support

---

## Project Flow

1. EventBridge Scheduler triggers the Backup Lambda function.
2. Lambda identifies EC2 instances tagged with Backup=True.
3. Lambda creates EBS snapshots of attached volumes.
4. SNS sends email notification after successful backup.
5. CloudWatch stores execution logs.
6. Cleanup Lambda runs daily.
7. Snapshots older than 7 days are deleted automatically.

---

## Project Structure

SnapShield-AWS-Backup-System/

├── lambda_backup.py

├── lambda_cleanup.py

├── README.md

├── architecture.png

└── screenshots/


