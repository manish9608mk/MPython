'''
====================================================================
                    AWS FUNDAMENTALS
====================================================================

GOAL:

Understand the basic AWS architecture.

    AWS
    Account
    Region
    Availability Zone
    VPC
    Subnet
    Compute
    Storage
    Database
    IAM
    Security Group
    Route Table

====================================================================
1. WHAT IS CLOUD COMPUTING?
====================================================================

Before AWS, understand Cloud Computing.

Traditional approach:

    Company
       |
       v
    Buy physical servers
       |
       v
    Install OS
       |
       v
    Configure network
       |
       v
    Maintain hardware


Cloud approach:

    Company
       |
       v
    Cloud Provider
       |
       +---- Compute
       +---- Storage
       +---- Database
       +---- Networking
       +---- Security


Instead of buying and maintaining all physical infrastructure,
we can use infrastructure provided by a cloud provider.


====================================================================
2. WHAT IS AWS?
====================================================================

AWS = Amazon Web Services.

AWS is a cloud platform.

It provides many services for building and running applications.


Common examples:

    EC2       -> Virtual servers
    S3        -> Object/file storage
    RDS       -> Managed relational databases
    VPC       -> Networking
    IAM       -> Identity and permissions
    Lambda    -> Run code without managing a traditional server
    ECS/EKS   -> Containers
    CloudWatch-> Monitoring


Think of AWS like a large toolbox.

You choose the right tool for the problem.


====================================================================
3. AWS ACCOUNT
====================================================================

An AWS Account is the main boundary where your AWS resources
and billing are organized.


                    AWS ACCOUNT
                         |
          +--------------+--------------+
          |              |              |
         VPC             S3            IAM
          |
       +--+--+
       |     |
      EC2   RDS


A company may have separate accounts for different environments:

    Development
    Staging
    Production


IMPORTANT:

    Account = your AWS environment/boundary

    Region  = where resources are geographically located


====================================================================
4. REGION
====================================================================

A Region is a geographical AWS location.

Examples:

    ap-south-1
    us-east-1
    eu-west-1


Think:

                    AWS
                     |
        +------------+------------+
        |            |            |
      Region A     Region B     Region C


You normally choose a Region when creating regional resources.


WHY DOES REGION MATTER?

    - Latency
    - Data residency/compliance
    - Service availability
    - Cost
    - Disaster recovery design


Simple rule:

    Always know which AWS Region you are working in.


====================================================================
5. AVAILABILITY ZONE
====================================================================

A Region contains multiple Availability Zones (AZs).


                    REGION
                  ap-south-1
                       |
          +------------+------------+
          |            |            |
         AZ-a         AZ-b         AZ-c


An Availability Zone is an isolated location inside a Region.

Why?

To reduce the impact of failures.

For example:


             REGION
                |
        +-------+-------+
        |               |
       AZ-a            AZ-b
        |               |
      App A            App B


If one AZ has a problem, a properly designed application
may continue operating through another AZ.


IMPORTANT:

    Region
        = geographical area

    Availability Zone
        = isolated location inside that Region


====================================================================
6. WHAT IS A RESOURCE?
====================================================================

A SERVICE is a category.

A RESOURCE is the actual thing you create.


Example:


    S3
     |
     +---- Bucket A
     +---- Bucket B


    RDS
     |
     +---- Database A
     +---- Database B


S3 and RDS are SERVICES.

The buckets and databases are RESOURCES.


Think:

    Service = type of tool

    Resource = actual thing created using that tool


====================================================================
7. COMPUTE
====================================================================

Compute means:

    "Where does my application/code run?"


Examples:

    EC2
    Lambda
    ECS
    EKS


Simple architecture:


              Application Code
                     |
                     v
                   COMPUTE
                     |
          +----------+----------+
          |          |          |
         EC2       ECS/EKS    Lambda


EC2:

    A virtual server.


Lambda:

    Run code without managing a traditional server yourself.


ECS/EKS:

    Run containerized applications.


The important question is:

    "Where is my application running?"


====================================================================
8. STORAGE
====================================================================

Storage means:

    "Where do I store files and objects?"


Examples:

    Images
    Videos
    PDFs
    Datasets
    Backups
    Model files
    Logs


AWS S3 is object storage.


                Application
                     |
                     v
                    S3
                     |
          +----------+----------+
          |          |          |
       image.jpg  data.csv   model.pkl


Mental model:

    S3 = cloud storage for objects/files


S3 is NOT a replacement for a relational database.


====================================================================
9. DATABASE
====================================================================

A database stores application data in a structured way.


Example:


    Users
    ----------------
    id
    name
    email


    Orders
    ----------------
    id
    user_id
    amount


AWS RDS provides managed relational databases.


             Application
                  |
                  v
                 RDS
                  |
                  v
            PostgreSQL/MySQL


RDS can manage much of the underlying database infrastructure,
while you focus on the database and application requirements.


====================================================================
10. S3 VS DATABASE
====================================================================

This difference is very important.


Suppose we have a user:


    User information:

        id
        name
        email


    -> Database


User's profile picture:


    profile.jpg


    -> S3


So:


                 APPLICATION
                  /        \
                 /          \
                v            v
             DATABASE       S3
           structured      files
              data        /objects


Simple rule:

    Structured application data
        -> Database


    Files/objects
        -> S3


====================================================================
11. VPC
====================================================================

VPC = Virtual Private Cloud.

A VPC is your logical network inside AWS.


                    AWS ACCOUNT
                         |
                         v
                        VPC
                         |
             +-----------+-----------+
             |                       |
        Public Subnet           Private Subnet


Inside a VPC you can control things such as:

    - IP ranges
    - Subnets
    - Routing
    - Network access


Mental model:

    VPC = your cloud network


====================================================================
12. SUBNET
====================================================================

A subnet is a smaller network inside a VPC.


Example:


                    VPC
                10.0.0.0/16
                     |
          +----------+----------+
          |                     |
       Subnet A              Subnet B
       10.0.1.0/24           10.0.2.0/24


A subnet belongs to one Availability Zone.


Example:


                  REGION
                     |
          +----------+----------+
          |                     |
         AZ-a                  AZ-b
          |                     |
       Subnet A              Subnet B


Mental model:

    VPC = large network

    Subnet = smaller section of that network


====================================================================
13. PUBLIC AND PRIVATE SUBNET
====================================================================

This is one of the most important AWS networking concepts.


PUBLIC SUBNET:


       Resource
           |
           v
      Route Table
           |
           v
     Internet Gateway
           |
           v
        Internet


PRIVATE SUBNET:


       Resource
           |
           v
      Route Table
           |
           X
     No direct internet route


A common architecture:


                    INTERNET
                        |
                        v
                 Load Balancer
                        |
                        v
                Application
                        |
                        v
                    Database


The database is normally kept private.

Why?

Because the database should not be directly exposed to the
public internet.


IMPORTANT:

    Public/private design depends on network routing and
    resource configuration.

    Simply creating a subnet does not automatically make
    an application public.


====================================================================
14. ROUTE TABLE
====================================================================

A Route Table answers:

    "Where should network traffic go?"


Example:


    Destination       Target

    10.0.0.0/16       local
    0.0.0.0/0         Internet Gateway


Meaning:

    Traffic inside the VPC stays inside the VPC.

    Other IPv4 traffic can be sent toward the Internet Gateway,
    if the rest of the network configuration allows it.


Mental model:

    Route Table = traffic direction


====================================================================
15. INTERNET GATEWAY
====================================================================

Internet Gateway (IGW) provides a path between a VPC and
the internet for appropriately configured resources.


Basic idea:


       Public Resource
             |
             v
        Route Table
             |
             v
            IGW
             |
             v
         Internet


IMPORTANT:

    An Internet Gateway alone does not make a resource public.

Other configuration also matters:

    - Route table
    - Public IP/addressing
    - Security Group


====================================================================
16. NAT GATEWAY
====================================================================

NAT Gateway is commonly used when resources in a private subnet
need outbound internet access.


Example:


       Private Application
                |
                v
         Private Route Table
                |
                v
           NAT Gateway
                |
                v
       Internet Gateway
                |
                v
             Internet


Example:

    A private application needs to download something
    from the internet.


IMPORTANT COST WARNING:

    NAT Gateway can create AWS charges.

    Do NOT create one just for learning unless we specifically
    need it.

    We will only use it when the architecture requires it.


====================================================================
17. SECURITY GROUP
====================================================================

A Security Group is a virtual firewall for AWS resources.


Example:


       Application
            |
            | TCP 5432
            v
         Database


Database Security Group can allow:


    TCP 5432
    Source = Application Security Group


Meaning:

    Only the intended application network identity is allowed
    to connect to PostgreSQL on port 5432.


Security principle:

    Allow only what is required.


Avoid unnecessarily opening database ports to:

    0.0.0.0/0


Mental model:


    Route Table
        =
    Where does traffic go?


    Security Group
        =
    Is this traffic allowed?


====================================================================
18. IAM
====================================================================

IAM = Identity and Access Management.


IAM answers two basic questions:


    WHO are you?


    WHAT are you allowed to do?


Example:


          Developer
              |
              v
             IAM
              |
        +-----+-----+
        |           |
       Read        Write
       S3          S3


IAM includes concepts such as:


    Users
    Groups
    Policies
    Roles


For AWS workloads, IAM Roles are commonly preferred over
putting long-lived AWS access keys directly inside application code.


Example:


        EC2
         |
         v
      IAM Role
         |
         v
      S3 Access


Mental model:

    IAM = identity + permissions


====================================================================
19. LEAST PRIVILEGE
====================================================================

This is a major cloud security principle.


BAD:


    Application
         |
         v
    AdministratorAccess


If the application only needs to read files from S3,
giving it administrator access is unnecessary.


BETTER:


    Application
         |
         v
       IAM Role
         |
         v
    Only required S3 permission


Principle:

    Give only the permissions that are actually required.


This is called:

    Least Privilege


====================================================================
20. HOW THE PIECES CONNECT
====================================================================

Now combine everything.


                         AWS ACCOUNT
                              |
                              v
                           REGION
                              |
                              v
                             VPC
                              |
                +-------------+-------------+
                |                           |
          Public Subnet               Private Subnet
                |                           |
         Load Balancer                  Application
                                            |
                                  +---------+---------+
                                  |                   |
                                  v                   v
                                 RDS                  S3
                              Database             Storage


Security:


    Internet
       |
       v
    Load Balancer
       |
       v
    Application
       |
       v
    RDS


IAM:


    Application
         |
         v
      IAM Role
         |
         v
         S3


This is the basic mental model behind many cloud applications.


====================================================================
21. A SIMPLE REAL-WORLD ARCHITECTURE
====================================================================

Suppose a company has a web application.


Users
  |
  v
Internet
  |
  v
Load Balancer
  |
  v
Application
  |
  +-----------> RDS
  |
  +-----------> S3


Possible responsibilities:


    Load Balancer
        -> Receive/distribute traffic


    Application
        -> Run business logic


    RDS
        -> Store structured application data


    S3
        -> Store files/objects


    VPC
        -> Network isolation


    Security Groups
        -> Control network access


    IAM
        -> Control AWS permissions


    CloudWatch
        -> Monitoring


You will learn each of these separately.


====================================================================
22. CONSOLE VS CLI VS TERRAFORM
====================================================================

There are different ways to work with AWS.


AWS Console:

    Browser interface.

    Useful for:
        - Learning
        - Exploring
        - Checking resources
        - Debugging


AWS CLI:

    Terminal interface.

    Useful for:
        - Automation
        - Scripts
        - Troubleshooting
        - Fast operations


Terraform:

    Infrastructure as Code.

    Useful for:
        - Repeatable infrastructure
        - Version control
        - Team collaboration
        - Automation


Typical professional workflow:


    Understand
        |
        v
    Try manually / CLI
        |
        v
    Understand dependencies
        |
        v
    Terraform
        |
        v
    CI/CD automation


IMPORTANT:

    You do NOT need to memorize every AWS CLI command.

    You need to understand what you are trying to create.


====================================================================
23. AWS COST MINDSET
====================================================================

Every time you create an AWS resource, ask:


    "Does this cost money?"


Potentially billable services/resources include:

    EC2
    RDS
    NAT Gateway
    Load Balancer
    S3 storage
    Data transfer
    Some monitoring usage


For learning:


    Understand first.
    Create only what is required.
    Delete resources when finished.
    Check pricing before creating expensive resources.


IMPORTANT:

    We will NOT create expensive AWS resources just for practice.


====================================================================
24. AWS SECURITY MINDSET
====================================================================

Never think about security after building everything.


Think from the beginning:


    Who can access it?
          |
          v
        IAM


    Who can connect to it?
          |
          v
    Security Group


    Should it be public?
          |
          v
    Network design


    Where is sensitive data?
          |
          v
    Encryption / Secrets


Basic rule:


    Public only when necessary.

    Private by default where appropriate.

    Least privilege for permissions.


====================================================================
25. HOW TO APPROACH ANY AWS PROJECT
====================================================================

When someone gives you a new application,
do NOT immediately start creating resources.


Ask:


    1. What does the application do?


    2. Where will the application run?

           EC2?
           ECS?
           EKS?
           Lambda?


    3. What data does it need?


           RDS?
           DynamoDB?
           S3?


    4. Should resources be public or private?


    5. How will users reach the application?


           Load Balancer?
           API Gateway?
           etc.


    6. How will services communicate?


           VPC?
           Security Groups?
           Routes?


    7. What AWS permissions are required?


           IAM?


    8. How will we monitor it?


           CloudWatch?


    9. What happens if something fails?


           Backup?
           Multi-AZ?
           Recovery?


   10. What will it cost?


This way you design the architecture before creating resources.


====================================================================
26. WHAT YOU SHOULD REMEMBER
====================================================================

Remember these core ideas:


    AWS
        -> Cloud platform


    Account
        -> Main AWS boundary


    Region
        -> Geographical AWS location


    Availability Zone
        -> Isolated location inside a Region


    VPC
        -> Your AWS network


    Subnet
        -> Smaller network inside a VPC


    Route Table
        -> Decides where traffic goes


    Internet Gateway
        -> Internet connectivity path


    NAT Gateway
        -> Private resources' outbound internet access


    Security Group
        -> Network firewall


    IAM
        -> Identity and permissions


    EC2
        -> Virtual server


    S3
        -> Object/file storage


    RDS
        -> Managed relational database


====================================================================
27. THE MOST IMPORTANT DIAGRAM
====================================================================


                         AWS ACCOUNT
                              |
                           REGION
                              |
                         AVAILABILITY
                            ZONES
                              |
                             VPC
                              |
              +---------------+---------------+
              |                               |
        PUBLIC SUBNET                    PRIVATE SUBNET
              |                               |
        Load Balancer                    Application
                                              |
                                    +---------+---------+
                                    |                   |
                                    v                   v
                                   RDS                  S3
                                Database              Storage


              IAM
               |
               +---- Who can access AWS resources?


              ROUTE TABLE
               |
               +---- Where should traffic go?


              SECURITY GROUP
               |
               +---- Which network traffic is allowed?


              CLOUDWATCH
               |
               +---- What is happening in the system?


====================================================================
28. FINAL MENTAL MODEL
====================================================================

Do NOT memorize AWS as hundreds of unrelated services.


Think like this:


    APPLICATION
         |
         v
    WHERE DOES IT RUN?
         |
         +---- EC2 / ECS / EKS / Lambda
         |
         v
    WHERE IS DATA STORED?
         |
         +---- RDS / DynamoDB / S3
         |
         v
    HOW DOES IT COMMUNICATE?
         |
         +---- VPC / Subnet / Routes
         |
         v
    WHO CAN ACCESS IT?
         |
         +---- IAM / Security Groups
         |
         v
    HOW DO USERS REACH IT?
         |
         +---- Load Balancer / Internet
         |
         v
    HOW DO WE MONITOR IT?
         |
         +---- CloudWatch
         |
         v
    HOW DO WE AUTOMATE IT?
         |
         +---- Terraform / CI/CD


This is the foundation.

Once this mental model is clear,
learning individual AWS services becomes much easier.

'''