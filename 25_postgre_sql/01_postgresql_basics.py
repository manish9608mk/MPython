'''
============================================================
                POSTGRESQL — BASICS
============================================================

WHAT IS POSTGRESQL?
-------------------
PostgreSQL is an open-source Relational Database Management
System (RDBMS).

Its job is to store, organize, retrieve, and manage data
for applications.

Think of PostgreSQL as a highly organized data manager.

For example, an application may need to store:

    Users
    Products
    Orders
    Payments

PostgreSQL stores this information reliably and allows the
application to work with it.

------------------------------------------------------------

WHAT IS SQL?
------------
SQL = Structured Query Language.

SQL is the language we use to communicate with a relational
database.

Example:

    SELECT * FROM users;

This asks the database:

    "Give me all records from the users table."

Important:

    SQL         → Language
    PostgreSQL  → Database Management System

They are NOT the same thing.

------------------------------------------------------------

WHAT DOES "RELATIONAL" MEAN?
----------------------------
Relational databases organize data into tables and allow
tables to have relationships with each other.

Example:

    users
    ----------------
    id | name
    ----------------
    1  | Manish
    2  | Rahul


    orders
    -------------------------
    id | user_id | product
    -------------------------
    1  | 1       | Laptop
    2  | 2       | Phone

Here `user_id` connects an order to a user.

This relationship is one of the most important ideas in
relational databases.

------------------------------------------------------------

DATABASE HIERARCHY
------------------

    PostgreSQL Server
          ↓
       Database
          ↓
        Schema
          ↓
        Table
          ↓
    Rows + Columns


Think about a company:

    Company
       ↓
    Departments
       ↓
    Tables
       ↓
    Records

------------------------------------------------------------

TABLE
-----
A table stores data in rows and columns.

Example:

    users

    id | name   | age
    -----------------
    1  | Manish | 23
    2  | Rahul  | 24

Column:
    Describes what type of information is stored.

Row:
    Represents one actual record.

------------------------------------------------------------

WHY DO WE NEED POSTGRESQL?
--------------------------
Imagine an application has 10 users.

We could store their information in a file.

But imagine:

    10,000 users
    1,000,000 users
    thousands of orders
    millions of messages

Now we need a proper system to:

    - store data
    - search data
    - update data
    - delete data
    - maintain relationships
    - protect data
    - handle multiple users
    - maintain consistency

A database system solves these problems.

------------------------------------------------------------

REAL-WORLD EXAMPLES
-------------------

E-commerce:
    users
    products
    orders
    payments

Banking:
    customers
    accounts
    transactions

Social Media:
    users
    posts
    comments
    likes

Company/SaaS:
    users
    organizations
    subscriptions
    invoices

AI Application:
    users
    conversations
    messages
    model information

The database design changes according to the problem,
but the fundamental PostgreSQL concepts remain the same.

------------------------------------------------------------

MENTAL MODEL
------------

Application
     ↓
   SQL
     ↓
PostgreSQL
     ↓
 Database
     ↓
  Tables
     ↓
Rows + Columns

Remember:

    SQL = language
    PostgreSQL = database system
    Table = organized collection of records
    Row = one record
    Column = one attribute/field

------------------------------------------------------------

IMPORTANT POINTS
----------------
1. PostgreSQL is an RDBMS.
2. PostgreSQL stores and manages structured data.
3. SQL is used to communicate with PostgreSQL.
4. Relational databases use tables.
5. Tables contain rows and columns.
6. Tables can be connected through relationships.
7. PostgreSQL is commonly used for production systems.

------------------------------------------------------------

COMMON MISTAKES
---------------

❌ PostgreSQL = SQL

Correct:

    SQL → language
    PostgreSQL → database system

❌ Row = Column

Correct:

    Row    → one record
    Column → one attribute/field

❌ Database = Table

Correct:

    Database → can contain multiple tables.

============================================================
                    BASIC COMMANDS
============================================================

These commands are executed inside the PostgreSQL `psql`
terminal, NOT directly as Python code.

------------------------------------------------------------

CHECK POSTGRESQL VERSION
------------------------------------------------------------

    psql --version

Example:

    psql (PostgreSQL) 16.x


------------------------------------------------------------

CONNECT TO POSTGRESQL
------------------------------------------------------------

    psql -U postgres

`-U` means "user".

Here we are connecting as the PostgreSQL user:

    postgres


------------------------------------------------------------

CONNECT TO A SPECIFIC DATABASE
------------------------------------------------------------

    psql -U postgres -d database_name


------------------------------------------------------------

LIST DATABASES
------------------------------------------------------------

    \l


------------------------------------------------------------

SHOW CURRENT DATABASE
------------------------------------------------------------

    SELECT current_database();


------------------------------------------------------------

SHOW POSTGRESQL VERSION
------------------------------------------------------------

    SELECT version();


------------------------------------------------------------

LIST TABLES
------------------------------------------------------------

    \dt


------------------------------------------------------------

EXIT psql
------------------------------------------------------------

    \q

============================================================
'''













'''
============================================================
              RUNNING POSTGRESQL WITH DOCKER
============================================================

Mental Model:

Mac
 ↓
Docker
 ↓
PostgreSQL Container
 ↓
PostgreSQL Server
 ↓
Database
 ↓
Tables
 ↓
Rows

We don't need PostgreSQL installed directly on the Mac.

Docker can run PostgreSQL inside a container.

------------------------------------------------------------

IMPORTANT COMMANDS
------------------------------------------------------------

Check Docker:

    docker --version

See running containers:

    docker ps

Start PostgreSQL:

    docker run -d \
      --name postgres-learning \
      -e POSTGRES_USER=admin \
      -e POSTGRES_PASSWORD=admin123 \
      -e POSTGRES_DB=learning_db \
      -p 5432:5432 \
      postgres:17

Connect to PostgreSQL:

    docker exec -it postgres-learning \
    psql -U admin -d learning_db

Inside psql:

    SELECT version();

    SELECT current_database();

    \dt

Exit:

    \q

------------------------------------------------------------

REAL-WORLD CONNECTION
------------------------------------------------------------

In a real application:

    FastAPI
       ↓
    PostgreSQL

During development:

    FastAPI
       ↓
    PostgreSQL Docker Container

In production:

    FastAPI
       ↓
    AWS RDS PostgreSQL

The PostgreSQL concepts remain the same.

Only the environment changes.

============================================================
'''