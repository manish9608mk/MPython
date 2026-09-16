'''
============================================================
AWS ECS — Elastic Container Service
============================================================

ECS = AWS service for running and managing containers.

Think:

Docker Image
     ↓
    ECS
     ↓
Running Container


WHY ECS?
--------

Instead of manually managing containers:

EC2
 ↓
Install Docker
 ↓
Run Containers
 ↓
Manage Everything


ECS helps manage:

    Containers
    Deployments
    Scaling
    Networking
    Health


ECS CORE COMPONENTS
-------------------

Cluster
   ↓
Service
   ↓
Task
   ↓
Container


CLUSTER
-------

A logical grouping of ECS resources.

Example:

ECS Cluster
    ├── API Service
    ├── Worker Service
    └── ML Service


TASK DEFINITION
---------------

A blueprint that defines how a container runs.

It can specify:

    Docker image
    CPU
    Memory
    Ports
    Environment variables
    IAM roles


TASK
----

A running instance of a Task Definition.

Task Definition
      ↓
     Task
      ↓
 Container


SERVICE
-------

Keeps the required number of tasks running.

Example:

Desired Count = 3

ECS Service
   ↓
┌──────┬──────┬──────┐
│ Task │ Task │ Task │
└──────┴──────┴──────┘


ECS LAUNCH OPTIONS
------------------

EC2 Launch Type
    → You manage the EC2 infrastructure

Fargate
    → AWS manages the underlying servers


ECS + FARGATE
-------------

Internet
    ↓
   ALB
    ↓
ECS Service
    ↓
Fargate Tasks
    ↓
Docker Containers


IAM
---

ECS Task
    ↓
IAM Task Role
    ↓
AWS Services


IMPORTANT COMMANDS
------------------

List ECS clusters:

aws ecs list-clusters


List services:

aws ecs list-services \
    --cluster CLUSTER_NAME


List running tasks:

aws ecs list-tasks \
    --cluster CLUSTER_NAME


Describe a task:

aws ecs describe-tasks \
    --cluster CLUSTER_NAME \
    --tasks TASK_ID


COST SAFETY
-----------

ECS itself is not necessarily the main cost.

The underlying compute can be BILLABLE:

    Fargate → Usage charges
    EC2     → Instance charges

For learning:

❌ Don't launch Fargate tasks unnecessarily
❌ Don't leave test workloads running
❌ Check pricing before creating resources


ECS vs EC2
----------

EC2
→ Virtual Machine

ECS
→ Container Orchestration

Fargate
→ Serverless compute for containers


PRODUCTION PATTERN
------------------

Users
  ↓
ALB
  ↓
ECS Service
  ↓
Fargate Tasks
  ↓
Docker Containers
  ↓
RDS / S3 / Other Services


REMEMBER
--------

Cluster
→ Group of ECS resources

Task Definition
→ Container blueprint

Task
→ Running workload

Service
→ Keeps desired tasks running

Fargate
→ Serverless container compute

ECS = Run and manage containers on AWS.

============================================================
'''