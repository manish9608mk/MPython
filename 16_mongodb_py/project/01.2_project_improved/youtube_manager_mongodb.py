#1
from pymongo import MongoClient
from bson import ObjectId
from pymongo.errors import PyMongoError

from dotenv import load_dotenv
import os
import re


#2
# Load environment variables from .env
load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")
database = os.getenv("MONGO_DATABASE")

if not all([username, password, cluster, database]):
    raise ValueError("MongoDB environment variables are missing.")


#3
# Connect to MongoDB
try:
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@{cluster}/"
    )

    client.admin.command("ping")
    print("MongoDB connected successfully.")

except PyMongoError as e:
    print(f"MongoDB connection failed: {e}")
    raise SystemExit(1)


#4
# Select database and collection
db = client[database]
video_collection = db["videos"]


#5
# Fetch videos, sort by name and limit results
def list_videos():
    print("-" * 70)

    try:
        videos = video_collection.find().sort("name", 1).limit(30)

        for video in videos:
            print(
                f"\nID: {video['_id']}, "
                f"Name: {video['name']}, "
                f"Time: {video['time']}"
            )

    except PyMongoError as e:
        print(f"Failed to fetch videos: {e}")

    print("-" * 70)


#6
# Insert a new document
def add_video(name, time):
    try:
        result = video_collection.insert_one({
            "name": name,
            "time": time
        })

        print(f"Video added successfully! ID: {result.inserted_id}")

    except PyMongoError as e:
        print(f"Failed to add video: {e}")


#7
# Update a document using ObjectId
def update_video(video_id, updated_name, updated_time):

    if not ObjectId.is_valid(video_id):
        print("Invalid video ID!")
        return

    try:
        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {
                "$set": {
                    "name": updated_name,
                    "time": updated_time
                }
            }
        )

        if result.matched_count == 0:
            print("Video not found!")
        else:
            print("Video updated successfully!")

    except PyMongoError as e:
        print(f"Failed to update video: {e}")


#8
# Delete a document using ObjectId
def delete_video(video_id):

    if not ObjectId.is_valid(video_id):
        print("Invalid video ID!")
        return

    try:
        result = video_collection.delete_one(
            {"_id": ObjectId(video_id)}
        )

        if result.deleted_count == 0:
            print("Video not found!")
        else:
            print("Video deleted successfully!")

    except PyMongoError as e:
        print(f"Failed to delete video: {e}")


#9
# Search using regex
def search_videos(name):
    try:
        query = {
            "name": {
                "$regex": re.escape(name),
                "$options": "i"
            }
        }

        videos = video_collection.find(query)

        found = False

        for video in videos:
            found = True

            print(
                f"\nID: {video['_id']}, "
                f"Name: {video['name']}, "
                f"Time: {video['time']}"
            )

        if not found:
            print("No videos found!")

    except PyMongoError as e:
        print(f"Failed to search videos: {e}")


#10
# Find videos using comparison operator $gt
def find_long_videos(min_time):
    try:
        videos = video_collection.find({
            "time": {"$gt": min_time}
        })

        found = False

        for video in videos:
            found = True

            print(
                f"\nID: {video['_id']}, "
                f"Name: {video['name']}, "
                f"Time: {video['time']}"
            )

        if not found:
            print("No videos found!")

    except PyMongoError as e:
        print(f"Failed to find videos: {e}")


#11
# Find videos using comparison operator $lt
def find_short_videos(max_time):
    try:
        videos = video_collection.find({
            "time": {"$lt": max_time}
        })

        found = False

        for video in videos:
            found = True

            print(
                f"\nID: {video['_id']}, "
                f"Name: {video['name']}, "
                f"Time: {video['time']}"
            )

        if not found:
            print("No videos found!")

    except PyMongoError as e:
        print(f"Failed to find videos: {e}")


#12
# Create an index on name
def create_indexes():
    try:
        index_name = video_collection.create_index([("name", 1)])
        print(f"Index created successfully: {index_name}")

    except PyMongoError as e:
        print(f"Failed to create index: {e}")


