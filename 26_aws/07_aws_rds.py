'''
============================================================
AWS RDS — Relational Database Service
============================================================

RDS = Managed Relational Database

Instead of managing a database server yourself:

You manage:
    → Database configuration
    → Data
    → Queries
    → Application

AWS manages much of:
    → Server infrastructure
    → OS maintenance
    → Backups
    → Patching
    → Monitoring
    → Failover options


RDS ENGINES
-----------

Common engines:

    PostgreSQL
    MySQL
    MariaDB
    Oracle
    SQL Server


BASIC ARCHITECTURE
------------------

Application
     ↓
Security Group
     ↓
RDS PostgreSQL
     ↓
Database


RDS + VPC
---------

RDS normally runs inside a VPC.

VPC
└── Private Subnet A
└── Private Subnet B
        ↓
    RDS


DB SUBNET GROUP
---------------

A DB subnet group tells RDS which subnets
it can use.

Typically:

Private Subnet A
        +
Private Subnet B
        ↓
DB Subnet Group
        ↓
RDS


SECURITY
--------

Application
    ↓
Application Security Group
    ↓
RDS Security Group
    ↓
Port 5432
    ↓
PostgreSQL


Do NOT normally allow:

0.0.0.0/0 → 5432


DATABASE vs S3
--------------

RDS
→ Structured data

S3
→ Files / objects


Example:

MLflow metadata
    → PostgreSQL / RDS

ML model files
    → S3


IMPORTANT COMMANDS
------------------

List RDS databases:

aws rds describe-db-instances


Get details of a specific database:

aws rds describe-db-instances \
    --db-instance-identifier DB_IDENTIFIER


Check DB subnet groups:

aws rds describe-db-subnet-groups


Check RDS security groups:

aws ec2 describe-security-groups


COST SAFETY
-----------

RDS is BILLABLE.

Important:

❌ Don't create RDS just for practice
❌ Don't leave unnecessary databases running
❌ Don't choose Multi-AZ unnecessarily for learning
❌ Don't create production-sized instances for testing


PRODUCTION THINKING
-------------------

Application
    ↓
Private Network
    ↓
RDS
    ↓
Backups + Monitoring
    ↓
High Availability when required


REMEMBER
--------

RDS       = Managed relational database
Engine    = PostgreSQL / MySQL / etc.
Subnet    = Network location
DB Subnet Group = Allowed subnets
SG        = Database firewall
Port 5432  = PostgreSQL

============================================================
'''