"""

 MONGODB:

MongoDB is a NoSQL, document-oriented database.

Unlike relational databases such as MySQL/PostgreSQL,
MongoDB stores data as documents instead of rows and tables.

------------------------------------------------------------
1. WHAT IS MONGODB?
------------------------------------------------------------

MongoDB is a NoSQL database designed to store data in
flexible, JSON-like documents.

Example document:

{
    "_id": ObjectId("..."),
    "name": "Tum Hi Ho",
    "time": "5 min"
}

MongoDB internally stores documents in BSON
(Binary JSON) format.

------------------------------------------------------------
2. SQL DATABASE vs MONGODB
------------------------------------------------------------

SQL Database:

Database
    |
    +-- Table
          |
          +-- Row
          +-- Row
          +-- Row

MongoDB:

Database
    |
    +-- Collection
          |
          +-- Document
          +-- Document
          +-- Document


SQL terminology          MongoDB terminology

Database              -> Database
Table                 -> Collection
Row                   -> Document
Column                -> Field

------------------------------------------------------------
3. DATABASE
------------------------------------------------------------

A database is a container for collections.

Example:

ytmanager

Inside it:

ytmanager
    |
    +-- videos
    +-- users
    +-- comments

In PyMongo:

db = client["ytmanager"]

------------------------------------------------------------
4. COLLECTION
------------------------------------------------------------

A collection is similar to a table in SQL.

Example:

videos

It contains multiple documents.

In PyMongo:

video_collection = db["videos"]

A collection does not require a fixed schema like a
traditional SQL table.

------------------------------------------------------------
5. DOCUMENT
------------------------------------------------------------

A document is the basic unit of data in MongoDB.

Example:

{
    "name": "Blinding Lights",
    "time": "6 min"
}

Another document could contain different fields:

{
    "name": "Dhun",
    "time": "4 min",
    "artist": "Unknown"
}

MongoDB allows flexible document structures.

------------------------------------------------------------
6. FIELD
------------------------------------------------------------

A field is similar to a column in SQL.

Example:

{
    "name": "Dhun",
    "time": "4 min"
}

Fields:

name
time

------------------------------------------------------------
7. BSON
------------------------------------------------------------

MongoDB stores documents internally as BSON.

BSON = Binary JSON

BSON supports additional data types that normal JSON
does not have, such as:

- ObjectId
- Date
- Binary data
- Decimal128

------------------------------------------------------------
8. _id FIELD
------------------------------------------------------------

Every MongoDB document normally has a unique "_id" field.

Example:

{
    "_id": ObjectId("6a8d874b78391d7832899f26"),
    "name": "Dhun",
    "time": "4 min"
}

MongoDB automatically generates _id if we don't provide one.

Example:

video_collection.insert_one({
    "name": "Dhun",
    "time": "4 min"
})

MongoDB automatically creates:

"_id": ObjectId(...)

------------------------------------------------------------
9. ObjectId
------------------------------------------------------------

ObjectId is MongoDB's commonly used identifier type.

Example:

ObjectId("6a8d874b78391d7832899f26")

When receiving an ID from the user, it is usually a string.

Therefore we convert:

video_id = input(...)

into:

ObjectId(video_id)

Example:

ObjectId(video_id)

------------------------------------------------------------
10. MONGODB CONNECTION
------------------------------------------------------------

PyMongo is the official Python driver commonly used to
connect Python applications with MongoDB.

Example:

from pymongo import MongoClient

client = MongoClient(MONGODB_URI)

client
    |
    +-- database
          |
          +-- collection
                |
                +-- documents

------------------------------------------------------------
11. MONGODB URI
------------------------------------------------------------

A MongoDB connection string contains information required
to connect to the MongoDB server.

Example:

mongodb+srv://username:password@cluster.mongodb.net/

Important:

Never hard-code credentials in source code.

Bad:

MongoClient(
    "mongodb+srv://username:password@cluster.mongodb.net/"
)

Better:

Store credentials in environment variables.

------------------------------------------------------------
12. ENVIRONMENT VARIABLES
------------------------------------------------------------

Sensitive configuration should be stored outside the
source code.

Example .env:

MONGO_USERNAME=managerpy
MONGO_PASSWORD=managerpy
MONGO_CLUSTER=cluster0.example.mongodb.net
MONGO_DATABASE=ytmanager

Python:

from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")
database = os.getenv("MONGO_DATABASE")

------------------------------------------------------------
13. DATABASE ACCESS
------------------------------------------------------------

After connecting:

client = MongoClient(...)

Select database:

db = client["ytmanager"]

Select collection:

videos = db["videos"]

So the hierarchy is:

MongoClient
    |
    +-- Database
          |
          +-- Collection
                |
                +-- Document

------------------------------------------------------------
14. CRUD
------------------------------------------------------------

CRUD means:

C -> Create
R -> Read
U -> Update
D -> Delete

MongoDB provides operations for all four.

Create:

insert_one()
insert_many()

Read:

find_one()
find()

Update:

update_one()
update_many()

Delete:

delete_one()
delete_many()

------------------------------------------------------------
15. CREATE
------------------------------------------------------------

Insert one document:

video_collection.insert_one({
    "name": "Tum Hi Ho",
    "time": "5 min"
})

Insert multiple documents:

video_collection.insert_many([
    {
        "name": "Dhun",
        "time": "4 min"
    },
    {
        "name": "Blinding Lights",
        "time": "6 min"
    }
])

------------------------------------------------------------
16. READ
------------------------------------------------------------

Find one document:

video_collection.find_one()

Find documents:

video_collection.find()

Example:

for video in video_collection.find():
    print(video)

------------------------------------------------------------
17. FILTERING
------------------------------------------------------------

find() can accept a filter.

Example:

video_collection.find({
    "name": "Dhun"
})

This means:

Find documents where name == "Dhun".

Example:

video_collection.find_one({
    "name": "Dhun"
})

------------------------------------------------------------
18. UPDATE
------------------------------------------------------------

update_one() updates one matching document.

Example:

video_collection.update_one(
    {"name": "Dhun"},
    {
        "$set": {
            "time": "5 min"
        }
    }
)

The first argument is the filter.

The second argument contains the update operation.

------------------------------------------------------------
19. $set
------------------------------------------------------------

$set changes specific fields.

Example:

{
    "$set": {
        "name": "New Name",
        "time": "10 min"
    }
}

It does NOT replace the entire document.

------------------------------------------------------------
20. DELETE
------------------------------------------------------------

Delete one document:

video_collection.delete_one({
    "name": "Dhun"
})

Delete multiple documents:

video_collection.delete_many({
    "time": "5 min"
})

Be careful with delete_many().

------------------------------------------------------------
21. UPDATE RESULT
------------------------------------------------------------

update_one() returns a result object.

Example:

result = video_collection.update_one(
    {"_id": ObjectId(video_id)},
    {
        "$set": {
            "name": "New Name"
        }
    }
)

Useful properties:

result.matched_count
result.modified_count

matched_count:

How many documents matched the filter.

modified_count:

How many documents were actually modified.

------------------------------------------------------------
22. DELETE RESULT
------------------------------------------------------------

delete_one() also returns a result.

Example:

result = video_collection.delete_one({
    "_id": ObjectId(video_id)
})

result.deleted_count

If:

deleted_count == 1

then a document was deleted.

If:

deleted_count == 0

then no matching document was found.

------------------------------------------------------------
23. MONGODB ATLAS
------------------------------------------------------------

MongoDB Atlas is MongoDB's cloud database service.

Instead of running MongoDB only on your local machine,
you can use a MongoDB cluster hosted in the cloud.

Architecture:

Python Application
        |
        | Internet
        ↓
MongoDB Atlas
        |
        +-- Cluster
              |
              +-- Database
                    |
                    +-- Collection
                          |
                          +-- Documents

------------------------------------------------------------
24. LOCAL MONGODB vs MONGODB ATLAS
------------------------------------------------------------

Local MongoDB:

Application
    |
    ↓
MongoDB running on your computer

MongoDB Atlas:

Application
    |
    ↓
Internet
    |
    ↓
MongoDB Atlas Cloud
    |
    ↓
Cluster

------------------------------------------------------------
25. SCHEMA FLEXIBILITY
------------------------------------------------------------

MongoDB is schema-flexible.

Example document 1:

{
    "name": "Dhun",
    "time": "4 min"
}

Document 2:

{
    "name": "Blinding Lights",
    "time": "6 min",
    "artist": "The Weeknd"
}

Both can exist in the same collection.

However, schema flexibility does NOT mean
"no structure is required."

Production applications should still maintain
a consistent data model.

------------------------------------------------------------
26. INDEX
------------------------------------------------------------

An index improves query performance.

Without an index:

MongoDB may need to scan many documents.

With an appropriate index:

MongoDB can locate matching documents much faster.

Example:

Create an index on name:

video_collection.create_index("name")

MongoDB automatically creates an index on _id.

------------------------------------------------------------
27. EMBEDDING vs REFERENCING
------------------------------------------------------------

MongoDB supports two common ways of modeling related data.

1. Embedding

2. Referencing

Embedding:

{
    "name": "Video",
    "comments": [
        {
            "user": "A",
            "text": "Great!"
        },
        {
            "user": "B",
            "text": "Nice!"
        }
    ]
}

Data is stored inside the same document.

Referencing:

Video document:

{
    "_id": 101,
    "name": "Video"
}

Comment document:

{
    "_id": 501,
    "video_id": 101,
    "text": "Great!"
}

The documents are connected using an ID.

------------------------------------------------------------
28. NoSQL
------------------------------------------------------------

NoSQL means "Not Only SQL".

MongoDB is a document-oriented NoSQL database.

Common characteristics:

- Document-based
- Flexible schema
- JSON-like data model
- Horizontal scaling support
- High availability features
- Powerful querying
- Distributed architecture

------------------------------------------------------------
29. MongoDB vs SQL
------------------------------------------------------------

SQL:

Tables
Rows
Columns
JOINs
Fixed schema

MongoDB:

Collections
Documents
Fields
Embedding / references
Flexible schema

Example SQL:

SELECT * FROM videos;

MongoDB:

db.videos.find()

------------------------------------------------------------
30. PYTHON + MONGODB FLOW
------------------------------------------------------------

Your current project follows this flow:

.env
 |
 ↓
load_dotenv()
 |
 ↓
os.getenv()
 |
 ↓
MongoClient()
 |
 ↓
MongoDB Atlas
 |
 ↓
Database
 |
 ↓
Collection
 |
 ↓
CRUD functions
 |
 ↓
main()
 |
 ↓
User

------------------------------------------------------------
31. YOUR YOUTUBE MANAGER
------------------------------------------------------------

Your application structure:

MongoDB Atlas
      |
      ↓
ytmanager
      |
      ↓
videos
      |
      +-----------------------+
      |                       |
      ↓                       ↓
   Document                Document
      |                       |
      ↓                       ↓
{
    "_id": ...,
    "name": "...",
    "time": "..."
}

------------------------------------------------------------
32. IMPORTANT PYTHON EXCEPTIONS
------------------------------------------------------------

MongoDB-related operations can fail.

PyMongo provides MongoDB-specific exceptions.

Example:

from pymongo.errors import PyMongoError

try:
    ...
except PyMongoError as e:
    print(e)

Invalid ObjectId:

from bson.errors import InvalidId

try:
    ObjectId(video_id)
except InvalidId:
    print("Invalid ID")

------------------------------------------------------------
33. IMPORTANT SECURITY RULES
------------------------------------------------------------

NEVER:

1. Hard-code passwords
2. Push .env to GitHub
3. Commit database credentials
4. Disable TLS certificate verification in production

Use:

.env
.gitignore
environment variables
secret management systems

Example .gitignore:

.env

------------------------------------------------------------
34. IMPORTANT INTERVIEW TERMS
------------------------------------------------------------

Know these terms:

MongoDB
NoSQL
Document database
Collection
Document
Field
BSON
ObjectId
MongoDB Atlas
PyMongo
CRUD
find()
find_one()
insert_one()
insert_many()
update_one()
update_many()
delete_one()
delete_many()
$set
Index
Embedding
Referencing
Schema flexibility
Replication
Sharding
Transactions

------------------------------------------------------------
35. CORE MENTAL MODEL
------------------------------------------------------------

Remember MongoDB like this:

MongoClient
    ↓
Database
    ↓
Collection
    ↓
Document
    ↓
Field

Example:

client
  ↓
ytmanager
  ↓
videos
  ↓
{
    "_id": ObjectId(...),
    "name": "Blinding Lights",
    "time": "6 min"
}

"""





