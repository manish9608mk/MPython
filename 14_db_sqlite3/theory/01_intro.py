'''
SQLite3 in Python
==================

SQLite is a lightweight relational database.

Python provides the built-in sqlite3 module
to work with SQLite databases.

# Import SQLite module
import sqlite3


Basic Database Flow
===================

connect()
    ↓
cursor()
    ↓
execute()
    ↓
commit()
    ↓
close()


SQLite stores data in a database file,
for example:

youtube.db


Important SQL Operations
========================

CREATE TABLE → Create a table
INSERT       → Add data
SELECT       → Read data
UPDATE       → Modify data
DELETE       → Remove data


CRUD
====

C → Create → INSERT
R → Read   → SELECT
U → Update → UPDATE
D → Delete → DELETE
'''








# ============================================================
# DETAILED NOTES
# ============================================================

'''
1. WHAT IS SQLITE?
==================

SQLite is a lightweight relational database.

It stores application data permanently
inside a database file.

Example:

youtube.db


Why SQLite?
-----------

- No separate database server is required.
- Database is stored in a single file.
- Built into Python through the sqlite3 module.
- Easy to learn and use.
- Useful for small applications, testing and prototypes.


Architecture:

Python Application
        |
        | sqlite3
        ↓
    SQLite Database
        |
        ↓
    youtube.db


2. sqlite3 MODULE
=================

sqlite3 is Python's built-in module
for working with SQLite databases.

No installation is normally required.

Example:

import sqlite3


3. DATABASE CONNECTION
======================

A connection connects Python
to the SQLite database.

Example:

connection = sqlite3.connect("youtube.db")

If youtube.db does not exist,
SQLite can create it.


4. CURSOR
=========

A cursor is used to execute SQL queries
on the database.

Example:

cursor = connection.cursor()


5. SQL QUERY
============

SQL (Structured Query Language) is used
to work with data inside the database.

Examples:

CREATE TABLE
INSERT
SELECT
UPDATE
DELETE


6. TABLE
========

A table stores data in rows and columns.

Example:

videos table

+----+------------------+----------+
| id | name             | time     |
+----+------------------+----------+
| 1  | Python Tutorial  | 10 min   |
| 2  | Docker Basics    | 15 min   |
+----+------------------+----------+


7. ROW
======

A row represents one complete record.

Example:

1 | Python Tutorial | 10 min

This is one video record.


8. COLUMN
=========

A column represents one attribute of the data.

Example:

id
name
time


9. PRIMARY KEY
==============

A primary key uniquely identifies each row.

Example:

id INTEGER PRIMARY KEY

So:

id = 1
id = 2
id = 3

Each ID identifies one video.


10. BASIC DATABASE FLOW
=======================

Connect
   ↓
Create Cursor
   ↓
Execute SQL Query
   ↓
Commit Changes
   ↓
Close Connection


11. CREATE TABLE
================

Creates a table if it does not already exist.

Example:

CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT,
    time TEXT
)


12. INSERT
==========

Adds new data to the table.

Example:

INSERT INTO videos (name, time)
VALUES ('Python Tutorial', '10 min')


13. SELECT
==========

Reads data from the table.

Example:

SELECT * FROM videos


14. UPDATE
==========

Modifies existing data.

Example:

UPDATE videos
SET name = 'Python Advanced'
WHERE id = 1


15. DELETE
==========

Removes data from the table.

Example:

DELETE FROM videos
WHERE id = 1


16. IMPORTANT PYTHON METHODS
============================

sqlite3.connect()
→ Connects to the database.

connection.cursor()
→ Creates a cursor.

cursor.execute()
→ Executes an SQL query.

connection.commit()
→ Saves database changes.

cursor.fetchone()
→ Gets one row.

cursor.fetchall()
→ Gets all rows.

connection.close()
→ Closes the database connection.


17. COMMIT
==========

INSERT, UPDATE and DELETE change
the database.

Use:

connection.commit()

to save those changes permanently.


18. PARAMETERIZED QUERIES
=========================

When using user input,
use parameterized queries.

Example:

cursor.execute(
    "INSERT INTO videos (name, time) VALUES (?, ?)",
    (name, time)
)

The ? placeholders safely receive
the values.

This is safer than directly building
SQL queries using user input.


19. JSON vs SQLITE
==================

JSON:

Python
  ↓
JSON file
  ↓
Data

Good for simple file-based storage.


SQLite:

Python
  ↓
sqlite3
  ↓
SQLite database
  ↓
Tables
  ↓
Rows + Columns

Better when the application needs
structured relational data and SQL queries.


20. OUR YOUTUBE MANAGER
======================

Before:

Python
   ↓
JSON
   ↓
youtube.txt


After:

Python
   ↓
sqlite3
   ↓
youtube.db
   ↓
videos table


Project CRUD:

add_video()
    ↓
INSERT

list_all_videos()
    ↓
SELECT

update_video()
    ↓
UPDATE

delete_video()
    ↓
DELETE


21. BASIC SQLITE3 EXAMPLE
=========================

import sqlite3

connection = sqlite3.connect("youtube.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT,
        time TEXT
    )
""")

connection.commit()

connection.close()


22. IMPORTANT REAL-WORLD IDEA
=============================

The same basic database concepts
are used in larger applications.

For example:

Frontend
   ↓
API
   ↓
Python Backend
   ↓
Service Layer
   ↓
Database
   ↓
Persistent Data


SQLite is excellent for learning
these database concepts.

Larger production applications may use:

- PostgreSQL
- MySQL
- Microsoft SQL Server
- Oracle Database


23. WHAT THIS PROJECT WILL TEACH
================================

Python
   ↓
Functions
   ↓
Error Handling
   ↓
File Handling
   ↓
JSON
   ↓
SQLite
   ↓
SQL
   ↓
CRUD
   ↓
Database-backed Application


24. IMPORTANT TERMS TO REMEMBER
================================

Database
→ Stores application data.

Table
→ Stores related data.

Row
→ One record.

Column
→ One attribute.

Primary Key
→ Unique identifier.

Connection
→ Link between Python and database.

Cursor
→ Executes SQL queries.

Query
→ SQL command.

Commit
→ Saves database changes.

CRUD
→ Create, Read, Update, Delete.





EXAMPLE DEMO:

import sqlite3

# Connect to the database
connection = sqlite3.connect("youtube.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT,
        time TEXT
    )
""")

# Insert video
cursor.execute(
    "INSERT INTO videos (name, time) VALUES (?, ?)",
    ("Artificial Intelligence Intro", "10 min")
)

# Save changes
connection.commit()

# Read all videos
cursor.execute("SELECT * FROM videos")

videos = cursor.fetchall()

print(videos)

# Close connection
connection.close()
'''