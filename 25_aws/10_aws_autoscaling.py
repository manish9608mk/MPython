'''
============================================================
AWS AUTO SCALING — EC2 Auto Scaling
============================================================

Auto Scaling = Automatically adjusts the number of
EC2 instances based on demand.


WITHOUT AUTO SCALING
--------------------

Users
  ↓
EC2
  ↓
Traffic increases
  ↓
Server overloaded


WITH AUTO SCALING
-----------------

              ┌── EC2
Users → ALB ──┼── EC2
              ├── EC2
              └── EC2
                   ↑
              Auto Scaling
              adds/removes
              instances


AUTO SCALING GROUP (ASG)
------------------------

ASG manages a group of EC2 instances.

It defines:

    Minimum instances
    Desired instances
    Maximum instances


Example:

Min     = 2
Desired = 2
Max     = 5


Traffic increases
    ↓
ASG launches instances

Traffic decreases
    ↓
ASG removes unnecessary instances


SCALING TYPES
-------------

Scale Out
    → Add more instances

Scale In
    → Remove instances


HEALTH CHECKS
-------------

ASG can replace unhealthy instances.

Unhealthy EC2
     ↓
ASG detects problem
     ↓
Instance removed
     ↓
New EC2 launched


BASIC ARCHITECTURE
------------------

                 Internet
                    ↓
                   ALB
                    ↓
              Target Group
                    ↓
             Auto Scaling Group
              ┌─────┼─────┐
             EC2   EC2   EC2


LAUNCH TEMPLATE
---------------

A Launch Template defines how new EC2 instances
should be created.

It can specify:

    AMI
    Instance type
    Security group
    Storage
    User data


IMPORTANT COMMANDS
------------------

List Auto Scaling Groups:

aws autoscaling describe-auto-scaling-groups


List Launch Templates:

aws ec2 describe-launch-templates


Check a specific Auto Scaling Group:

aws autoscaling describe-auto-scaling-groups \
    --auto-scaling-group-names ASG_NAME


COST SAFETY
-----------

Auto Scaling itself is a management feature,
but the EC2 instances it launches are generally
BILLABLE.

So:

❌ Don't create an ASG just for practice
❌ Don't set unnecessarily high maximum capacity
❌ Don't leave test infrastructure running


PRODUCTION PATTERN
------------------

Users
  ↓
ALB
  ↓
Target Group
  ↓
Auto Scaling Group
  ↓
EC2 Instances


REMEMBER
--------

ASG
→ Manages EC2 capacity

Scale Out
→ Add instances

Scale In
→ Remove instances

Launch Template
→ Defines how instances are created

Min / Desired / Max
→ Controls capacity

============================================================
'''