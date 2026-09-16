'''
============================================================
                 AWS FUNDAMENTALS
============================================================


1. WHAT IS AWS?
------------------------------------------------------------

AWS (Amazon Web Services) is a cloud platform.

Instead of buying physical servers, we can use
computing resources provided by AWS.


                    AWS
                     |
        +------------+------------+
        |            |            |
      Compute      Storage      Database
       (EC2)         (S3)         (RDS)


------------------------------------------------------------
2. AWS ACCOUNT
------------------------------------------------------------

An AWS Account is the main boundary for your AWS resources.

Think:

    AWS Account
         |
    +----+----+
    |         |
   S3        EC2
             |
            RDS


------------------------------------------------------------
3. REGION
------------------------------------------------------------

A Region is a geographical location where AWS
resources are hosted.

Examples:

    ap-south-1  -> Mumbai
    us-east-1   -> N. Virginia
    eu-west-1   -> Ireland


              AWS
               |
       +-------+-------+
       |               |
    Mumbai          US East
   ap-south-1       us-east-1


Choose a Region based on:

    - Location
    - Latency
    - Cost
    - Service availability


------------------------------------------------------------
4. AVAILABILITY ZONE (AZ)
------------------------------------------------------------

A Region contains multiple Availability Zones.

Example:


             Mumbai Region
                  |
        +---------+---------+
        |         |         |
       AZ-a      AZ-b      AZ-c


AZs are separate locations designed to provide
better availability and fault isolation.


Remember:

    Region = geographical area
    AZ     = isolated location inside a Region


------------------------------------------------------------
5. VPC
------------------------------------------------------------

VPC = Virtual Private Cloud

VPC is your private network inside AWS.


                AWS
                 |
                VPC
                 |
        +--------+--------+
        |                 |
      Subnet A          Subnet B


Think:

    VPC = Big network


------------------------------------------------------------
6. SUBNET
------------------------------------------------------------

A Subnet is a smaller network inside a VPC.


                 VPC
                  |
          +-------+-------+
          |               |
       Subnet A        Subnet B


A subnet belongs to one Availability Zone.


------------------------------------------------------------
7. PUBLIC vs PRIVATE SUBNET
------------------------------------------------------------

PUBLIC SUBNET:

    Resource
       |
    Route Table
       |
      IGW
       |
    Internet


PRIVATE SUBNET:

    Resource
       |
    Route Table
       |
      No direct
     internet route


Common design:

    Internet
       |
       v
    Application
       |
       v
    Database

Database is usually kept private.


------------------------------------------------------------
8. ROUTE TABLE
------------------------------------------------------------

Route Table decides:

    "Where should network traffic go?"


Example:

    10.0.0.0/16  -> local
    0.0.0.0/0    -> Internet Gateway


Think:

    Route Table = Traffic direction


------------------------------------------------------------
9. INTERNET GATEWAY
------------------------------------------------------------

IGW = Internet Gateway

It provides a path between a VPC and the internet
for appropriately configured resources.


    Resource
       |
    Route Table
       |
      IGW
       |
    Internet


IGW alone does NOT make a resource public.


------------------------------------------------------------
10. SECURITY GROUP
------------------------------------------------------------

Security Group = Virtual firewall.

It controls allowed network traffic.


    Application
         |
      TCP 5432
         |
         v
      Database


Example:

    Allow PostgreSQL
    Port: 5432
    Source: Application Security Group


Think:

    Security Group = Who can connect?


------------------------------------------------------------
11. IAM
------------------------------------------------------------

IAM = Identity and Access Management.

IAM answers:

    WHO are you?
    WHAT are you allowed to do?


Important IAM concepts:

    User
    Group
    Policy
    Role


Think:

    IAM = Identity + Permissions


------------------------------------------------------------
12. COMPUTE
------------------------------------------------------------

Compute = Where does my application run?

Examples:

    EC2     -> Virtual server
    Lambda  -> Run code without managing servers
    ECS/EKS -> Containers


------------------------------------------------------------
13. STORAGE
------------------------------------------------------------

S3 = Object Storage.

Used for:

    Images
    Videos
    PDFs
    Backups
    Datasets
    Model files


Think:

    S3 = Cloud storage for files/objects


------------------------------------------------------------
14. DATABASE
------------------------------------------------------------

RDS = Managed relational database service.

Examples:

    PostgreSQL
    MySQL


Think:

    RDS = Managed database


------------------------------------------------------------
15. S3 vs DATABASE
------------------------------------------------------------

Files:

    image.jpg
    model.pkl
    dataset.csv

          ↓

         S3


Structured application data:

    users
    orders
    products

          ↓

       Database


Remember:

    S3      -> Files / Objects
    Database-> Structured data


------------------------------------------------------------
16. BASIC AWS ARCHITECTURE
------------------------------------------------------------


                    INTERNET
                        |
                        v
                  Load Balancer
                        |
                        v
                   Application
                    /       \
                   /         \
                  v           v
                RDS          S3
             Database      Storage


Everything can be organized inside:

                    AWS
                     |
                    VPC
                     |
              +------+------+
              |             |
           Subnet        Subnet


IAM controls permissions.

Security Groups control network access.

Route Tables control traffic direction.


------------------------------------------------------------
17. AWS CLI
------------------------------------------------------------

CLI = Command Line Interface.

It lets us work with AWS from the terminal.


Basic structure:

    aws <service> <operation>


Examples:

    aws s3 ls

    aws ec2 describe-vpcs

    aws rds describe-db-instances


You DON'T need to memorize every command.

Understand:

    service + operation


------------------------------------------------------------
18. MOST IMPORTANT MENTAL MODEL
------------------------------------------------------------


    AWS Account
         |
       Region
         |
        VPC
         |
      Subnets
         |
    +----+----+
    |         |
  Compute   Database
              |
             S3


    IAM
     ↓
    Who can access what?


    Route Table
     ↓
    Where does traffic go?


    Security Group
     ↓
    Which traffic is allowed?


------------------------------------------------------------
19. AWS GOLDEN RULE
------------------------------------------------------------

Before creating anything:

    1. Understand it
    2. Check if it costs money
    3. Create only when necessary
    4. Verify it
    5. Delete when no longer needed

------------------------------------
AWS
│
├── Region
│    └── Availability Zones
│
├── VPC
│    └── Subnets
│
├── Compute → EC2 / ECS / Lambda
├── Storage → S3
├── Database → RDS
├── IAM → Permissions
└── Security Group → Network Firewall
'''