#13
# Display collection indexes
def list_indexes():
    try:
        indexes = video_collection.list_indexes()

        for index in indexes:
            print(index)

    except PyMongoError as e:
        print(f"Failed to list indexes: {e}")


#14
# Calculate video statistics
def video_statistics():
    try:
        result = video_collection.aggregate([
            {
                "$group": {
                    "_id": None,
                    "total_videos": {"$sum": 1},
                    "total_time": {"$sum": "$time"},
                    "average_time": {"$avg": "$time"},
                    "shortest_time": {"$min": "$time"},
                    "longest_time": {"$max": "$time"}
                }
            }
        ])

        for stats in result:
            print(f"\nTotal videos: {stats['total_videos']}")
            print(f"Total time: {stats['total_time']}")
            print(f"Average time: {stats['average_time']}")
            print(f"Shortest video: {stats['shortest_time']}")
            print(f"Longest video: {stats['longest_time']}")

    except PyMongoError as e:
        print(f"Failed to calculate statistics: {e}")

#15
# Main menu
def main():

    while True:
        print("\nYouTube Manager App Using MongoDB")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Search videos")
        print("4. Find long videos")
        print("5. Update a video")
        print("6. Delete a video")
        print("7. Create index")
        print("8. List indexes")
        print("9. Exit the app")
        print("10. Video statistics")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            list_videos()

        elif choice == 2:
            name = input("Enter video name: ")

            try:
                time = int(input("Enter video time: "))

            except ValueError:
                print("Please enter a valid number!")
                continue

            add_video(name, time)

        elif choice == 3:
            name = input("Enter video name to search: ")
            search_videos(name)

        elif choice == 4:
            try:
                min_time = int(input("Enter minimum video time: "))
                find_long_videos(min_time)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == 5:
            video_id = input("Enter video ID to update: ")
            updated_name = input("Enter the updated video name: ")

            try:
                updated_time = int(input("Enter the updated video time: "))

            except ValueError:
                print("Please enter a valid number!")
                continue

            update_video(video_id, updated_name, updated_time)

        elif choice == 6:
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == 7:
            create_indexes()

        elif choice == 8:
            list_indexes()

        elif choice == 9:
            print("Exiting application...")
            break

        elif choice == 10:
            video_statistics()

        else:
            print("Invalid choice!")


#16
# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()