'''
One important thing for your current project

You are now at the point where you should understand this hierarchy very clearly:

MongoDB Atlas
      ↓
    Cluster
      ↓
   Database
      ↓
  Collection
      ↓
   Document
      ↓
     Field

And your Python code:

client = MongoClient(...)

↓

db = client[database]

↓

video_collection = db["videos"]

↓

video_collection.insert_one(...)
video_collection.find(...)
video_collection.update_one(...)
video_collection.delete_one(...)

That is the core MongoDB + PyMongo mental model.

'''




'''

MongoDB Complete Learning Roadmap
🟢 Level 1 — Fundamentals

Ye tum almost kar chuke ho.

What is MongoDB?
NoSQL vs SQL
MongoDB architecture
Database
Collection
Document
Field
BSON
_id and ObjectId
MongoDB Atlas
MongoDB connection URI
PyMongo basics
.env / environment variables
🟢 Level 2 — CRUD ⭐

Most important for your current project.

insert_one()
insert_many()
find()
find_one()
Query filters
Comparison operators:
$eq
$ne
$gt
$gte
$lt
$lte
$in
$nin
Logical operators:
$and
$or
$not
$nor
update_one()
update_many()
$set
$unset
$inc
$push
$pull
delete_one()
delete_many()

🟡 Level 3 — Querying Properly
Projection
Sorting
Limiting results
Skipping results
Pagination
Nested documents
Arrays
Querying arrays
Querying nested fields
Regular expressions
Distinct values
count_documents()

Example:

videos.find(
    {"time": {"$gt": "5 min"}},
    {"name": 1, "time": 1}
).sort("name", 1).limit(10)

🟡 Level 4 — Indexing ⭐

Very important for backend/interviews.

What is an index?
Why indexes improve performance
Collection scan
Index scan
Single-field index
Compound index
Unique index
Multikey index
Indexing rules
create_index()
drop_index()
explain()
Query performance

You should understand:

Without index
Query
 ↓
Scan many documents
 ↓
Find matching document

vs.

With index
Query
 ↓
Index
 ↓
Locate document

🟡 Level 5 — Data Modeling ⭐

This becomes very important when building real applications.

Schema design
Embedding
Referencing
One-to-one relationships
One-to-many relationships
Many-to-many relationships
Embedding vs referencing
Data duplication
Normalization vs denormalization
Schema validation

You should be able to answer:

"Should I embed this data or create another collection?"

🟠 Level 6 — Aggregation ⭐

Very important MongoDB topic.

Aggregation framework
Aggregation pipeline
$match
$group
$project
$sort
$limit
$skip
$unwind
$lookup
$count
$sum
$avg
$min
$max
$push

Example:

Documents
    ↓
$match
    ↓
$group
    ↓
$sort
    ↓
$project
    ↓
Result

🟠 Level 7 — Transactions & Consistency
Atomic operations
MongoDB transactions
Sessions
ACID transactions
Read concern
Write concern
Read preference
Consistency concepts

You don't need extreme depth initially.

🔴 Level 8 — MongoDB Internals & Scaling

This is where MongoDB becomes more system-design/interview oriented.

Replica sets
Primary
Secondary
Replication
Automatic failover
Election
Write concern
Read preference
Sharding
Shard key
Config servers
mongos
Horizontal scaling
High availability

Basic architecture:

                MongoDB Cluster
                      |
          +-----------+-----------+
          ↓                       ↓
       Primary                Secondary
          |                       |
          +------ Replication ----+

🔴 Level 9 — Production MongoDB

For actual backend/cloud engineering:

Authentication
Authorization
MongoDB users/roles
Network access
TLS/SSL
Secrets management
Backups
Restore
Monitoring
Performance optimization
Connection pooling
Connection limits
Logging
MongoDB Atlas monitoring
For YOU specifically

Don't study all 116 topics right now.

Your current position is approximately:

MongoDB Fundamentals       ✅
MongoDB Atlas              ✅
PyMongo                    ✅
.env                       ✅
CRUD                       ✅
ObjectId                   ✅

Query Operators            ⬜
Advanced Queries           ⬜
Indexes                    ⬜
Data Modeling              ⬜
Aggregation                ⬜
Transactions               ⬜
Replication                ⬜
Sharding                   ⬜
Production/Monitoring      ⬜
Your next sequence should be:
CRUD
 ↓
Query Operators
 ↓
Advanced Queries
 ↓
Indexes
 ↓
Data Modeling
 ↓
Aggregation
 ↓
Transactions
 ↓
Replication
 ↓
Sharding
 ↓
Production/Atlas

For your current YouTube Manager project, Level 1-3 + basic Level 4 is enough. Then you can move on rather than spending weeks on MongoDB.

And since your main goal is AI/ML + software engineering, you don't need to become a MongoDB specialist. You need to be able to use MongoDB confidently in a Python backend and understand its performance/data-modeling fundamentals.
'''