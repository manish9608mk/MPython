'''
============================================================
AWS EC2 — Elastic Compute Cloud
============================================================

EC2 = Virtual Server in AWS

Think:

Physical Server
      ↓
AWS Data Center
      ↓
EC2 Instance
      ↓
Your Application


EC2 INSTANCE
------------

An EC2 instance is a virtual machine.

You choose:

    AMI
    ↓
    OS / Server Image

    Instance Type
    ↓
    CPU + RAM

    Storage
    ↓
    EBS

    Network
    ↓
    VPC + Subnet

    Security
    ↓
    Security Group


BASIC ARCHITECTURE
------------------

Internet
   ↓
Load Balancer
   ↓
Security Group
   ↓
EC2
   ↓
Application


IMPORTANT CONCEPTS
------------------

AMI
→ Machine image used to launch an instance

Instance Type
→ CPU, memory, network capacity, etc.

EBS
→ Persistent block storage for EC2

Security Group
→ Virtual firewall

Key Pair
→ Used for SSH authentication

Elastic IP
→ Static public IPv4 address


INSTANCE STATES
---------------

Running
   ↓
Stopped
   ↓
Terminated

Stopped:
→ Instance is not running
→ Some attached resources can still incur charges

Terminated:
→ Instance is permanently deleted


IMPORTANT COMMANDS
------------------

List EC2 instances:

aws ec2 describe-instances


List only running instances:

aws ec2 describe-instances \
    --filters Name=instance-state-name,Values=running


Check a specific instance:

aws ec2 describe-instances \
    --instance-ids INSTANCE_ID


List AMIs:

aws ec2 describe-images


List security groups:

aws ec2 describe-security-groups


START / STOP / TERMINATE
------------------------

These change infrastructure and may have
billing or data consequences.

Start:

aws ec2 start-instances \
    --instance-ids INSTANCE_ID

Stop:

aws ec2 stop-instances \
    --instance-ids INSTANCE_ID

Terminate:

aws ec2 terminate-instances \
    --instance-ids INSTANCE_ID


COST SAFETY
-----------

EC2 is generally BILLABLE.

For learning:

❌ Don't launch instances unnecessarily
❌ Don't leave paid resources running
❌ Don't terminate something without checking it

First learn:

    Architecture
        ↓
    Commands
        ↓
    Cost
        ↓
    Then create resources when actually needed


EC2 vs CONTAINER
----------------

EC2
→ Virtual machine

Docker Container
→ Application container

ECS
→ AWS service for running containers


REMEMBER
--------

EC2 = Virtual Server

AMI       → Image
Type      → CPU/RAM
EBS       → Storage
SG        → Firewall
VPC       → Network

============================================================
'''