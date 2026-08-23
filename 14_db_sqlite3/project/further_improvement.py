'''
============================================================
        YOUTUBE VIDEO MANAGER — PROJECT ROADMAP
============================================================

CURRENT PROJECT:
    Python + SQLite3 CRUD Application

GOAL:
    Convert this basic CRUD application into a
    resume-worthy production-style backend project.

------------------------------------------------------------
PHASE 1 — CURRENT CRUD FOUNDATION
------------------------------------------------------------

[✓] SQLite database connection
[✓] Cursor creation
[✓] Create table
[✓] INSERT video
[✓] SELECT videos
[✓] UPDATE video
[✓] DELETE video
[✓] commit()
[✓] Input validation
[✓] ValueError handling
[✓] sqlite3.Error handling
[✓] Parameterized SQL queries
[✓] Empty database handling
[✓] User-friendly table display

------------------------------------------------------------
PHASE 2 — IMPROVE CURRENT CRUD
------------------------------------------------------------

[ ] Add database error handling to EVERY database operation
    - list_videos()
    - add_videos()
    - update_video()
    - delete_video()

[ ] Use conn.rollback() when database operation fails

[ ] Validate video ID
    - Must be integer
    - Must be greater than 0

[ ] Validate video name
    - Cannot be empty
    - Cannot contain only spaces
    - Add maximum length

[ ] Validate video time
    - Cannot be empty
    - Validate proper format

[ ] Add confirmation before deleting a video

[ ] Show existing video details before UPDATE

[ ] Display success/error messages consistently

[ ] Prevent duplicate videos if required

[ ] Add database constraints where appropriate

------------------------------------------------------------
PHASE 3 — ADD MORE SQL FEATURES
------------------------------------------------------------

[ ] Search videos by name

    SQL concepts:
        WHERE
        LIKE

[ ] Search videos by category

[ ] Search videos by ID

[ ] Sort videos

    SQL concepts:
        ORDER BY
        ASC
        DESC

[ ] Filter videos

    SQL concepts:
        WHERE
        AND
        OR

[ ] Limit results

    SQL concept:
        LIMIT

[ ] Add pagination

    Example:
        Page 1 → videos 1-10
        Page 2 → videos 11-20

------------------------------------------------------------
PHASE 4 — IMPROVE DATABASE DESIGN
------------------------------------------------------------

Current table:

    videos
    ----------------
    id
    name
    time

Improve database schema:

    videos
    --------------------------------
    id
    name
    time
    category
    description
    url
    created_at
    updated_at
    views
    likes
    status

[ ] Add category

    Example:
        Python
        AWS
        Docker
        Kubernetes
        DSA
        Linux

[ ] Add description

[ ] Add YouTube URL

[ ] Add created_at timestamp

[ ] Add updated_at timestamp

[ ] Add views

[ ] Add likes

[ ] Add status

    Example:
        active
        archived

------------------------------------------------------------
PHASE 5 — DATABASE RELATIONSHIPS
------------------------------------------------------------

Create additional tables.

    videos
       |
       | category_id
       ↓
    categories

Possible schema:

    categories
    ----------------
    id
    name

    videos
    ----------------
    id
    name
    time
    category_id
    description
    url
    created_at
    updated_at

Learn:

[ ] Primary Key
[ ] Foreign Key
[ ] One-to-Many relationship
[ ] JOIN
[ ] INNER JOIN
[ ] LEFT JOIN
[ ] Foreign key constraints

------------------------------------------------------------
PHASE 6 — DATABASE PERFORMANCE
------------------------------------------------------------

[ ] Learn database indexes

[ ] Create indexes for frequently searched columns

    Example:
        name
        category_id
        created_at

[ ] Understand:

    Index
    Query performance
    Full table scan
    Query optimization

[ ] Learn EXPLAIN QUERY PLAN

[ ] Optimize slow queries

------------------------------------------------------------
PHASE 7 — TRANSACTIONS
------------------------------------------------------------

[ ] Understand transactions

[ ] commit()

[ ] rollback()

[ ] Atomic operations

[ ] Handle failed transactions safely

[ ] Understand:

    BEGIN
    COMMIT
    ROLLBACK

[ ] Learn ACID properties

    Atomicity
    Consistency
    Isolation
    Durability

------------------------------------------------------------
PHASE 8 — CLEAN PROJECT STRUCTURE
------------------------------------------------------------

Instead of keeping everything in one file:

    youtube_manager/
    |
    ├── main.py
    ├── database.py
    ├── models.py
    ├── crud.py
    ├── validators.py
    ├── config.py
    ├── utils.py
    |
    ├── tests/
    │   ├── test_crud.py
    │   ├── test_database.py
    │   └── test_validators.py
    |
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    └── .env

Learn:

[ ] Modules
[ ] Packages
[ ] Separation of concerns
[ ] Clean code
[ ] DRY principle

------------------------------------------------------------
PHASE 9 — REMOVE GLOBAL DATABASE STATE
------------------------------------------------------------

Current:

    global conn
    global cursor

Improve:

[ ] Create database connection through a function

[ ] Pass connection/database dependency where required

[ ] Avoid unnecessary global variables

[ ] Learn context managers

    with sqlite3.connect(...) as conn:

------------------------------------------------------------
PHASE 10 — OBJECT ORIENTED DESIGN
------------------------------------------------------------

Create classes such as:

    Database
    Video
    VideoRepository
    VideoService

Possible architecture:

    User
      ↓
    Service Layer
      ↓
    Repository Layer
      ↓
    Database

Learn:

[ ] Classes
[ ] Encapsulation
[ ] Abstraction
[ ] Composition
[ ] Repository pattern
[ ] Service layer

------------------------------------------------------------
PHASE 11 — LOGGING
------------------------------------------------------------

Replace excessive print-based debugging with:

    Python logging

[ ] logging
[ ] Log levels

    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

[ ] Application log file

    logs/app.log

[ ] Log database errors

[ ] Log important application events

------------------------------------------------------------
PHASE 12 — TESTING
------------------------------------------------------------

Add automated tests.

Use:

    pytest

Test:

[ ] Add video
[ ] List videos
[ ] Update video
[ ] Delete video
[ ] Search video
[ ] Invalid video ID
[ ] Empty video name
[ ] Empty time
[ ] Non-existing video
[ ] Database errors
[ ] Transaction rollback

Target:

    High test coverage

------------------------------------------------------------
PHASE 13 — REST API
------------------------------------------------------------

Convert the CLI application into a backend API.

Use:

    FastAPI

Architecture:

    Client
       ↓
    REST API
       ↓
    Service Layer
       ↓
    Repository Layer
       ↓
    Database

Create endpoints:

    GET    /videos
    GET    /videos/{id}

    POST   /videos

    PUT    /videos/{id}

    DELETE /videos/{id}

    GET    /videos/search

------------------------------------------------------------
PHASE 14 — API FEATURES
------------------------------------------------------------

[ ] Request validation

[ ] Response validation

[ ] HTTP status codes

    200 OK
    201 Created
    400 Bad Request
    404 Not Found
    500 Internal Server Error

[ ] API error handling

[ ] Pagination

[ ] Filtering

[ ] Searching

[ ] Sorting

[ ] API documentation

    Swagger
    OpenAPI

------------------------------------------------------------
PHASE 15 — AUTHENTICATION & AUTHORIZATION
------------------------------------------------------------

Add users.

Create:

    users
    ----------------
    id
    username
    email
    password_hash
    created_at

[ ] User registration

[ ] Login

[ ] Password hashing

[ ] Authentication

[ ] Authorization

[ ] JWT authentication

[ ] Protected endpoints

Example:

    POST /auth/register
    POST /auth/login

    GET /videos
    POST /videos
    PUT /videos/{id}
    DELETE /videos/{id}

------------------------------------------------------------
PHASE 16 — DATABASE UPGRADE
------------------------------------------------------------

Move from:

    SQLite

to:

    PostgreSQL

Learn:

[ ] PostgreSQL
[ ] Database server
[ ] Users
[ ] Roles
[ ] Permissions
[ ] Connections
[ ] Transactions
[ ] Indexes
[ ] Foreign keys

Application architecture:

    FastAPI
       ↓
    PostgreSQL

------------------------------------------------------------
PHASE 17 — ORM
------------------------------------------------------------

Learn an ORM.

Possible:

    SQLAlchemy

Use ORM models:

    User
    Video
    Category

Learn:

[ ] Models
[ ] Relationships
[ ] Queries
[ ] Transactions
[ ] Migrations

------------------------------------------------------------
PHASE 18 — DATABASE MIGRATIONS
------------------------------------------------------------

Use:

    Alembic

Learn:

[ ] Database migrations

[ ] Schema versioning

[ ] Upgrade database

[ ] Downgrade database

Example:

    Migration 001
        ↓
    Migration 002
        ↓
    Migration 003

------------------------------------------------------------
PHASE 19 — DOCKER
------------------------------------------------------------

Containerize application.

Create:

    Dockerfile

[ ] Python application container

[ ] PostgreSQL container

[ ] Environment variables

[ ] Docker volumes

[ ] Docker networks

[ ] Health checks

------------------------------------------------------------
PHASE 20 — DOCKER COMPOSE
------------------------------------------------------------

Create:

    docker-compose.yml

Architecture:

    ┌───────────────┐
    │   FastAPI     │
    │   Container   │
    └───────┬───────┘
            │
            ↓
    ┌───────────────┐
    │  PostgreSQL   │
    │   Container   │
    └───────────────┘

------------------------------------------------------------
PHASE 21 — ENVIRONMENT CONFIGURATION
------------------------------------------------------------

Never hard-code sensitive configuration.

Use:

    .env

Example configuration:

    DATABASE_URL
    SECRET_KEY
    JWT_SECRET
    DEBUG

[ ] python-dotenv

[ ] Environment variables

[ ] Secret management

[ ] Separate:

    Development
    Testing
    Production

------------------------------------------------------------
PHASE 22 — SECURITY
------------------------------------------------------------

[ ] SQL injection prevention

    Use parameterized queries / ORM

[ ] Password hashing

[ ] JWT security

[ ] Input validation

[ ] Secure HTTP headers

[ ] CORS configuration

[ ] Rate limiting

[ ] Secret management

[ ] Don't expose database credentials

[ ] Don't commit .env

------------------------------------------------------------
PHASE 23 — GIT & GITHUB
------------------------------------------------------------

[ ] Initialize Git repository

[ ] Meaningful commits

[ ] Feature branches

[ ] Pull requests

[ ] GitHub repository

[ ] Proper .gitignore

[ ] README.md

[ ] GitHub Issues

[ ] GitHub Projects

------------------------------------------------------------
PHASE 24 — CI/CD
------------------------------------------------------------

Use:

    GitHub Actions

Pipeline:

    Git Push
       ↓
    GitHub Actions
       ↓
    Run Tests
       ↓
    Lint
       ↓
    Build Docker Image
       ↓
    Push Image
       ↓
    Deploy

Learn:

[ ] CI
[ ] CD
[ ] Automated testing
[ ] Build pipeline
[ ] Deployment pipeline

------------------------------------------------------------
PHASE 25 — CODE QUALITY
------------------------------------------------------------

Add:

[ ] Type hints

[ ] Docstrings

[ ] PEP 8

[ ] Ruff / Flake8

[ ] Black

[ ] MyPy

[ ] Pre-commit hooks

Goal:

    Clean
    Readable
    Maintainable
    Production-quality code

------------------------------------------------------------
PHASE 26 — MONITORING
------------------------------------------------------------

Add application monitoring.

Learn:

[ ] Prometheus

[ ] Grafana

[ ] Metrics

Track:

    Request count
    Request latency
    Error rate
    Database performance
    CPU
    Memory

Example:

    API Requests
         ↓
    Prometheus
         ↓
    Grafana Dashboard

------------------------------------------------------------
PHASE 27 — OBSERVABILITY
------------------------------------------------------------

Implement:

[ ] Structured logging

[ ] Metrics

[ ] Health checks

[ ] Readiness check

[ ] Liveness check

Example:

    GET /health
    GET /ready

Learn:

    Logs
    Metrics
    Traces

------------------------------------------------------------
PHASE 28 — CLOUD DEPLOYMENT
------------------------------------------------------------

Deploy to AWS.

Possible architecture:

                 Internet
                     │
                     ↓
              Load Balancer
                     │
                     ↓
              FastAPI Application
                     │
                     ↓
                PostgreSQL
                     │
                     ↓
                  AWS RDS

Possible AWS services:

[ ] EC2 / ECS
[ ] RDS
[ ] S3
[ ] CloudWatch
[ ] IAM
[ ] VPC
[ ] Load Balancer
[ ] ECR

------------------------------------------------------------
PHASE 29 — INFRASTRUCTURE AS CODE
------------------------------------------------------------

Use:

    Terraform

Create infrastructure using code.

[ ] VPC

[ ] Subnets

[ ] Security groups

[ ] EC2/ECS

[ ] RDS

[ ] IAM

[ ] Load Balancer

Learn:

    Infrastructure as Code
    Terraform state
    Modules
    Variables
    Outputs

------------------------------------------------------------
PHASE 30 — KUBERNETES
------------------------------------------------------------

Advanced version:

    Client
      ↓
    Load Balancer
      ↓
    Kubernetes
      ↓
    FastAPI Pods
      ↓
    PostgreSQL

Learn:

[ ] Pods
[ ] Deployments
[ ] Services
[ ] ConfigMaps
[ ] Secrets
[ ] Ingress
[ ] Health checks
[ ] Horizontal scaling

------------------------------------------------------------
PHASE 31 — CACHING
------------------------------------------------------------

Add Redis.

Architecture:

    Client
      ↓
    FastAPI
      ↓
    Redis
      ↓
    PostgreSQL

Use caching for:

[ ] Frequently requested videos

Learn:

[ ] Cache
[ ] Cache hit
[ ] Cache miss
[ ] TTL
[ ] Cache invalidation

------------------------------------------------------------
PHASE 32 — ASYNCHRONOUS PROCESSING
------------------------------------------------------------

For heavy/background tasks:

[ ] Background jobs

[ ] Task queues

Possible technologies:

    Celery
    Redis

Example:

    Upload video
        ↓
    Queue task
        ↓
    Background worker
        ↓
    Process task

------------------------------------------------------------
PHASE 33 — FILE STORAGE
------------------------------------------------------------

Instead of storing large files in database:

    Application
        ↓
       S3
        ↓
    File/Object Storage

Use database only for metadata.

Learn:

[ ] AWS S3
[ ] Object storage
[ ] Presigned URLs

------------------------------------------------------------
PHASE 34 — ADVANCED FEATURES
------------------------------------------------------------

[ ] Favorites

[ ] Watch history

[ ] User playlists

[ ] Categories

[ ] Tags

[ ] Video ratings

[ ] Likes

[ ] Comments

[ ] Recently watched

[ ] Recommended videos

[ ] User dashboard

[ ] Admin dashboard

------------------------------------------------------------
PHASE 35 — SEARCH ENGINE
------------------------------------------------------------

For advanced search:

    PostgreSQL Full Text Search

or later:

    Elasticsearch / OpenSearch

Features:

[ ] Full-text search

[ ] Ranking

[ ] Filters

[ ] Autocomplete

------------------------------------------------------------
PHASE 36 — PERFORMANCE & SCALABILITY
------------------------------------------------------------

[ ] Database indexing

[ ] Query optimization

[ ] Connection pooling

[ ] Caching

[ ] Pagination

[ ] Load testing

[ ] Horizontal scaling

[ ] Stateless application design

Learn:

    Scalability
    Availability
    Reliability
    Performance

------------------------------------------------------------
PHASE 37 — LOAD TESTING
------------------------------------------------------------

Test API performance.

Possible tools:

    Locust
    k6

Measure:

    Requests/second
    Latency
    Error rate
    Concurrent users

------------------------------------------------------------
PHASE 38 — BACKUP & RECOVERY
------------------------------------------------------------

[ ] Database backup

[ ] Automated backups

[ ] Restore procedure

[ ] Disaster recovery

[ ] Point-in-time recovery

Learn:

    Backup
    Recovery
    RPO
    RTO

------------------------------------------------------------
PHASE 39 — PRODUCTION DEPLOYMENT
------------------------------------------------------------

Final architecture:

                         USERS
                           │
                           ↓
                    Load Balancer
                           │
                           ↓
                    FastAPI Backend
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
            Redis       PostgreSQL      S3
              │            │
              └──────┬─────┘
                     ↓
                 AWS Cloud

Monitoring:

    Prometheus
         ↓
      Grafana

CI/CD:

    GitHub
       ↓
    GitHub Actions
       ↓
    Docker
       ↓
    AWS

------------------------------------------------------------
PHASE 40 — DOCUMENTATION
------------------------------------------------------------

Create professional README.md.

Include:

[ ] Project overview

[ ] Features

[ ] Architecture diagram

[ ] Technology stack

[ ] Database schema

[ ] API documentation

[ ] Installation instructions

[ ] Environment variables

[ ] Running locally

[ ] Docker setup

[ ] Testing

[ ] Deployment

[ ] Screenshots

[ ] Performance results

[ ] Future improvements

------------------------------------------------------------
PHASE 41 — RESUME-WORTHY PROJECT REQUIREMENTS
------------------------------------------------------------

Before putting this project on resume, aim for:

[ ] Python

[ ] SQL

[ ] PostgreSQL

[ ] FastAPI

[ ] SQLAlchemy

[ ] REST API

[ ] Authentication

[ ] Docker

[ ] Git/GitHub

[ ] GitHub Actions

[ ] AWS

[ ] Testing

[ ] Logging

[ ] Monitoring

[ ] CI/CD

[ ] Clean Architecture

[ ] Documentation

------------------------------------------------------------
FINAL PROJECT
------------------------------------------------------------

PROJECT NAME:

    YouTube Video Management Platform

TECH STACK:

    Python
    FastAPI
    PostgreSQL
    SQLAlchemy
    Redis
    Docker
    GitHub Actions
    AWS
    Terraform
    Prometheus
    Grafana

CORE FEATURES:

    User Authentication
    Video CRUD
    Search
    Filtering
    Sorting
    Pagination
    Categories
    Tags
    Playlists
    Likes
    Comments
    Watch History
    Admin Controls

BACKEND:

    REST API
    Authentication
    Authorization
    Validation
    Error Handling
    Logging
    Testing

DATABASE:

    PostgreSQL
    Indexing
    Transactions
    Relationships
    Migrations

DEVOPS:

    Docker
    CI/CD
    AWS
    Terraform
    Monitoring
    Logging

------------------------------------------------------------
RESUME IMPACT
------------------------------------------------------------

The final project should demonstrate:

    Python Backend Development
          +
    Database Engineering
          +
    REST API Development
          +
    System Design
          +
    Testing
          +
    Docker
          +
    CI/CD
          +
    AWS
          +
    Infrastructure as Code
          +
    Monitoring

DO NOT ADD FEATURES JUST FOR THE SAKE OF ADDING FEATURES.

Every feature should teach a real engineering concept.

Build progressively:

    SQLite CRUD
         ↓
    Clean Python Application
         ↓
    FastAPI Backend
         ↓
    PostgreSQL
         ↓
    Authentication
         ↓
    Docker
         ↓
    Testing
         ↓
    CI/CD
         ↓
    AWS
         ↓
    Terraform
         ↓
    Monitoring
         ↓
    Production Deployment

============================================================
'''