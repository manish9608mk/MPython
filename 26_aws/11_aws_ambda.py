'''
============================================================
AWS LAMBDA — Serverless Compute
============================================================

Lambda = Run code without managing servers.

Traditional:

User
 ↓
EC2
 ↓
Application
 ↓
You manage server


Lambda:

User / Event
     ↓
  Lambda
     ↓
   Code


SERVERLESS
----------

You don't manage:

    OS
    Server hardware
    Server provisioning
    Server scaling


You mainly manage:

    Code
    Configuration
    Permissions


HOW LAMBDA WORKS
----------------

Event
  ↓
Lambda Function
  ↓
Python / Node.js / Java / etc.
  ↓
Result


EXAMPLE
-------

API Request
    ↓
API Gateway
    ↓
Lambda
    ↓
Process Request
    ↓
Response


COMMON USE CASES
----------------

✅ APIs
✅ Background processing
✅ File processing
✅ Scheduled jobs
✅ Event-driven automation
✅ Lightweight backend tasks


LAMBDA + S3
-----------

File uploaded
     ↓
    S3
     ↓
Lambda triggered
     ↓
Process file


LAMBDA + IAM
------------

Lambda
  ↓
IAM Execution Role
  ↓
AWS Services

Example:

Lambda
  ↓
IAM Role
  ↓
Read from S3


IMPORTANT CONCEPTS
------------------

Function
→ Your executable code

Trigger
→ Event that starts the function

Execution Role
→ IAM permissions for Lambda

Runtime
→ Environment used to execute code

Timeout
→ Maximum execution time


IMPORTANT COMMANDS
------------------

List Lambda functions:

aws lambda list-functions


Get function details:

aws lambda get-function \
    --function-name FUNCTION_NAME


Get function configuration:

aws lambda get-function-configuration \
    --function-name FUNCTION_NAME


COST SAFETY
-----------

Lambda is generally usage-based.

For learning:

❌ Don't create unnecessary functions/resources
❌ Avoid uncontrolled high-frequency triggers
❌ Understand invocation and execution costs


EC2 vs LAMBDA
-------------

EC2
→ You manage the server

Lambda
→ AWS manages the server infrastructure


EC2:
Continuous server-oriented workloads

Lambda:
Event-driven / short-lived workloads


PRODUCTION PATTERN
------------------

Client
  ↓
API Gateway
  ↓
Lambda
  ↓
AWS Services


REMEMBER
--------

Lambda = Serverless compute

Function       → Code
Trigger        → Starts function
Execution Role → Permissions
Runtime        → Execution environment

============================================================
'''