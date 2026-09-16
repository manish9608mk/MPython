'''
============================================================
AWS API GATEWAY — API Management
============================================================

API Gateway = Managed service for creating and exposing APIs.

Basic idea:

Client
  ↓
API Gateway
  ↓
Backend
  ↓
Response


COMMON ARCHITECTURE
-------------------

Client
   ↓
API Gateway
   ↓
┌───────────────┐
│ Lambda        │
│ ECS           │
│ EC2           │
│ Other Backend │
└───────────────┘


WHY API GATEWAY?
----------------

✅ Expose backend APIs
✅ Route requests
✅ Authentication / authorization
✅ Throttling
✅ Monitoring
✅ Request/response handling


API BASICS
----------

Example:

GET /users
POST /users
GET /users/123


API Gateway receives the request
and routes it to the configured backend.


TWO COMMON API TYPES
--------------------

REST API
    → Feature-rich REST APIs

HTTP API
    → Simpler, lower-cost API use cases


API GATEWAY + LAMBDA
--------------------

Client
  ↓
API Gateway
  ↓
Lambda
  ↓
Application Logic
  ↓
Response


API GATEWAY + ECS
-----------------

Client
  ↓
API Gateway
  ↓
Load Balancer / Backend
  ↓
ECS
  ↓
Application


AUTHENTICATION
--------------

API Gateway
    ↓
Authorization
    ↓
Backend


Possible approaches include:

    IAM
    JWT
    Cognito
    Lambda authorizers


THROTTLING
----------

Controls how many requests can be processed.

Example:

Too many requests
       ↓
   Throttling
       ↓
Request limited


IMPORTANT COMMANDS
------------------

List APIs:

aws apigateway get-rest-apis


Get a specific REST API:

aws apigateway get-rest-api \
    --rest-api-id API_ID


For HTTP APIs:

aws apigatewayv2 get-apis


COST SAFETY
-----------

API Gateway can incur charges based on usage
and configuration.

For learning:

❌ Don't create APIs unnecessarily
❌ Avoid uncontrolled request loops
❌ Check pricing before production-scale usage


PRODUCTION PATTERN
------------------

                    ┌── Lambda
Client → API Gateway ──┤
                    └── Backend


REMEMBER
--------

API Gateway
    → API entry point

Route
    → Where request goes

Integration
    → Backend connected to API

Authorization
    → Who can access

Throttling
    → Controls request rate

============================================================
'''