'''
============================================================
15_AWS_ECR.py
AWS ECR — Elastic Container Registry
============================================================

ECR = AWS service for storing Docker images.

Think:

Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
ECR Repository
    ↓
ECS / Fargate
    ↓
Running Container


WHY ECR?
--------

Your application needs a place to store
container images before ECS runs them.

ECR provides:

    → Private Docker image storage
    → Image versioning through tags
    → Access control with IAM
    → Integration with ECS


ECR REPOSITORY
--------------

A repository stores Docker images.

Example:

ECR
└── murphai-backend
      ├── v1
      ├── v2
      └── latest


IMAGE TAG
---------

A tag identifies a particular image version.

Example:

myapp:v1
myapp:v2
myapp:latest


BASIC WORKFLOW
--------------

Developer
    ↓
Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
ECR
    ↓
ECS / Fargate
    ↓
Container


ECR + ECS
---------

ECR
 ↓
Docker Image
 ↓
ECS Task Definition
 ↓
Fargate Task
 ↓
Container


IMPORTANT COMMANDS
------------------

List ECR repositories:

aws ecr describe-repositories


List images in a repository:

aws ecr list-images \
    --repository-name REPOSITORY_NAME


Get repository details:

aws ecr describe-repositories \
    --repository-names REPOSITORY_NAME


LOGIN TO ECR
------------

Docker needs authentication before pushing
images to a private ECR repository.

Typical command:

aws ecr get-login-password \
    --region REGION | \
docker login \
    --username AWS \
    --password-stdin ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com


PUSH WORKFLOW
-------------

1. Build image

docker build -t myapp .


2. Tag image for ECR

docker tag myapp:latest \
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/myapp:latest


3. Push image

docker push \
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/myapp:latest


PULL WORKFLOW
-------------

ECS
 ↓
ECR
 ↓
Pull Docker Image
 ↓
Run Container


ECR vs S3
---------

ECR
→ Container / Docker images

S3
→ General object/file storage


COST SAFETY
-----------

ECR storage and data transfer can incur charges.

For learning:

❌ Don't push unnecessary large images
❌ Don't keep unused images forever
❌ Use lifecycle policies for cleanup when appropriate


PRODUCTION THINKING
-------------------

Source Code
    ↓
Docker Build
    ↓
Image
    ↓
ECR
    ↓
ECS
    ↓
Running Application


REMEMBER
--------

ECR = Docker Image Registry

Repository
→ Stores images

Image
→ Container package

Tag
→ Image version/identifier

ECR + ECS
→ Store image → Run container

============================================================
'''