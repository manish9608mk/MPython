'''
============================================================
                       AWS CLI
============================================================


1. WHAT IS AWS CLI?
------------------------------------------------------------

AWS CLI = Command Line Interface.

It lets us manage AWS from the terminal.

Instead of:

    Terminal → Browser → AWS Console

We can do:

    Terminal → AWS CLI → AWS


------------------------------------------------------------
2. BASIC COMMAND STRUCTURE
------------------------------------------------------------

    aws <service> <operation>


Example:

    aws ec2 describe-vpcs


Meaning:

    aws
      ↓
    EC2 service
      ↓
    describe VPCs


Another example:

    aws s3 ls

    aws rds describe-db-instances


------------------------------------------------------------
3. PROFILE
------------------------------------------------------------

A profile tells AWS CLI which configured identity
to use.

Example:

    --profile my-profile


Command:

    aws sts get-caller-identity \
        --profile my-profile


Think:

    Profile = WHO am I?


------------------------------------------------------------
4. REGION
------------------------------------------------------------

Region tells AWS where to perform the operation.

Example:

    --region ap-south-1


Command:

    aws ec2 describe-vpcs \
        --region ap-south-1


Think:

    Region = WHERE?


------------------------------------------------------------
5. PROFILE + REGION
------------------------------------------------------------

Common pattern:


    aws <service> <operation> \
        --profile <profile> \
        --region <region>


Example:

    aws ec2 describe-vpcs \
        --profile my-profile \
        --region ap-south-1


Think:


          COMMAND
             |
       +-----+-----+
       |           |
    PROFILE       REGION
       |           |
      WHO?        WHERE?


------------------------------------------------------------
6. IMPORTANT COMMAND TYPES
------------------------------------------------------------

READ:

    describe-*
    list-*
    get-*


Examples:

    aws ec2 describe-vpcs
    aws ec2 describe-subnets
    aws s3api list-buckets


These are mainly used to inspect AWS.


CREATE:

    create-*


MODIFY:

    put-*
    update-*
    modify-*


DELETE:

    delete-*
    terminate-*


Important:

    READ → usually just inspection

    CREATE/MODIFY → changes AWS

    DELETE → removes AWS resources


------------------------------------------------------------
7. VERIFY YOUR IDENTITY
------------------------------------------------------------

Very useful command:


    aws sts get-caller-identity


Use it when you want to know:

    "Which AWS identity am I currently using?"


------------------------------------------------------------
8. OUTPUT
------------------------------------------------------------

Useful output formats:


    --output json

    --output table

    --output text


Example:

    aws ec2 describe-vpcs --output table


Think:

    JSON  → detailed / scripts
    table → easy for humans


------------------------------------------------------------
9. QUERY
------------------------------------------------------------

    --query

is used to select only the information you need.


Example:


    aws ec2 describe-vpcs \
        --query 'Vpcs[].VpcId'


Instead of showing everything,
it shows only VPC IDs.


Think:

    AWS response
         ↓
      --query
         ↓
    Only required data


------------------------------------------------------------
10. PROFESSIONAL WORKFLOW
------------------------------------------------------------


    INSPECT
       ↓
    UNDERSTAND
       ↓
    CREATE / MODIFY
       ↓
    VERIFY
       ↓
    DELETE when no longer needed


Never blindly run a command.


------------------------------------------------------------
11. COST SAFETY
------------------------------------------------------------

AWS CLI itself is not what creates the bill.

Resources can create charges.

For example:


    describe-vpcs
        → inspection


    create-db-instance
        → creates RDS
        → can cost money


    run-instances
        → creates EC2
        → can cost money


Before CREATE:

    Understand the resource
    Check its cost
    Create only if necessary


------------------------------------------------------------
12. DO I NEED TO MEMORIZE COMMANDS?
------------------------------------------------------------

NO.


Remember the pattern:


    aws
      ↓
    service
      ↓
    operation
      ↓
    options


Example:


    aws ec2 describe-vpcs


If you forget the exact command:

    Check AWS documentation.


Real engineers use documentation.


------------------------------------------------------------
13. CONSOLE vs CLI vs TERRAFORM
------------------------------------------------------------


    AWS Console
        ↓
    Manual / Visual


    AWS CLI
        ↓
    Terminal / Commands


    Terraform
        ↓
    Infrastructure as Code


Professional environments commonly use
automation and Infrastructure as Code.

But CLI knowledge is important for:

    debugging
    inspection
    troubleshooting
    automation


============================================================
MOST IMPORTANT
============================================================


    PROFILE = WHO?

    REGION  = WHERE?

    CLI     = HOW I TALK TO AWS?

    describe/list/get = READ

    create/modify = CHANGE

    delete = REMOVE

---------------
revision: 
aws
 ↓
service
 ↓
operation
 ↓
--profile  → WHO?
--region   → WHERE?

READ → Understand
WRITE → Check impact/cost
CHANGE → Verify
DELETE → Be careful
'''