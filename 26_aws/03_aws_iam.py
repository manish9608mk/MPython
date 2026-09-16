'''
============================================================
AWS IAM — Identity & Access Management
============================================================

IAM = WHO can do WHAT in AWS?


AUTHENTICATION vs AUTHORIZATION
--------------------------------

Authentication
    → Who are you?

Authorization
    → What are you allowed to do?


IAM COMPONENTS
--------------

User
    → Individual identity

Group
    → Collection of users

Policy
    → Permission rules

Role
    → Temporary identity/permissions
    → Commonly used by AWS services and applications


MENTAL MODEL
------------

Identity
    ↓
IAM
    ↓
Policy
    ↓
Permission
    ↓
AWS Resource


EXAMPLE
-------

Developer
    ↓
IAM Identity
    ↓
Policy
    ↓
Allow S3 Read
    ↓
S3 Bucket


LEAST PRIVILEGE
---------------

Give only the permissions required.

Avoid:

Application
    ↓
AdministratorAccess

Prefer:

Application
    ↓
Only required permissions


IAM USER vs ROLE
----------------

IAM User
    → Human identity

IAM Role
    → Temporary permissions
    → EC2 / ECS / Lambda / CI-CD commonly use roles


PRODUCTION PATTERN
------------------

Human
    ↓
SSO / IAM Identity Center
    ↓
Temporary credentials

Application
    ↓
IAM Role
    ↓
AWS Services


IMPORTANT COMMANDS
------------------

Check current AWS identity:

aws sts get-caller-identity


List IAM users:

aws iam list-users


List groups:

aws iam list-groups


Check policies attached to a user:

aws iam list-attached-user-policies \
    --user-name USER_NAME


SECURITY RULES
--------------

❌ Never hard-code access keys
❌ Never commit credentials to Git
❌ Never give unnecessary AdministratorAccess
❌ Never expose credentials

✅ Use IAM roles for applications
✅ Use least privilege
✅ Use MFA for human access


PROFESSIONAL WORKFLOW
---------------------

Who?
 ↓
What resource?
 ↓
Which action?
 ↓
Why?
 ↓
Minimum required permission


REMEMBER
--------

IAM = Identity + Permissions

You don't need to memorize every IAM command.
Understand the permission model and learn commands when needed.
============================================================
'''