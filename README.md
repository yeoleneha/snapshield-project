# 🚀 SnapShield – Automated EC2 Backup & Snapshot Management System

## 📖 Project Overview

SnapShield is an automated AWS backup solution designed to create and manage Amazon EBS snapshots for EC2 instances. The project leverages AWS Lambda, EventBridge Scheduler, SNS, CloudWatch, and IAM to automate backup operations and reduce manual intervention.

The solution automatically identifies EC2 instances marked for backup, creates EBS snapshots, sends email notifications upon successful execution, and removes outdated snapshots after a defined retention period to optimize storage costs.

This project demonstrates practical implementation of AWS automation, serverless computing, backup strategies, disaster recovery planning, monitoring, and cloud operations.

---

## 🎯 Objectives

* Automate EC2 backup operations
* Improve disaster recovery readiness
* Eliminate manual backup tasks
* Implement cost-optimized snapshot retention
* Monitor backup activities through CloudWatch
* Receive automated email notifications

---

## ☁️ AWS Services Used

| Service                      | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| Amazon EC2                   | Hosts application workloads             |
| Amazon EBS                   | Persistent block storage                |
| AWS Lambda                   | Automates backup and cleanup tasks      |
| Amazon EventBridge Scheduler | Triggers Lambda functions automatically |
| Amazon SNS                   | Sends email notifications               |
| Amazon CloudWatch            | Stores logs and monitoring data         |
| AWS IAM                      | Provides secure permissions             |

---

## 🏗️ Architecture

```text
                    EventBridge Scheduler
                              │
                              ▼
                    Backup Lambda Function
                              │
                              ▼
                     EC2 Instance (Tagged)
                              │
                              ▼
                         EBS Volume
                              │
                              ▼
                         EBS Snapshot
                              │
                              ▼
                     SNS Email Notification

                              ▲
                              │
                    Cleanup Lambda Function
                              │
                              ▼
              Delete Snapshots Older Than 7 Days

                              │
                              ▼
                     CloudWatch Monitoring
```

### Architecture Diagram

![Architecture](architecture.png)

---

## ✨ Key Features

### Automated Snapshot Creation

Creates EBS snapshots automatically for EC2 instances tagged for backup.

### Daily Scheduled Backups

EventBridge Scheduler triggers backup execution automatically every day.

### Email Notifications

Amazon SNS sends email alerts after successful backup execution.

### Snapshot Retention Management

Snapshots older than 7 days are deleted automatically.

### Monitoring and Logging

CloudWatch stores execution logs for monitoring and troubleshooting.

### Cost Optimization

Prevents unnecessary storage costs by cleaning up outdated snapshots.

### Disaster Recovery

Snapshots can be used to restore EBS volumes and recover critical data.

---

## 🔄 Project Workflow

### Step 1

EventBridge Scheduler triggers the Backup Lambda function.

### Step 2

Lambda identifies EC2 instances tagged with:

```text
Backup = True
```

### Step 3

Lambda retrieves attached EBS volumes.

### Step 4

Lambda creates EBS snapshots.

### Step 5

SNS sends email notifications with backup status.

### Step 6

CloudWatch stores execution logs.

### Step 7

Cleanup Lambda executes daily.

### Step 8

Snapshots older than 7 days are deleted automatically.

---

## ⚙️ Implementation Steps

### 1. Launch EC2 Instance

* Create an Amazon EC2 instance
* Attach EBS storage
* Configure Security Groups
* Assign required IAM permissions

### 2. Configure EC2 Tags

Add the following tag:

| Key    | Value |
| ------ | ----- |
| Backup | True  |

### 3. Create SNS Topic

* Create SNS Topic
* Subscribe email address
* Confirm email subscription

### 4. Create IAM Role

Permissions used:

* ec2:DescribeInstances
* ec2:DescribeVolumes
* ec2:CreateSnapshot
* ec2:DescribeSnapshots
* ec2:DeleteSnapshot
* sns:Publish
* logs:*

### 5. Create Backup Lambda

Function Name:

```text
SnapShieldBackup
```

Responsibilities:

* Discover tagged EC2 instances
* Create EBS snapshots
* Send SNS notifications

### 6. Create Cleanup Lambda

Function Name:

```text
SnapShieldCleanup
```

Responsibilities:

* Identify SnapShield snapshots
* Delete snapshots older than 7 days

### 7. Configure EventBridge Scheduler

Create two schedules:

#### DailyBackup

Triggers Backup Lambda

#### DailyCleanup

Triggers Cleanup Lambda

### 8. Verify CloudWatch Logs

Navigate to:

```text
Lambda → Monitor → View CloudWatch Logs
```

Verify successful execution logs.

---

## 📁 Repository Structure

```text
SnapShield-AWS-Backup-System/
│
├── lambda_backup.py
├── lambda_cleanup.py
├── README.md
├── architecture.png
├── 01-ec2-instance-running.png
├── 02-ec2-tags-backup-true.png
├── 03-iam-role-permissions.png
├── 04-sns-topic-created.png
├── 05-lambda-backup-function.png
├── 06-lambda-backup-test-success.png
├── 07-ebs-snapshot-created.png
├── 08-cloudwatch-logs.png
├── 09-eventbridge-backup-schedule.png
├── 10-lambda-cleanup-function.png
├── 11-eventbridge-cleanup-schedule.png
└── 12-email-notification.png
```

---

## 📸 Project Screenshots

The repository includes implementation screenshots covering:

* EC2 Instance Configuration
* EC2 Tags
* IAM Role Permissions
* SNS Topic Setup
* Backup Lambda Function
* Backup Execution Success
* EBS Snapshot Creation
* CloudWatch Logs
* EventBridge Schedules
* Cleanup Lambda Function
* Email Notifications

---

## 🛠️ Skills Demonstrated

* AWS EC2
* Amazon EBS
* AWS Lambda
* Amazon SNS
* EventBridge Scheduler
* CloudWatch Monitoring
* IAM Roles & Policies
* Python (Boto3)
* Automation
* Disaster Recovery
* Backup Strategy
* Serverless Architecture