'''
===========================================================
        MONGODB + PYMONGO REVISION NOTES
        Based on This YouTube Manager Project
===========================================================


#1 IMPORTS
-----------------------------------------------------------

from pymongo import MongoClient
    -> MongoDB se connection banane ke liye.

from bson import ObjectId
    -> MongoDB ke _id ko ObjectId ke form mein handle karne ke liye.

from pymongo.errors import PyMongoError
    -> MongoDB/PyMongo errors handle karne ke liye.

from dotenv import load_dotenv
    -> .env file se environment variables load karne ke liye.

import os
    -> Environment variables access karne ke liye.

import re
    -> Regular Expression (regex) search ke liye.


===========================================================
#2 ENVIRONMENT VARIABLES
===========================================================

load_dotenv()

    -> .env file ke variables ko Python mein load karta hai.

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")
database = os.getenv("MONGO_DATABASE")

    -> .env se values read karta hai.

Example .env:

MONGO_USERNAME=abc
MONGO_PASSWORD=xyz
MONGO_CLUSTER=cluster.mongodb.net
MONGO_DATABASE=youtube_db


if not all([username, password, cluster, database]):
    raise ValueError("MongoDB environment variables are missing.")

    -> Check karta hai ki required variables available hain ya nahi.

all([...])
    -> Sab values truthy honi chahiye.

raise ValueError(...)
    -> Invalid/missing value hone par error raise karta hai.


===========================================================
#3 MONGODB CONNECTION
===========================================================

client = MongoClient(
    f"mongodb+srv://{username}:{password}@{cluster}/"
)

    -> MongoDB server se connection create karta hai.

client
    -> MongoDB connection object.

MongoClient()
    -> MongoDB server ke saath connection establish karne ke
       liye PyMongo ka main class.


client.admin.command("ping")

    -> MongoDB connection test karta hai.

Agar successful:
    MongoDB connected successfully.


try:
    ...
except PyMongoError as e:
    ...

    -> MongoDB related errors safely handle karta hai.

e
    -> Actual error object.


===========================================================
#4 DATABASE AND COLLECTION
===========================================================

db = client[database]

    -> Database select karta hai.

video_collection = db["videos"]

    -> "videos" collection select karta hai.


MongoDB structure:

MongoDB
   |
   +-- Database
          |
          +-- Collection
                 |
                 +-- Document
                 +-- Document
                 +-- Document


Example document:

{
    "_id": ObjectId("..."),
    "name": "Blinding Lights",
    "time": 4
}


MongoDB mein:

Database     -> youtube_db
Collection   -> videos
Document     -> ek video


===========================================================
#5 FIND DOCUMENTS
===========================================================

video_collection.find()

    -> Collection ke documents retrieve karta hai.

Example:

videos = video_collection.find()

    -> Saare documents.


-----------------------------------------------------------
SORT
-----------------------------------------------------------

video_collection.find().sort("name", 1)

    -> name ke according ascending order.

1  = Ascending
-1 = Descending


Example:

.sort("name", 1)

A -> Z


.sort("name", -1)

Z -> A


-----------------------------------------------------------
LIMIT
-----------------------------------------------------------

.limit(30)

    -> Maximum 30 documents return karega.

Example:

find().sort("name", 1).limit(30)


Flow:

find()
   ↓
sort()
   ↓
limit()
   ↓
results


-----------------------------------------------------------
ITERATING RESULTS
-----------------------------------------------------------

for video in videos:
    print(video)

    -> MongoDB se aaye documents ko one by one process karta hai.


-----------------------------------------------------------
DOCUMENT FIELD ACCESS
-----------------------------------------------------------

video["_id"]
video["name"]
video["time"]

    -> Document ke fields access karne ke liye.


===========================================================
#6 INSERT
===========================================================

video_collection.insert_one({
    "name": name,
    "time": time
})

    -> Collection mein ek new document insert karta hai.


Example:

{
    "name": "Save Your Tears",
    "time": 4
}


insert_one()
    -> Single document insert.


-----------------------------------------------------------
INSERT RESULT
-----------------------------------------------------------

result = video_collection.insert_one({...})

result.inserted_id

    -> Newly inserted document ka MongoDB-generated _id.


Example:

Video added successfully!
ID: 68xxxxxxxxxxxxxxxx


===========================================================
#7 UPDATE
===========================================================

video_collection.update_one(
    {"_id": ObjectId(video_id)},
    {
        "$set": {
            "name": updated_name,
            "time": updated_time
        }
    }
)


update_one()
    -> Ek matching document update karta hai.


First argument:
----------------

{"_id": ObjectId(video_id)}

    -> Kis document ko find karna hai.


Second argument:
-----------------

{
    "$set": {
        "name": updated_name,
        "time": updated_time
    }
}

    -> Kaunse fields update karne hain.


-----------------------------------------------------------
$set
-----------------------------------------------------------

"$set"

    -> Existing field ki value change karta hai.


Example:

Before:

{
    "name": "Dhun",
    "time": 4
}


After:

{
    "name": "Dhun Updated",
    "time": 5
}


-----------------------------------------------------------
ObjectId
-----------------------------------------------------------

MongoDB ka default _id generally ObjectId hota hai.

MongoDB:

"_id": ObjectId("68abcdef...")


User input:

video_id = "68abcdef..."


Convert:

ObjectId(video_id)


-----------------------------------------------------------
VALIDATE OBJECTID
-----------------------------------------------------------

ObjectId.is_valid(video_id)

    -> Check karta hai ki given ID valid ObjectId format mein hai
       ya nahi.


-----------------------------------------------------------
UPDATE RESULT
-----------------------------------------------------------

result.matched_count

    -> Kitne documents match hue.


0
    -> Document nahi mila.

1
    -> Document match hua.


===========================================================
#8 DELETE
===========================================================

video_collection.delete_one(
    {"_id": ObjectId(video_id)}
)


delete_one()
    -> Matching document delete karta hai.


-----------------------------------------------------------
DELETE RESULT
-----------------------------------------------------------

result.deleted_count

    -> Kitne documents delete hue.


0
    -> Document nahi mila.

1
    -> Document delete hua.


===========================================================
#9 SEARCH WITH REGEX
===========================================================

query = {
    "name": {
        "$regex": re.escape(name),
        "$options": "i"
    }
}


video_collection.find(query)


-----------------------------------------------------------
$regex
-----------------------------------------------------------

"$regex"

    -> Pattern-based text search.


Example:

Database:

"Python Tutorial"
"Python Advanced"
"Docker Tutorial"


Search:

Python

    -> Python Tutorial
    -> Python Advanced


-----------------------------------------------------------
$options: "i"
-----------------------------------------------------------

"i"

    -> Case-insensitive search.


Python
python
PYTHON
PyThOn

    -> Same search treat hoga.


-----------------------------------------------------------
re.escape()
-----------------------------------------------------------

re.escape(name)

    -> User input ke special regex characters ko safely escape
       karta hai.


===========================================================
#10 COMPARISON OPERATOR: $gt
===========================================================

video_collection.find({
    "time": {"$gt": min_time}
})


$gt
    -> Greater Than


Example:

{"time": {"$gt": 5}}

    -> time > 5


Agar videos:

2
4
6
8

Query:

time > 5

Result:

6
8


-----------------------------------------------------------
OTHER COMMON COMPARISON OPERATORS
-----------------------------------------------------------

$gt
    -> Greater than

$gte
    -> Greater than or equal

$lt
    -> Less than

$lte
    -> Less than or equal

$eq
    -> Equal

$ne
    -> Not equal

$in
    -> Given list mein se koi value

$nin
    -> Given list mein se koi value nahi


Examples:

{"time": {"$gt": 5}}

{"time": {"$gte": 5}}

{"time": {"$lt": 5}}

{"time": {"$lte": 5}}

{"time": {"$eq": 5}}

{"time": {"$ne": 5}}

{"time": {"$in": [3, 5, 7]}}

{"time": {"$nin": [3, 5, 7]}}


Important:
    Tumhare project mein mainly $gt use hua hai.
    Baaki operators need ke according use karna.


===========================================================
#11 FIND SHORT VIDEOS
===========================================================

video_collection.find({
    "time": {"$lt": max_time}
})


$lt
    -> Less Than


Example:

{"time": {"$lt": 5}}

    -> time < 5


===========================================================
#12 INDEX
===========================================================

video_collection.create_index([("name", 1)])


    -> name field par index create karta hai.


1
    -> Ascending index

-1
    -> Descending index


Index ka purpose:

Without index:
    MongoDB ko bahut documents scan karne pad sakte hain.


With index:
    Search/query faster ho sakti hai.


Example:

create_index([("name", 1)])


-----------------------------------------------------------
LIST INDEXES
-----------------------------------------------------------

video_collection.list_indexes()

    -> Collection ke existing indexes show karta hai.


Default MongoDB index:

_id_


MongoDB automatically _id field par index create karta hai.


===========================================================
#13 AGGREGATION PIPELINE
===========================================================

video_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "total_videos": {"$sum": 1},
            "total_time": {"$sum": "$time"},
            "average_time": {"$avg": "$time"},
            "shortest_time": {"$min": "$time"},
            "longest_time": {"$max": "$time"}
        }
    }
])


aggregate()

    -> Documents par calculations/processing karne ke liye.


Aggregation pipeline:

documents
    ↓
stage 1
    ↓
stage 2
    ↓
stage 3
    ↓
final result


Har stage previous stage ka output process karta hai.


-----------------------------------------------------------
$group
-----------------------------------------------------------

"$group"

    -> Documents ko group karke calculations karne ke liye.


"_id": None

    -> Saare documents ko ek single group mein rakho.


-----------------------------------------------------------
$sum
-----------------------------------------------------------

"total_videos": {"$sum": 1}

    -> Har document ke liye 1 add karta hai.

Example:

5 documents

1 + 1 + 1 + 1 + 1 = 5


-----------------------------------------------------------
SUM FIELD
-----------------------------------------------------------

"total_time": {"$sum": "$time"}

    -> Sabhi videos ke time ko add karta hai.


Example:

4 + 5 + 6 = 15


"$time"

    -> MongoDB document ke time field ko refer karta hai.


Important:

"$time"
    -> Field reference

time
    -> Normal Python variable / key name context ke according


-----------------------------------------------------------
$avg
-----------------------------------------------------------

"average_time": {"$avg": "$time"}

    -> Average calculate karta hai.


Example:

4, 6, 8

Average:

18 / 3 = 6


-----------------------------------------------------------
$min
-----------------------------------------------------------

"shortest_time": {"$min": "$time"}

    -> Minimum value.


Example:

4, 7, 2, 9

Result:

2


-----------------------------------------------------------
$max
-----------------------------------------------------------

"longest_time": {"$max": "$time"}

    -> Maximum value.


Example:

4, 7, 2, 9

Result:

9


===========================================================
#14 AGGREGATION RESULT
===========================================================

result = video_collection.aggregate([...])

    -> Aggregation result return karta hai.


for stats in result:
    print(stats)


    -> Result ko iterate karte hain.


stats["total_videos"]
stats["total_time"]
stats["average_time"]
stats["shortest_time"]
stats["longest_time"]

    -> Aggregation se generated fields access karte hain.


Example result:

{
    "_id": None,
    "total_videos": 5,
    "total_time": 25,
    "average_time": 5,
    "shortest_time": 2,
    "longest_time": 8
}


===========================================================
#15 MONGODB QUERY BASIC STRUCTURE
===========================================================

MongoDB query generally:

{
    "field": {
        "operator": value
    }
}


Example:

{
    "time": {
        "$gt": 5
    }
}


Meaning:

time > 5


Simple equality:

{
    "name": "Python"
}


Meaning:

name == "Python"


===========================================================
#16 LOGICAL OPERATORS
===========================================================

$and
    -> All conditions true.


{
    "$and": [
        {"time": {"$gt": 5}},
        {"name": "Python"}
    ]
}


$or
    -> At least one condition true.


{
    "$or": [
        {"name": "Python"},
        {"name": "Docker"}
    ]
}


$not
    -> Condition ko negate karta hai.


$nor
    -> All conditions false hone chahiye.


For this project:
    $and and $or ka basic understanding enough hai.


===========================================================
#17 CURSOR
===========================================================

video_collection.find()

    -> Usually Cursor return karta hai.


Cursor ko:

for video in videos:
    ...

se iterate kar sakte hain.


Cursor par common methods:

.find()
.sort()
.limit()


Example:

video_collection.find().sort("name", 1).limit(30)


===========================================================
#18 ERROR HANDLING
===========================================================

try:
    MongoDB operation
except PyMongoError as e:
    print(e)


Purpose:

    Application crash hone ke bajay error handle karna.


Example:

try:
    result = video_collection.insert_one({...})

except PyMongoError as e:
    print(f"Failed to add video: {e}")


===========================================================
#19 MAIN MENU
===========================================================

while True:

    -> Menu continuously show karta hai.


choice = int(input(...))

    -> User input ko integer mein convert karta hai.


if / elif / else

    -> User ke choice ke according function call hota hai.


break

    -> while loop terminate karta hai.


continue

    -> Current iteration skip karke next iteration par jata hai.


Example:

if choice == 1:
    list_videos()

elif choice == 2:
    add_video(...)

elif choice == 9:
    break


===========================================================
#20 INPUT VALIDATION
===========================================================

try:
    time = int(input("Enter video time: "))

except ValueError:
    print("Please enter a valid number!")
    continue


input()
    -> Always string return karta hai.


int()
    -> String ko integer mein convert karta hai.


Invalid:

"4 min"

    -> int("4 min") ERROR


Valid:

"4"

    -> int("4") = 4


Important:

Tumhare current database mein:

"time": 4

ka unit MongoDB ko pata nahi hai.

4 ka matlab:
    4 seconds?
    4 minutes?

MongoDB ke liye sirf number 4 hai.

Unit application decide karti hai.

Agar project mein minutes decide kiya hai:

"time": 4

means:

4 minutes.


Better real-world design:

"time": 240

means:

240 seconds

OR

{
    "time": 4,
    "unit": "minutes"
}


But current project ke liye simple integer enough hai.


===========================================================
#21 PYTHON FUNCTION STRUCTURE USED IN PROJECT
===========================================================

def function_name(parameter):
    try:
        ...
    except PyMongoError as e:
        ...


Example:

def add_video(name, time):

    name
        -> parameter

    time
        -> parameter


Call:

add_video("Python", 5)


name = "Python"
time = 5


===========================================================
#22 IMPORTANT MONGODB METHODS USED
===========================================================

MongoClient()
    -> MongoDB connection

client.admin.command("ping")
    -> Connection test

client[database]
    -> Database select

db["videos"]
    -> Collection select

find()
    -> Read documents

insert_one()
    -> Insert one document

update_one()
    -> Update one document

delete_one()
    -> Delete one document

aggregate()
    -> Aggregation pipeline

create_index()
    -> Create index

list_indexes()
    -> Show indexes


===========================================================
#23 IMPORTANT OPERATORS USED
===========================================================

$set
    -> Update fields

$regex
    -> Regex search

$options
    -> Regex options

$gt
    -> Greater than

$lt
    -> Less than

$sum
    -> Sum

$avg
    -> Average

$min
    -> Minimum

$max
    -> Maximum

$group
    -> Group documents


===========================================================
#24 MOST IMPORTANT THINGS TO REMEMBER
===========================================================

MongoDB:

Database
    ↓
Collection
    ↓
Document
    ↓
Fields


CRUD:

Create
    -> insert_one()

Read
    -> find()

Update
    -> update_one()

Delete
    -> delete_one()


Queries:

find()
sort()
limit()


Filtering:

$gt
$lt
$gte
$lte
$eq
$ne
$in
$nin


Text search:

$regex
$options: "i"


Update:

$set


Aggregation:

aggregate()
    ↓
$group
    ↓
$sum
$avg
$min
$max


Indexes:

create_index()
list_indexes()


MongoDB ID:

ObjectId()
ObjectId.is_valid()


Errors:

try
except PyMongoError


===========================================================
#25 QUICK REVISION
===========================================================

Connect:

client = MongoClient(connection_string)


Database:

db = client["database_name"]


Collection:

collection = db["collection_name"]


Insert:

collection.insert_one({
    "name": "Python",
    "time": 5
})


Read:

collection.find()


Sort:

collection.find().sort("name", 1)


Limit:

collection.find().limit(10)


Update:

collection.update_one(
    {"_id": ObjectId(id)},
    {"$set": {"name": "New Name"}}
)


Delete:

collection.delete_one(
    {"_id": ObjectId(id)}
)


Search:

collection.find({
    "name": {
        "$regex": "python",
        "$options": "i"
    }
})


Greater than:

collection.find({
    "time": {"$gt": 5}
})


Less than:

collection.find({
    "time": {"$lt": 5}
})


Aggregation:

collection.aggregate([
    {
        "$group": {
            "_id": None,
            "total": {"$sum": 1},
            "sum_time": {"$sum": "$time"},
            "average": {"$avg": "$time"},
            "minimum": {"$min": "$time"},
            "maximum": {"$max": "$time"}
        }
    }
])


Index:

collection.create_index([
    ("name", 1)
])


List indexes:

collection.list_indexes()


===========================================================
#26 ONE-LINE MEMORY TRICK
===========================================================

MongoDB CRUD:

INSERT  -> insert_one()
READ    -> find()
UPDATE  -> update_one()
DELETE  -> delete_one()


Query:

find → filter → sort → limit


Aggregation:

aggregate → group → calculate


Index:

create_index → faster queries


ObjectId:

MongoDB _id → ObjectId()


===========================================================
'''