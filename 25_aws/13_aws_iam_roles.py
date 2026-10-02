'''
============================================================
AWS IAM ROLES — Workload Identity
============================================================

IAM Role = Temporary permissions that can be assumed
by a trusted identity.

Most importantly:

Application
    ↓
IAM Role
    ↓
AWS Service


WHY ROLES?
----------

Avoid putting long-term AWS access keys inside
applications.

Bad:

Application
    ↓
Hard-coded Access Key
    ↓
S3


Better:

Application
    ↓
IAM Role
    ↓
S3


COMMON USE CASES
----------------

EC2
 ↓
IAM Role
 ↓
S3 / CloudWatch / etc.


ECS Task
 ↓
IAM Task Role
 ↓
AWS Services


Lambda
 ↓
Execution Role
 ↓
AWS Services


CI/CD
 ↓
IAM Role
 ↓
Deploy to AWS


ROLE COMPONENTS
---------------

Trust Policy
    ↓
Who can assume the role?

Permissions Policy
    ↓
What can the role do?


Example:

EC2
 ↓
Trust Policy
 ↓
Can assume role
 ↓
Permissions Policy
 ↓
Read S3


TRUST vs PERMISSION
-------------------

Trust Policy:

"WHO can use this role?"

Permissions Policy:

"WHAT can this role do?"


LEAST PRIVILEGE
---------------

Role
 ↓
Only required permissions
 ↓
Specific AWS resources


IMPORTANT COMMANDS
------------------

List IAM roles:

aws iam list-roles


Get role details:

aws iam get-role \
    --role-name ROLE_NAME


List policies attached to a role:

aws iam list-attached-role-policies \
    --role-name ROLE_NAME


Check a role's inline policies:

aws iam list-role-policies \
    --role-name ROLE_NAME


PRODUCTION PATTERN
------------------

Human
 ↓
SSO / Identity Center
 ↓
Temporary access


Application
 ↓
IAM Role
 ↓
AWS Services


SECURITY RULES
--------------

❌ Don't hard-code credentials
❌ Don't share access keys
❌ Don't give unnecessary permissions

✅ Use roles
✅ Use temporary credentials
✅ Use least privilege
✅ Separate roles by workload/purpose


REMEMBER
--------

IAM User
    → Human identity

IAM Role
    → Temporary/workload identity

Trust Policy
    → WHO can assume the role

Permission Policy
    → WHAT the role can do

Best mental model:

"Role = identity + temporary permissions"

============================================================
'''