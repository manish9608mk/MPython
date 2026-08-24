'''
API
===

API stands for Application Programming Interface.

An API is a way for two different software systems
to communicate with each other.

Simple definition:

API = A set of rules that allows one program
      to request data or functionality from another program.


REAL-WORLD ANALOGY
==================

Think about a restaurant.

You → Customer
Restaurant → Server/Kitchen
Menu → Available options
Waiter → API

You don't directly enter the kitchen.

Instead:

You
 ↓
Waiter
 ↓
Kitchen
 ↓
Food
 ↓
Waiter
 ↓
You


Similarly in software:

Client
 ↓
API Request
 ↓
Server
 ↓
Database / Service
 ↓
API Response
 ↓
Client


Example:

You open a weather application.

The application needs current weather data.

It sends a request to a weather API:

Application
    ↓
Weather API
    ↓
Weather Server
    ↓
Weather Data
    ↓
API Response
    ↓
Application


WHY DO WE NEED APIs?
====================

Without APIs, applications would need
direct access to another system's internal
implementation.

APIs provide a controlled interface.

For example:

Your application
      ↓
     API
      ↓
Payment Service

Your application does not need to know
how the payment service internally works.

It only needs to know:

- Where to send the request
- What data to send
- What response it will receive


IMPORTANT IDEA
==============

API hides internal implementation details.

This is called:

ABSTRACTION

Example:

You call:

GET /users/10

You don't need to know:

- How the server finds the user
- Which database it uses
- How the database is structured
- How the backend code works

You only care about:

Request → Response


CLIENT AND SERVER
=================

Most APIs work using a client-server model.

Client:
→ The application making the request.

Server:
→ The system receiving the request
   and processing it.


Example:

Python Program
      ↓
    Request
      ↓
     API
      ↓
    Server
      ↓
   Database
      ↓
    Response
      ↓
Python Program


WHAT IS AN API REQUEST?
=======================

An API request is a message sent by
the client to the server.

A request can contain:

1. HTTP Method
2. URL
3. Headers
4. Query Parameters
5. Request Body


Example:

GET https://api.example.com/users/10


Here:

GET
→ HTTP method

https://api.example.com
→ Server/API address

/users/10
→ Endpoint


WHAT IS AN API RESPONSE?
========================

The server processes the request
and sends a response back.

Example:

{
    "id": 10,
    "name": "Manish",
    "age": 23
}


The response usually contains:

- Status code
- Headers
- Response body


HTTP
====

Most web APIs communicate using HTTP.

HTTP stands for:

HyperText Transfer Protocol.


Common HTTP methods:

GET
POST
PUT
PATCH
DELETE


GET
===

Used to retrieve data.

Example:

GET /videos

Meaning:

"Give me the videos."


POST
====

Used to create new data.

Example:

POST /videos

Request body:

{
    "name": "Python Tutorial",
    "time": "10 min"
}

Meaning:

"Create a new video."


PUT
===

Used to completely update
an existing resource.

Example:

PUT /videos/10

Request:

{
    "name": "Advanced Python",
    "time": "20 min"
}


PATCH
=====

Used to partially update
an existing resource.

Example:

PATCH /videos/10

Request:

{
    "name": "Advanced Python"
}


DELETE
======

Used to delete a resource.

Example:

DELETE /videos/10

Meaning:

"Delete video with ID 10."


CRUD AND HTTP
=============

CRUD operations commonly map to HTTP methods:

CREATE → POST
READ   → GET
UPDATE → PUT / PATCH
DELETE → DELETE


API ENDPOINT
============

An endpoint is a specific URL
through which an API provides a resource
or operation.

Example:

/users
/videos
/products
/orders


Example:

GET /users

→ Get all users


GET /users/10

→ Get user with ID 10


POST /users

→ Create a user


DELETE /users/10

→ Delete user 10


URL
===

URL stands for:

Uniform Resource Locator.

Example:

https://api.example.com/users/10


Parts:

https://
→ Protocol

api.example.com
→ Domain / Host

/users/10
→ Path


QUERY PARAMETERS
=================

Query parameters are additional parameters
provided in the URL.

Example:

GET /videos?category=python


Here:

category=python

is a query parameter.


Multiple parameters:

GET /videos?category=python&limit=10


Here:

category = python
limit = 10


PATH PARAMETERS
===============

Path parameters are part of the URL path.

Example:

GET /videos/10


Here:

10

is the video ID.


Difference:

Path parameter:

/videos/10


Query parameter:

/videos?id=10


HEADERS
=======

Headers contain additional information
about the request or response.

Example:

Content-Type: application/json

Authorization: Bearer TOKEN


Common headers:

Content-Type
→ Specifies the format of the data.

Authorization
→ Used to send authentication information.

Accept
→ Specifies which response format
  the client accepts.


REQUEST BODY
============

The request body contains data
sent to the server.

Mostly used with:

POST
PUT
PATCH


Example:

{
    "name": "Python",
    "time": "10 min"
}


JSON
====

JSON is one of the most commonly used
data formats in APIs.

Example:

{
    "name": "Python",
    "language": "Python",
    "level": "Advanced"
}


Python:

{
    "name": "Python",
    "language": "Python",
    "level": "Advanced"
}

JSON:

{
    "name": "Python",
    "language": "Python",
    "level": "Advanced"
}


API RESPONSE STATUS CODES
=========================

HTTP status codes tell the client
what happened with the request.


2xx
---

Success.


200 OK
→ Request succeeded.


201 Created
→ Resource was successfully created.


204 No Content
→ Request succeeded but there is
  no response body.


4xx
---

Client-side error.


400 Bad Request
→ Request data is invalid.


401 Unauthorized
→ Authentication is required
  or credentials are invalid.


403 Forbidden
→ Client is authenticated
  but does not have permission.


404 Not Found
→ Requested resource does not exist.


409 Conflict
→ Request conflicts with
  the current state of the resource.


5xx
---

Server-side error.


500 Internal Server Error
→ Server encountered an unexpected error.


502 Bad Gateway
→ Server received an invalid response
  from another server.


503 Service Unavailable
→ Service is temporarily unavailable.


IMPORTANT STATUS CODE MEMORY
============================

200 → Success
201 → Created
204 → Success, no content

400 → Bad request
401 → Authentication problem
403 → Permission problem
404 → Not found
409 → Conflict

500 → Server error
502 → Bad gateway
503 → Service unavailable


REST API
========

REST stands for:

Representational State Transfer.

A REST API is an API designed around
resources and HTTP methods.


Example resource:

videos


REST API:

GET    /videos
POST   /videos
GET    /videos/10
PUT    /videos/10
PATCH  /videos/10
DELETE /videos/10


This is commonly called:

RESTful API.


RESOURCE
========

A resource is an object/data
that an API exposes.

Examples:

Users
Videos
Products
Orders
Payments


Example:

/users
/videos
/products
/orders


AUTHENTICATION
==============

Authentication answers:

"Who are you?"


Example:

Username + Password
API Key
Token
JWT
OAuth


Example header:

Authorization: Bearer <token>


AUTHORIZATION
=============

Authorization answers:

"What are you allowed to do?"


Example:

A normal user:

Can:
→ View videos

Cannot:
→ Delete another user's videos


An admin:

Can:
→ View
→ Add
→ Update
→ Delete


Authentication vs Authorization
================================

Authentication
→ Who are you?

Authorization
→ What are you allowed to do?


API KEY
=======

An API key is a credential
used by some APIs to identify
and authenticate a client/application.

Example:

GET /weather?api_key=ABC123


Important:

Never expose real API keys
inside public GitHub repositories.


TOKEN
=====

A token is another common way
to authenticate API requests.

Example:

Authorization: Bearer TOKEN


API DOCUMENTATION
=================

API documentation explains
how developers can use an API.

It usually contains:

- Endpoints
- HTTP methods
- Parameters
- Headers
- Request body
- Response format
- Status codes
- Authentication
- Examples


Example documentation:

GET /users

Response:

[
    {
        "id": 1,
        "name": "Alice"
    },
    {
        "id": 2,
        "name": "Bob"
    }
]


API HANDLING IN PYTHON
======================

Python can communicate with APIs
using libraries such as:

requests
httpx
urllib


The requests library is commonly used
for learning and simple API clients.

Example:

import requests

response = requests.get(
    "https://api.example.com/users"
)


STATUS CODE
===========

print(response.status_code)


RESPONSE BODY
=============

print(response.text)


JSON RESPONSE
=============

data = response.json()

print(data)


Example:

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)


IMPORTANT:
==========

response.json()

converts a JSON response body
into a Python object.

Usually:

JSON object → Python dictionary

JSON array → Python list


API REQUEST FLOW
================

Python Application
        |
        | HTTP Request
        ↓
      API
        |
        ↓
     Server
        |
        ↓
    Database
        |
        ↓
     Server
        |
        | HTTP Response
        ↓
Python Application


Example:

Python:

requests.get("/videos")


Server:

SELECT * FROM videos


Server Response:

[
    {
        "id": 1,
        "name": "Python",
        "time": "10 min"
    }
]


Python:

data = response.json()


API + DATABASE
==============

A common backend architecture:

Client
  ↓
API
  ↓
Backend
  ↓
Database


Example:

YouTube-like application:

Frontend
    ↓
GET /videos
    ↓
Python API
    ↓
SQLite/PostgreSQL
    ↓
videos table
    ↓
JSON response
    ↓
Frontend


YOUR YOUTUBE MANAGER
====================

Currently:

Python
   ↓
SQLite
   ↓
videos table


After learning API:

Client
   ↓
API
   ↓
Python Backend
   ↓
SQLite
   ↓
videos table


Eventually:

Frontend
   ↓
REST API
   ↓
Python Backend
   ↓
Database


WHY API IS IMPORTANT FOR YOU
============================

API knowledge is important for:

- Backend development
- Cloud engineering
- DevOps
- Platform engineering
- SRE
- Microservices
- Automation
- AWS services
- CI/CD systems
- Kubernetes applications
- AI/ML applications


REAL-WORLD EXAMPLES
===================

Weather Application
→ Weather API

Payment Application
→ Payment API

Maps Application
→ Maps API

GitHub automation
→ GitHub API

AWS automation
→ AWS APIs

AI application
→ AI/LLM APIs


API vs LIBRARY
==============

Library:

Your code
   ↓
Library function
   ↓
Result


API:

Your application
   ↓
Request
   ↓
Another application/service
   ↓
Response


Simple difference:

Library
→ Usually code you directly use
  inside your application.

API
→ Interface through which
  software systems communicate.


API vs DATABASE
===============

Database:
→ Stores data.

API:
→ Provides a controlled way
  to access or modify data.


Example:

Frontend
   ↓
API
   ↓
Database


The frontend normally should not
directly access the database.

The backend/API controls
database access.


IMPORTANT INTERVIEW QUESTIONS
=============================

1. What is an API?

2. What is REST API?

3. What is an endpoint?

4. Difference between GET and POST?

5. Difference between PUT and PATCH?

6. What is a status code?

7. Difference between 401 and 403?

8. What is JSON?

9. What are headers?

10. What are query parameters?

11. What are path parameters?

12. What is authentication?

13. What is authorization?

14. What is an API key?

15. What is a token?

16. What is CRUD?

17. How does a Python program consume an API?

18. How does an API communicate with a database?


MENTAL MODEL
============

Client
  ↓
HTTP Request
  ↓
API Endpoint
  ↓
Backend Logic
  ↓
Database / External Service
  ↓
Backend Logic
  ↓
HTTP Response
  ↓
Client


MOST IMPORTANT THINGS TO REMEMBER
=================================

API
→ Allows software systems to communicate.

HTTP
→ Communication protocol commonly used by web APIs.

Endpoint
→ Specific API URL.

GET
→ Read.

POST
→ Create.

PUT/PATCH
→ Update.

DELETE
→ Delete.

JSON
→ Common API data format.

Status Code
→ Tells what happened.

Authentication
→ Who are you?

Authorization
→ What can you do?

Request
→ Client → Server.

Response
→ Server → Client.

REST API
→ Resource-oriented API using HTTP conventions.
'''