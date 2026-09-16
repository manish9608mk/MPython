"""
======================================================================
AWS COMPLETE REVISION
======================================================================

Generic AWS revision for Cloud / DevOps / SRE / Software Engineering.

This is NOT project-specific.

Main rule:
    Understand the service first.
    Use CLI for inspection and troubleshooting.
    Use Terraform / IaC / CI-CD for repeatable infrastructure.

======================================================================
1. AWS FUNDAMENTALS
======================================================================

AWS
    → Cloud platform.

Region
    → Geographic AWS location.
    Example: ap-south-1

Availability Zone (AZ)
    → Isolated location inside a Region.

Account
    → Environment containing AWS resources.

Basic model:

AWS Account
    ↓
Region
    ↓
Availability Zones
    ↓
VPC
    ↓
Resources


CORE SERVICES
-------------

EC2       → Virtual machines
Lambda    → Serverless functions
ECS       → Container orchestration
Fargate   → Serverless container compute

S3        → Object storage
EBS       → Block storage

RDS       → Managed relational database

VPC       → Network
ALB       → Load balancing
Route 53  → DNS

IAM       → Identity and permissions
CloudWatch → Monitoring


======================================================================
2. AWS CLI
======================================================================

Basic structure:

aws <service> <operation>


Examples:

aws sts get-caller-identity
aws s3 ls
aws ec2 describe-instances


IDENTITY
--------

aws sts get-caller-identity


PROFILE
-------

aws sts get-caller-identity --profile PROFILE_NAME

aws configure set region REGION --profile PROFILE_NAME

aws configure get region --profile PROFILE_NAME


OUTPUT
------

--output json
--output table
--query '...'


Professional workflow:

Inspect
  ↓
Understand
  ↓
Change
  ↓
Verify


Remember:
    You do NOT need to memorize every CLI command.


======================================================================
3. IAM
======================================================================

IAM = Identity and Access Management.

Authentication
    → WHO are you?

Authorization
    → WHAT can you do?


COMPONENTS
----------

User
    → Individual identity

Group
    → Collection of users

Policy
    → Permission rules

Role
    → Temporary/workload identity


LEAST PRIVILEGE
---------------

Give only the permissions actually required.


Human access:

Human
  ↓
SSO / IAM Identity Center
  ↓
Temporary credentials


Application access:

Application
  ↓
IAM Role
  ↓
AWS Services


IMPORTANT COMMANDS
------------------

aws iam list-users

aws iam list-groups

aws iam list-roles

aws iam get-role --role-name ROLE_NAME

aws iam list-attached-user-policies \
    --user-name USER_NAME

aws iam list-attached-role-policies \
    --role-name ROLE_NAME

aws iam list-role-policies \
    --role-name ROLE_NAME


Security:

❌ Never hard-code AWS credentials
❌ Never commit credentials to Git
❌ Avoid unnecessary AdministratorAccess

✅ Use IAM roles
✅ Use least privilege
✅ Use MFA / federated access for humans


======================================================================
4. S3
======================================================================

S3 = Object Storage.

Bucket
  ↓
Objects

Example:

bucket/
    images/photo.jpg
    models/model.pkl
    logs/app.log


S3 features:

    Encryption
    Versioning
    Lifecycle rules
    Access control
    Block Public Access


IMPORTANT COMMANDS
------------------

List buckets:

aws s3 ls

List objects:

aws s3 ls s3://BUCKET_NAME

Create bucket:

aws s3 mb s3://BUCKET_NAME --region REGION

Upload:

aws s3 cp FILE s3://BUCKET_NAME/

Download:

aws s3 cp s3://BUCKET_NAME/FILE .

Delete object:

aws s3 rm s3://BUCKET_NAME/FILE


S3 API checks:

aws s3api get-bucket-location \
    --bucket BUCKET_NAME

aws s3api get-bucket-versioning \
    --bucket BUCKET_NAME

aws s3api get-bucket-encryption \
    --bucket BUCKET_NAME

aws s3api list-buckets


Security:

Prefer private buckets.
Use IAM / roles for application access.


======================================================================
5. VPC
======================================================================

VPC = Virtual Private Cloud.

It is your logical network inside AWS.

VPC
├── Public Subnet
└── Private Subnet


CIDR
----

Defines the network range.

Example:

10.0.0.0/16


SUBNET
-------

Smaller network inside a VPC.


PUBLIC SUBNET
-------------

Subnet
  ↓
Route Table
  ↓
Internet Gateway
  ↓
Internet


PRIVATE SUBNET
--------------

Subnet
  ↓
Private Route Table
  ↓
No direct Internet Gateway route


ROUTE TABLE
-----------

Controls where traffic goes.

Example:

10.0.0.0/16 → local
0.0.0.0/0    → Internet Gateway


INTERNET GATEWAY
----------------

Connects a VPC to the Internet.


NAT GATEWAY
-----------

Allows private resources to make outbound
Internet connections.

Private Subnet
    ↓
NAT Gateway
    ↓
Internet Gateway
    ↓
Internet


IMPORTANT:
    NAT Gateway is generally billable.


SECURITY GROUP
--------------

Virtual firewall for AWS resources.

Common ports:

22    → SSH
80    → HTTP
443   → HTTPS
5432  → PostgreSQL


IMPORTANT COMMANDS
------------------

aws ec2 describe-vpcs

aws ec2 describe-subnets

aws ec2 describe-route-tables

aws ec2 describe-internet-gateways

aws ec2 describe-nat-gateways

aws ec2 describe-security-groups

aws ec2 describe-vpcs --vpc-ids VPC_ID

aws ec2 describe-subnets --subnet-ids SUBNET_ID


Important:
    Public/private subnet status mainly depends on routing.


======================================================================
6. EC2
======================================================================

EC2 = Virtual Machine / Server.

EC2 components:

AMI
    → Machine image

Instance Type
    → CPU + RAM + network capacity

EBS
    → Block storage

Security Group
    → Firewall

IAM Role
    → AWS permissions

VPC/Subnet
    → Network location


IMPORTANT COMMANDS
------------------

aws ec2 describe-instances

Running instances:

aws ec2 describe-instances \
    --filters Name=instance-state-name,Values=running

Specific instance:

aws ec2 describe-instances \
    --instance-ids INSTANCE_ID

Volumes:

aws ec2 describe-volumes

Launch templates:

aws ec2 describe-launch-templates


STATE COMMANDS

Start:

aws ec2 start-instances \
    --instance-ids INSTANCE_ID

Stop:

aws ec2 stop-instances \
    --instance-ids INSTANCE_ID

Terminate:

aws ec2 terminate-instances \
    --instance-ids INSTANCE_ID


WARNING:
    EC2 is generally billable.
    Termination can permanently remove resources/data.


======================================================================
7. EBS
======================================================================

EBS = Block storage for EC2.

EC2
 ↓
EBS Volume
 ↓
Filesystem
 ↓
Application


Snapshot
    → Point-in-time backup of an EBS volume.


IMPORTANT COMMANDS
------------------

aws ec2 describe-volumes

aws ec2 describe-snapshots \
    --owner-ids self

aws ec2 describe-volumes \
    --volume-ids VOLUME_ID


Cost:
    EBS volumes and snapshots can incur charges.


======================================================================
8. RDS
======================================================================

RDS = Managed relational database.

Common engines:

    PostgreSQL
    MySQL
    MariaDB
    Oracle
    SQL Server


RDS
 ↓
Database Engine
 ↓
Database


RDS commonly runs inside a VPC.

Private Subnet A
        +
Private Subnet B
        ↓
DB Subnet Group
        ↓
RDS


Security pattern:

Application SG
      ↓
    5432
      ↓
RDS SG


Avoid:

0.0.0.0/0 → 5432


IMPORTANT COMMANDS
------------------

aws rds describe-db-instances

aws rds describe-db-instances \
    --db-instance-identifier DB_IDENTIFIER

aws rds describe-db-subnet-groups

aws rds describe-db-snapshots


Cost:
    RDS is generally billable.


======================================================================
9. ELB / LOAD BALANCING
======================================================================

Load Balancer distributes traffic.

Users
  ↓
ALB
  ↓
Target Group
  ↓
EC2 / ECS


ALB
    → HTTP / HTTPS
    → Layer 7

NLB
    → TCP / UDP / TLS
    → Layer 4


Target Group
    → Backend targets

Health Check
    → Checks target health


IMPORTANT COMMANDS
------------------

aws elbv2 describe-load-balancers

aws elbv2 describe-target-groups

aws elbv2 describe-target-health \
    --target-group-arn TARGET_GROUP_ARN


======================================================================
10. AUTO SCALING
======================================================================

Auto Scaling Group (ASG)
    → Manages EC2 capacity.

Important values:

Minimum
Desired
Maximum


Example:

Min = 2
Desired = 2
Max = 5


Scale Out
    → Add instances

Scale In
    → Remove instances


Launch Template
    → Blueprint for new EC2 instances.


IMPORTANT COMMANDS
------------------

aws autoscaling describe-auto-scaling-groups

aws ec2 describe-launch-templates


Cost:
    More EC2 instances = more compute cost.


======================================================================
11. LAMBDA
======================================================================

Lambda = Serverless compute.

Event
  ↓
Lambda
  ↓
Code
  ↓
Result


Common uses:

    APIs
    Background processing
    Event-driven tasks
    Scheduled jobs
    File processing


Lambda
  ↓
Execution Role
  ↓
AWS Services


IMPORTANT COMMANDS
------------------

aws lambda list-functions

aws lambda get-function \
    --function-name FUNCTION_NAME

aws lambda get-function-configuration \
    --function-name FUNCTION_NAME


======================================================================
12. API GATEWAY
======================================================================

API Gateway = Managed API entry point.

Client
  ↓
API Gateway
  ↓
Lambda / ECS / EC2
  ↓
Response


Common concepts:

    Routes
    Integrations
    Authorization
    Throttling


IMPORTANT COMMANDS
------------------

REST APIs:

aws apigateway get-rest-apis

aws apigateway get-rest-api \
    --rest-api-id API_ID


HTTP/WebSocket APIs:

aws apigatewayv2 get-apis


======================================================================
13. ECS
======================================================================

ECS = Container orchestration service.

Docker Image
    ↓
ECS
    ↓
Task
    ↓
Container


CORE COMPONENTS
---------------

Cluster
    → Logical grouping

Task Definition
    → Container blueprint

Task
    → Running workload

Service
    → Maintains desired number of tasks


LAUNCH OPTIONS
--------------

EC2
    → You manage EC2 infrastructure

Fargate
    → AWS manages underlying servers


Typical:

ALB
 ↓
ECS Service
 ↓
Fargate Tasks
 ↓
Containers


IMPORTANT COMMANDS
------------------

aws ecs list-clusters

aws ecs list-services \
    --cluster CLUSTER_NAME

aws ecs list-tasks \
    --cluster CLUSTER_NAME

aws ecs describe-tasks \
    --cluster CLUSTER_NAME \
    --tasks TASK_ID

aws ecs describe-services \
    --cluster CLUSTER_NAME \
    --services SERVICE_NAME


Cost:
    Fargate / EC2 compute can be billable.


======================================================================
14. ECR
======================================================================

ECR = Container Image Registry.

Dockerfile
    ↓
Docker Build
    ↓
Docker Image
    ↓
ECR
    ↓
ECS / Fargate


Repository
    → Stores container images

Tag
    → Identifies image version


IMPORTANT COMMANDS
------------------

aws ecr describe-repositories

aws ecr list-images \
    --repository-name REPOSITORY_NAME

aws ecr describe-repositories \
    --repository-names REPOSITORY_NAME


Docker authentication:

aws ecr get-login-password \
    --region REGION | \
docker login \
    --username AWS \
    --password-stdin ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com


Tag:

docker tag IMAGE:TAG \
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/REPOSITORY:TAG


Push:

docker push \
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/REPOSITORY:TAG


Cost:
    Storage and data transfer can incur charges.


======================================================================
15. CLOUDWATCH
======================================================================

CloudWatch = Monitoring and observability.

CloudWatch
    ├── Metrics
    ├── Logs
    ├── Alarms
    └── Dashboards


Metrics
    → Numerical measurements

Logs
    → Records/events

Alarms
    → Conditions that trigger actions/notifications

Dashboard
    → Visual monitoring


IMPORTANT COMMANDS
------------------

aws cloudwatch describe-alarms

aws cloudwatch list-metrics

aws logs describe-log-groups

Metric statistics:

aws cloudwatch get-metric-statistics \
    --namespace AWS/EC2 \
    --metric-name CPUUtilization \
    --statistics Average \
    --period 300 \
    --start-time START_TIME \
    --end-time END_TIME


Cost:
    High-volume logs and custom metrics can incur charges.


======================================================================
16. ROUTE 53
======================================================================

Route 53 = DNS service.

Domain
  ↓
Route 53
  ↓
IP / Load Balancer
  ↓
Application


IMPORTANT COMMANDS
------------------

aws route53 list-hosted-zones

aws route53 list-resource-record-sets \
    --hosted-zone-id HOSTED_ZONE_ID


======================================================================
17. COMMON REAL-WORLD ARCHITECTURE
======================================================================

                         Internet
                            |
                         Route 53
                            |
                           ALB
                            |
                  +---------+---------+
                  |                   |
                 ECS                 ECS
              Service A           Service B
                  |                   |
                Tasks               Tasks
                  |
          +-------+-------+
          |               |
         S3              RDS
       Storage        PostgreSQL


Supporting services:

IAM
    → Permissions

ECR
    → Container images

CloudWatch
    → Monitoring

VPC
    → Networking

Security Groups
    → Network security


======================================================================
18. SECURITY GROUP PATTERN
======================================================================

Internet
    ↓
ALB SG
    ↓
Application SG
    ↓
RDS SG


Example:

Internet → ALB : 443

ALB SG → Application SG : App Port

Application SG → RDS SG : 5432


This is better than:

Internet → Database


======================================================================
19. READ vs WRITE COMMANDS
======================================================================

READ / INSPECT
--------------

Usually:

describe-*
list-*
get-*


Examples:

aws ec2 describe-instances
aws iam list-roles
aws ecs list-clusters


WRITE / CHANGE
--------------

Examples:

create-*
put-*
update-*
modify-*
start-*
stop-*
delete-*
terminate-*


Rule:

    Inspect first.
    Change second.
    Verify afterward.


======================================================================
20. TERRAFORM / INFRASTRUCTURE AS CODE
======================================================================

Manual approach:

Engineer
   ↓
Console / CLI
   ↓
AWS Resources


Infrastructure as Code:

Terraform
   ↓
Plan
   ↓
Review
   ↓
Apply
   ↓
AWS


Benefits:

    Repeatability
    Version control
    Code review
    Automation
    Consistency


CLI remains useful for:

    Inspection
    Debugging
    Troubleshooting
    Verification


======================================================================
21. COST SAFETY
======================================================================

Before creating a resource:

1. Is it billable?
2. Do I need it?
3. What will it cost?
4. How will I remove it?
5. Is there a cheaper alternative?


Common potentially billable resources:

    EC2
    EBS
    RDS
    NAT Gateway
    Load Balancer
    Fargate
    ECR usage
    CloudWatch usage
    Data transfer
    Route 53 usage


Learning rule:

    Prefer read-only commands first.


======================================================================
22. MOST IMPORTANT COMMANDS TO REMEMBER
======================================================================

IDENTITY
--------

aws sts get-caller-identity


S3
--

aws s3 ls

aws s3 ls s3://BUCKET_NAME

aws s3 cp FILE s3://BUCKET_NAME/


EC2
---

aws ec2 describe-instances

aws ec2 describe-volumes

aws ec2 describe-security-groups


VPC
---

aws ec2 describe-vpcs

aws ec2 describe-subnets

aws ec2 describe-route-tables


IAM
---

aws iam list-users

aws iam list-roles

aws iam list-groups


RDS
---

aws rds describe-db-instances


ECS
---

aws ecs list-clusters

aws ecs list-services --cluster CLUSTER_NAME

aws ecs list-tasks --cluster CLUSTER_NAME


ECR
---

aws ecr describe-repositories

aws ecr list-images \
    --repository-name REPOSITORY_NAME


Lambda
------

aws lambda list-functions


CloudWatch
----------

aws cloudwatch describe-alarms

aws cloudwatch list-metrics


Route 53
--------

aws route53 list-hosted-zones


======================================================================
23. COMMAND PATTERN TO REMEMBER
======================================================================

Instead of memorizing hundreds of commands:

aws <service> <operation>


Then add:

--profile PROFILE
--region REGION
--query '...'
--output table
--output json


Example:

aws ec2 describe-instances \
    --profile PROFILE \
    --region REGION \
    --output table


Professional skill:

    Know what you need.
    Know which AWS service provides it.
    Know how to inspect it.
    Look up the exact command when necessary.


======================================================================
24. FINAL AWS MEMORY MAP
======================================================================

IAM
 ↓
Who can access?

VPC
 ↓
Where does it live?

Security Group
 ↓
Who can communicate?

EC2 / ECS / Lambda
 ↓
Where does code run?

ECR
 ↓
Where are container images stored?

S3
 ↓
Where are objects/files stored?

RDS
 ↓
Where is relational data stored?

ALB
 ↓
How does traffic reach the application?

Auto Scaling
 ↓
How does capacity change?

CloudWatch
 ↓
How do we monitor it?

Route 53
 ↓
How does the domain resolve?

Terraform
 ↓
How do we manage infrastructure as code?


======================================================================
ONE-LINE CHEAT SHEET
======================================================================

IAM        = Identity + Permissions
VPC        = Network
Subnet     = Smaller network
Route Table= Traffic direction
IGW        = Internet connection
NAT        = Private outbound Internet
SG         = Firewall
EC2        = Virtual Machine
EBS        = Block Storage
S3         = Object Storage
RDS        = Managed Relational Database
ALB        = Application Load Balancer
ASG        = EC2 Auto Scaling
Lambda     = Serverless Compute
ECS        = Container Orchestration
Fargate    = Serverless Container Compute
ECR        = Container Image Registry
CloudWatch = Monitoring
Route 53   = DNS
IAM Role   = Workload Identity
Terraform  = Infrastructure as Code


======================================================================
FINAL RULE
======================================================================

Do not try to memorize every AWS command.

Learn:

    Service
       ↓
    Purpose
       ↓
    Common operations
       ↓
    CLI pattern
       ↓
    Documentation when needed


Real-world engineers use documentation, CLI help,
Terraform, automation, and CI/CD.

Knowing how to find and verify the correct command
is part of being a good cloud engineer.

"""
