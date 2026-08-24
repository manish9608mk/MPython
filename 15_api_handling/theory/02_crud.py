# The core syntax you should memorize:
'''
GET
response = requests.get(url, timeout=10)

POST
response = requests.post(url, json=payload, timeout=10)

PUT
response = requests.put(url, json=payload, timeout=10)

PATCH
response = requests.patch(url, json=payload, timeout=10)

DELETE
response = requests.delete(url, timeout=10)

Then commonly:
response.raise_for_status()
data = response.json()


One Generic Pattern to Remember
For almost every API call:

import requests

url = "API_URL"

payload = {
    # data
}

response = requests.METHOD(
    url,
    json=payload,
    timeout=10
)

response.raise_for_status()

data = response.json()

print(data)


Where METHOD can be:
get
post
put
patch
delete







API ROADMAP:

1. HTTP Fundamentals
        ↓
2. requests library
        ↓
3. GET / POST / PUT / PATCH / DELETE
        ↓
4. Headers
        ↓
5. Query Parameters
        ↓
6. Authentication
        ↓
7. Response Handling
        ↓
8. JSON / Non-JSON
        ↓
9. Practical Error Handling  
        ↓
10. Timeout
        ↓
11. Retry + Exponential Backoff
        ↓
12. Pagination
        ↓
13. API Rate Limiting
        ↓
14. Idempotency
        ↓
15. REST API Design
        ↓
16. OAuth 2.0 + JWT
        ↓
17. API Security
        ↓
18. API Testing
        ↓
19. Build API Client
        ↓
20. FastAPI
        ↓
21. API + Database
        ↓
22. Dockerize API
        ↓
23. Deploy API on AWS
        ↓
24. Monitoring + Logging





One important thing:
For FAANG SDE interviews, API knowledge alone isn't enough. Your core preparation should remain:

Python
   +
DSA
   +
OOP
   +
DBMS/SQL
   +
Operating Systems
   +
Computer Networks
   +
System Design
   +
API/Backend fundamentals


For your Cloud → DevOps → Platform/SRE direction, APIs are especially useful because almost everything in cloud is API-driven:

Python
   ↓
HTTP / APIs
   ↓
AWS APIs
   ↓
Docker
   ↓
Kubernetes APIs
   ↓
Terraform
   ↓
CI/CD
   ↓
Monitoring
   ↓
Distributed Systems

So yes, what we're learning right now is worth learning deeply, but we don't need to turn this into an endless API course.
'''