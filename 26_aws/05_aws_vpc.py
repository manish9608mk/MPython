'''
============================================================
AWS VPC — Virtual Private Cloud
============================================================

VPC = Your private network inside AWS.

Think:

AWS
 ↓
VPC
 ↓
Subnets
 ↓
Resources


VPC
---

A VPC provides the network environment for:

    EC2
    ECS
    RDS
    Load Balancers
    etc.


CIDR
----

CIDR defines the IP address range of the VPC.

Example:

172.31.0.0/16


SUBNET
------

A subnet is a smaller network inside a VPC.

VPC
└── Subnet A
└── Subnet B
└── Subnet C


PUBLIC vs PRIVATE SUBNET
------------------------

Public subnet:

Subnet
  ↓
Route Table
  ↓
Internet Gateway
  ↓
Internet


Private subnet:

Subnet
  ↓
Private Route Table
  ↓
No direct Internet Gateway route


IMPORTANT:

A subnet is considered public/private mainly
because of its routing.


ROUTE TABLE
-----------

Controls where network traffic goes.

Example:

Destination       Target

172.31.0.0/16     local
0.0.0.0/0         Internet Gateway


INTERNET GATEWAY
----------------

IGW = Internet Gateway

Connects a VPC to the Internet.

Public resources can use:

VPC
 ↓
Route Table
 ↓
IGW
 ↓
Internet


SECURITY GROUP
--------------

Security Group = Virtual firewall.

Controls traffic to/from resources.

Example:

Internet
   ↓
Security Group
   ↓
Application


Common ports:

22    → SSH
80    → HTTP
443   → HTTPS
5432  → PostgreSQL


IMPORTANT COMMANDS
------------------

List VPCs:

aws ec2 describe-vpcs


List subnets:

aws ec2 describe-subnets


List route tables:

aws ec2 describe-route-tables


List Internet Gateways:

aws ec2 describe-internet-gateways


List security groups:

aws ec2 describe-security-groups


Check a specific VPC:

aws ec2 describe-vpcs \
    --vpc-ids VPC_ID


BASIC ARCHITECTURE
------------------

                 Internet
                    ↓
              Internet Gateway
                    ↓
                  VPC
              ┌─────┴─────┐
              ↓           ↓
        Public Subnet  Private Subnet
              ↓           ↓
             ALB         RDS
              ↓
          Application


PRODUCTION THINKING
-------------------

Internet-facing resources
    → Public subnet when required

Databases
    → Private subnet

Security
    → Security Groups

Routing
    → Route Tables


REMEMBER
--------

VPC       = Network
Subnet    = Smaller network
Route     = Traffic direction
IGW       = Internet connection
SG        = Firewall

============================================================
'''