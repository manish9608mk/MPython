
'''
============================================================
# MONGODB AGGREGATION PIPELINE
============================================================

Aggregation Pipeline is used when we want to process,
transform, filter, group, sort, or calculate data
inside MongoDB.

Think of it like:

MongoDB Documents
       ↓
   Stage 1
       ↓
   Stage 2
       ↓
   Stage 3
       ↓
   Final Result


Each stage receives the output of the previous stage.

Basic syntax:

collection.aggregate([
    {
        "$stage": {
            ...
        }
    },
    {
        "$stage": {
            ...
        }
    }
])


============================================================
#1 $match
============================================================

$match is used to FILTER documents.

It is similar to find().

Example:

video_collection.aggregate([
    {
        "$match": {
            "time": {"$gt": 5}
        }
    }
])

Meaning:

Find videos whose time is greater than 5.


Equivalent find():

video_collection.find({
    "time": {"$gt": 5}
})


Common operators can also be used:

$gt   → greater than
$gte  → greater than or equal
$lt   → less than
$lte  → less than or equal
$eq   → equal
$ne   → not equal
$in   → one of these values
$nin  → none of these values


Example:

{
    "$match": {
        "time": {"$gte": 5}
    }
}


IMPORTANT:

$match is usually placed early in the pipeline
to reduce the number of documents processed by
later stages.


============================================================
#2 $group
============================================================

$group is used to GROUP documents and perform
calculations on them.

It is similar to GROUP BY in SQL.

Example:

{
    "$group": {
        "_id": None,
        "total_videos": {"$sum": 1}
    }
}


"_id": None means:

Put ALL documents into one group.


Example data:

Video A → 5
Video B → 4
Video C → 6


After grouping:

{
    "_id": None,
    "total_videos": 3
}


------------------------------------------------------------
# GROUP BY a field
------------------------------------------------------------

Suppose documents contain:

{
    "name": "Python",
    "category": "Programming"
}

{
    "name": "Docker",
    "category": "DevOps"
}

We can group by category:

{
    "$group": {
        "_id": "$category",
        "count": {"$sum": 1}
    }
}


"$category" means:

Use the value of the category field as the group key.


Example result:

{
    "_id": "Programming",
    "count": 5
}

{
    "_id": "DevOps",
    "count": 3
}


IMPORTANT:

Inside aggregation:

"$field"

means:

Take the value from that document's field.


Example:

"$time"

means the value stored in the time field.


============================================================
#3 $sum
============================================================

$sum is used to calculate totals.

Example:

{
    "$group": {
        "_id": None,
        "total_time": {"$sum": "$time"}
    }
}


If:

Video 1 → 5
Video 2 → 4
Video 3 → 6


Result:

total_time = 15


------------------------------------------------------------
# $sum: 1
------------------------------------------------------------

This is a very common pattern.

{
    "total_videos": {"$sum": 1}
}


It counts documents.

For example:

5 documents

→ total_videos = 5


So remember:

$sum: 1
→ COUNT documents

$sum: "$field"
→ SUM values of a field


============================================================
#4 $avg
============================================================

$avg calculates the average.

Example:

{
    "average_time": {"$avg": "$time"}
}


If:

5
4
6

Average:

(5 + 4 + 6) / 3 = 5


Result:

{
    "average_time": 5
}


============================================================
#5 $min
============================================================

$min finds the smallest value.

Example:

{
    "shortest_time": {"$min": "$time"}
}


If:

5
4
6

Result:

4


============================================================
#6 $max
============================================================

$max finds the largest value.

Example:

{
    "longest_time": {"$max": "$time"}
}


If:

5
4
6

Result:

6


============================================================
#7 YOUR CURRENT AGGREGATION
============================================================

Your project uses:

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


This means:

Step 1:

Take all documents.

Step 2:

Put all documents into one group.

Because:

"_id": None


Step 3:

Calculate:

$sum: 1
→ number of videos

$sum: "$time"
→ total video time

$avg: "$time"
→ average video time

$min: "$time"
→ shortest video

$max: "$time"
→ longest video


Example:

Database:

Python → 5
Docker → 4
AWS → 6


Aggregation result:

{
    "_id": None,
    "total_videos": 3,
    "total_time": 15,
    "average_time": 5,
    "shortest_time": 4,
    "longest_time": 6
}


============================================================
#8 $sort
============================================================

$sort is used to sort documents.

Syntax:

{
    "$sort": {
        "time": 1
    }
}


1  → ascending
-1 → descending


Ascending:

4
5
6
7


Descending:

7
6
5
4


Example:

video_collection.aggregate([
    {
        "$sort": {
            "time": -1
        }
    }
])


This gives longest videos first.


------------------------------------------------------------
# SORT BY NAME
------------------------------------------------------------

{
    "$sort": {
        "name": 1
    }
}


A → B → C


Descending:

{
    "$sort": {
        "name": -1
    }
}


Z → Y → X


============================================================
#9 $limit
============================================================

$limit restricts the number of documents.

Example:

{
    "$limit": 5
}


Only first 5 documents continue to the next stage.


Example:

video_collection.aggregate([
    {
        "$sort": {
            "time": -1
        }
    },
    {
        "$limit": 3
    }
])


Meaning:

1. Sort videos by time descending.
2. Take only 3 videos.


Result:

Top 3 longest videos.


IMPORTANT:

ORDER MATTERS.


$sort → $limit

means:

"Give me the top 3 longest videos."


$limit → $sort

means:

"Take 3 documents first, then sort those 3."


These are NOT the same.


============================================================
#10 $project
============================================================

$project controls which fields should appear
in the output.

Example:

{
    "$project": {
        "_id": 0,
        "name": 1,
        "time": 1
    }
}


Meaning:

Show:

name
time

Hide:

_id


1 → include
0 → exclude


Example document:

{
    "_id": "...",
    "name": "Python",
    "time": 5
}


After $project:

{
    "name": "Python",
    "time": 5
}


============================================================
#11 $skip
============================================================

$skip skips a certain number of documents.

Example:

{
    "$skip": 5
}


Skip first 5 documents.


Common use:

Pagination.

Example:

$skip 10
$limit 10

means:

Skip first 10
Take next 10


This gives approximately page 2.


============================================================
#12 MULTIPLE STAGES
============================================================

The real power of aggregation comes from combining
multiple stages.


Example:

video_collection.aggregate([
    {
        "$match": {
            "time": {"$gt": 3}
        }
    },
    {
        "$sort": {
            "time": -1
        }
    },
    {
        "$limit": 3
    }
])


Flow:

All videos
    ↓
Only videos > 3
    ↓
Sort longest first
    ↓
Take top 3


This is the most important concept:

PIPELINE = multiple operations connected together.


============================================================
#13 $match + $group
============================================================

We can filter first and then calculate statistics.

Example:

video_collection.aggregate([
    {
        "$match": {
            "time": {"$gt": 5}
        }
    },
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1},
            "average_time": {"$avg": "$time"}
        }
    }
])


Meaning:

1. Find videos longer than 5.
2. Count them.
3. Calculate their average time.


Flow:

Documents
   ↓
$match
   ↓
Filtered documents
   ↓
$group
   ↓
Statistics


============================================================
#14 $group BY FIELD
============================================================

Example:

Suppose documents contain:

{
    "name": "Python",
    "category": "Programming",
    "time": 5
}

{
    "name": "Docker",
    "category": "DevOps",
    "time": 4
}

We can group by category:

video_collection.aggregate([
    {
        "$group": {
            "_id": "$category",
            "total_videos": {"$sum": 1},
            "total_time": {"$sum": "$time"}
        }
    }
])


Result could be:

Programming
→ total_videos: 5
→ total_time: 30

DevOps
→ total_videos: 3
→ total_time: 15


Remember:

"_id": "$category"

means:

GROUP BY category


============================================================
#15 $unwind
============================================================

$unwind is used when a document contains an ARRAY
and we want to process each array element separately.

Example document:

{
    "name": "Python Course",
    "tags": ["python", "backend", "programming"]
}


Using:

{
    "$unwind": "$tags"
}


MongoDB produces:

{
    "name": "Python Course",
    "tags": "python"
}

{
    "name": "Python Course",
    "tags": "backend"
}

{
    "name": "Python Course",
    "tags": "programming"
}


Think:

ARRAY
  ↓
$unwind
  ↓
ONE DOCUMENT PER ELEMENT


You do not need this immediately for your current project,
but it is an important aggregation stage.


============================================================
#16 $lookup
============================================================

$lookup is used to combine data from another collection.

It is similar to JOIN in SQL.


Example:

users collection:

{
    "_id": 1,
    "name": "Manish"
}


videos collection:

{
    "user_id": 1,
    "name": "Python"
}


$lookup can combine them.


Basic idea:

Collection A
      +
Collection B
      ↓
$lookup
      ↓
Combined result


This is useful when working with multiple collections.

You don't need to implement this in your current project
unless you create another collection such as users.


============================================================
#17 $count
============================================================

$count directly counts documents.

Example:

video_collection.aggregate([
    {
        "$match": {
            "time": {"$gt": 5}
        }
    },
    {
        "$count": "long_videos"
    }
])


Meaning:

Find videos > 5
then count them.


Result:

{
    "long_videos": 3
}


Compare:

$group + $sum: 1

and

$count


$count is simpler when you only need a count.


============================================================
#18 $set / $addFields
============================================================

Used to create a new field or modify fields.

Example:

{
    "$set": {
        "double_time": {
            "$multiply": ["$time", 2]
        }
    }
}


If:

time = 5

Then:

double_time = 10


Result:

{
    "name": "Python",
    "time": 5,
    "double_time": 10
}


Useful when you want to calculate a new value.


============================================================
#19 AGGREGATION EXPRESSIONS
============================================================

Inside aggregation we can perform calculations.

Common operators:

$add
$subtract
$multiply
$divide
$mod


Example:

{
    "$set": {
        "double_time": {
            "$multiply": ["$time", 2]
        }
    }
}


"$time"

means:

Get time from the current document.


============================================================
#20 PIPELINE ORDER
============================================================

The order of stages is extremely important.


Example:

[
    {"$match": ...},
    {"$sort": ...},
    {"$limit": ...}
]


means:

FILTER
  ↓
SORT
  ↓
LIMIT


Another example:

[
    {"$sort": ...},
    {"$limit": ...}
]


means:

SORT
  ↓
TOP N


General thinking:

1. Filter unnecessary data
2. Transform data
3. Group data
4. Sort data
5. Limit output
6. Select final fields


Not every pipeline needs all stages.


============================================================
#21 COMMON AGGREGATION PATTERNS
============================================================


PATTERN 1:

FILTER

[
    {"$match": {...}}
]


PATTERN 2:

FILTER + SORT

[
    {"$match": {...}},
    {"$sort": {...}}
]


PATTERN 3:

TOP N

[
    {"$sort": {"time": -1}},
    {"$limit": 5}
]


PATTERN 4:

STATISTICS

[
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1},
            "average": {"$avg": "$time"},
            "minimum": {"$min": "$time"},
            "maximum": {"$max": "$time"}
        }
    }
]


PATTERN 5:

FILTER + STATISTICS

[
    {"$match": {"time": {"$gt": 5}}},
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1},
            "average": {"$avg": "$time"}
        }
    }
]


PATTERN 6:

GROUP BY FIELD

[
    {
        "$group": {
            "_id": "$category",
            "count": {"$sum": 1}
        }
    }
]


============================================================
#22 find() vs aggregate()
============================================================

find():

Used mainly for retrieving documents.

Example:

video_collection.find({
    "time": {"$gt": 5}
})


aggregate():

Used for complex data processing.

Example:

video_collection.aggregate([
    {"$match": {"time": {"$gt": 5}}},
    {
        "$group": {
            "_id": None,
            "average": {"$avg": "$time"}
        }
    }
])


Simple rule:

find()
→ "Give me documents matching this condition."

aggregate()
→ "Process my data and give me a calculated/transformed result."


============================================================
#23 AGGREGATE RETURNS A CURSOR
============================================================

aggregate() returns a cursor.

Example:

result = video_collection.aggregate([
    ...
])


We can iterate:

for document in result:
    print(document)


This is exactly what you did in:

for stats in result:
    print(stats)


MongoDB sends the aggregation results through
the cursor.


============================================================
#24 IMPORTANT: FIELD TYPES MUST BE CONSISTENT
============================================================

Your "time" field should have the same type
for every document.

GOOD:

{
    "name": "Python",
    "time": 5
}

{
    "name": "Docker",
    "time": 4
}

{
    "name": "AWS",
    "time": 6
}


BAD:

{
    "name": "Python",
    "time": "5 min"
}

{
    "name": "Docker",
    "time": 4
}


Why?

Aggregation operations such as:

$sum
$avg
$min
$max

work best when the field has a consistent numeric type.


For your project:

Store time as an integer.

Example:

"time": 5


Not:

"time": "5 min"


Then display it as:

Time: 5 min


This keeps your database data clean and makes
queries and aggregation reliable.


============================================================
#25 YOUR PROJECT'S AGGREGATION FLOW
============================================================

Your function:

def video_statistics():

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


Flow:

MongoDB collection
       ↓
All video documents
       ↓
$group
       ↓
One group
       ↓
Calculate statistics
       ↓
Cursor
       ↓
for stats in result
       ↓
Print statistics


============================================================
#26 MOST IMPORTANT OPERATORS TO REMEMBER
============================================================

For your current level, remember these first:

$match
$group
$sum
$avg
$min
$max
$sort
$limit
$project
$count


Later learn:

$unwind
$lookup
$set
$addFields


You do NOT need to memorize every MongoDB aggregation
operator.


============================================================
#27 INTERVIEW MEMORY TRICK
============================================================

Think:

$match
→ FILTER

$group
→ GROUP / CALCULATE

$sum
→ TOTAL

$avg
→ AVERAGE

$min
→ SMALLEST

$max
→ LARGEST

$sort
→ ORDER

$limit
→ TOP N

$project
→ SELECT FIELDS

$skip
→ SKIP

$count
→ COUNT

$unwind
→ ARRAY → DOCUMENTS

$lookup
→ JOIN


============================================================
#28 MOST IMPORTANT PIPELINE TO REMEMBER
============================================================

FILTER → GROUP → SORT → LIMIT


Example:

video_collection.aggregate([
    {
        "$match": {
            "time": {"$gt": 3}
        }
    },
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1},
            "average_time": {"$avg": "$time"}
        }
    }
])


Meaning:

1. Filter videos > 3
2. Put them into one group
3. Count them
4. Calculate average time


============================================================
#29 REAL WORLD ANALOGY
============================================================

Imagine a YouTube database containing 10,000 videos.

You want:

"Find the 5 longest Python videos."

Pipeline:

$match
→ Find Python videos

$sort
→ Sort by time descending

$limit
→ Take first 5


Flow:

10,000 videos
      ↓
$match
      ↓
Python videos
      ↓
$sort
      ↓
Longest first
      ↓
$limit: 5
      ↓
Top 5 videos


This is the core idea of aggregation.


============================================================
#30 FINAL REVISION
============================================================

Aggregation Pipeline = DATA PROCESSING PIPELINE.

Syntax:

collection.aggregate([
    stage_1,
    stage_2,
    stage_3
])


Each stage processes the output of the previous stage.


Most important stages:

$match
→ filter documents

$group
→ group documents and calculate

$sort
→ sort documents

$limit
→ limit documents

$project
→ choose fields

$skip
→ skip documents

$count
→ count documents

$unwind
→ break array elements into documents

$lookup
→ combine collections


Important accumulators:

$sum
$avg
$min
$max


Most important concept:

PIPELINE ORDER MATTERS.


For example:

$match → $sort → $limit

means:

FILTER → SORT → TOP N


And:

$match → $group

means:

FILTER → CALCULATE STATISTICS


============================================================
#31 WHAT YOU NEED TO PRACTICE NOW
============================================================

For your current project, practice only these:

1. $match
2. $group
3. $sum
4. $avg
5. $min
6. $max
7. $sort
8. $limit
9. $project

Then create these functions:

find_top_3_longest_videos()

find_average_video_time()

find_total_video_time()

count_long_videos()

find_shortest_video()

find_longest_video()

These will make aggregation much stronger.

============================================================
'''
