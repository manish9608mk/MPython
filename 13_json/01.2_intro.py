'''
============================================================
                    JSON IN PYTHON
============================================================


1. WHAT IS JSON?
------------------------------------------------------------

JSON = JavaScript Object Notation.

JSON is a standard text/data format used to:

    - Store structured data
    - Exchange data between applications
    - Communicate with APIs
    - Store configuration
    - Save application data

JSON is very common in:

    - REST APIs
    - Web applications
    - Cloud applications
    - Configuration files
    - Data exchange
    - Application data


IMPORTANT:

JSON is NOT a Python dictionary.

JSON = Data format
dict = Python data structure


Example JSON:

{
    "name": "Manish",
    "age": 23,
    "skills": ["Python", "AWS"]
}


------------------------------------------------------------
2. IMPORT JSON
------------------------------------------------------------

Python provides a built-in json module.

No installation is required.

'''

import json

'''
------------------------------------------------------------
3. JSON ↔ PYTHON
------------------------------------------------------------

The most important thing to understand:

Python object
      ↕
     JSON

There are 4 core functions:

    json.dumps()
    json.loads()
    json.dump()
    json.load()


------------------------------------------------------------
4. json.dumps()
------------------------------------------------------------

Python object → JSON STRING

"dumps" contains "s"
"s" = String

Use dumps() when you want to convert
Python data into a JSON string.

Example:
'''

data = {
    "name": "Manish",
    "age": 23,
    "skills": ["Python", "AWS"]
}

json_data = json.dumps(data)

print(json_data)

'''
Output:

{"name": "Manish", "age": 23, "skills": ["Python", "AWS"]}


IMPORTANT:

dumps() = Python → JSON STRING


Mental model:

Python object
      ↓
   dumps()
      ↓
JSON string


------------------------------------------------------------
5. json.loads()
------------------------------------------------------------

JSON STRING → Python object

"loads" contains "s"
"s" = String

Use loads() when you have JSON data
as a string and want to convert it
into a Python object.

Example:
'''

json_data = '{"name": "Manish", "age": 23}'

data = json.loads(json_data)

print(data)
print(data["name"])
print(data["age"])

'''
Output:

{'name': 'Manish', 'age': 23}
Manish
23


IMPORTANT:

loads() = JSON STRING → Python


Mental model:

JSON string
      ↓
   loads()
      ↓
Python object


------------------------------------------------------------
6. json.dump()
------------------------------------------------------------

Python object → JSON FILE

Use dump() when you want to write
Python data directly into a JSON file.

Example:
'''

data = {
    "name": "Manish",
    "age": 23,
    "skills": ["Python", "AWS"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

'''
user.json:

{
    "name": "Manish",
    "age": 23,
    "skills": [
        "Python",
        "AWS"
    ]
}


IMPORTANT:

dump() = Python → JSON FILE


Mental model:

Python object
      ↓
    dump()
      ↓
JSON file


------------------------------------------------------------
7. json.load()
------------------------------------------------------------

JSON FILE → Python object

Use load() when you want to read
JSON data directly from a file.

Example:
'''

with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(data["name"])

'''
Output:

{'name': 'Manish', 'age': 23, 'skills': ['Python', 'AWS']}
Manish


IMPORTANT:

load() = JSON FILE → Python


Mental model:

JSON file
      ↓
    load()
      ↓
Python object


------------------------------------------------------------
8. THE MOST IMPORTANT DIFFERENCE
------------------------------------------------------------

                    JSON
                      |
              ----------------
              |              |
           STRING           FILE
              |              |
           loads()          load()
              ↓              ↓
           Python          Python


                    Python
                      |
              ----------------
              |              |
           dumps()          dump()
              ↓              ↓
        JSON string      JSON file


Remember:

dumps() → Python → JSON STRING
loads() → JSON STRING → Python

dump()  → Python → JSON FILE
load()  → JSON FILE → Python


EASY MEMORY TRICK:

"s" = String

loads()  → String → Python
dumps()  → Python → String

No "s" = File

load()   → File → Python
dump()   → Python → File


------------------------------------------------------------
9. JSON AND PYTHON DATA TYPES
------------------------------------------------------------

Common mapping:

Python              JSON

dict          →     object
list          →     array
str           →     string
int           →     number
float         →     number
True          →     true
False         →     false
None          →     null


Example:

Python:

{
    "active": True,
    "data": None
}


JSON:

{
    "active": true,
    "data": null
}


------------------------------------------------------------
10. indent
------------------------------------------------------------

indent is used to make JSON easier
for humans to read.

Example:
'''

data = {
    "name": "Manish",
    "age": 23,
    "city": "Bhopal"
}

print(json.dumps(data, indent=4))

'''
Output:

{
    "name": "Manish",
    "age": 23,
    "city": "Bhopal"
}


Without indent:

{"name": "Manish", "age": 23, "city": "Bhopal"}

With indent=4:

{
    "name": "Manish",
    "age": 23,
    "city": "Bhopal"
}


------------------------------------------------------------
11. JSON + FILE HANDLING
------------------------------------------------------------

JSON is commonly used together
with Python file handling.

READ JSON FILE:

'''

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

'''
JSON file
    ↓
open()
    ↓
json.load()
    ↓
Python dictionary/list


WRITE JSON FILE:

'''

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

'''
Python dictionary/list
    ↓
json.dump()
    ↓
JSON file


IMPORTANT:

with open() is preferred because
the file is automatically closed.


------------------------------------------------------------
12. JSON + APIs
------------------------------------------------------------

This is VERY important in real projects.

APIs commonly send and receive JSON data.

Typical flow:

        API
         ↓
    JSON response
         ↓
      Python
         ↓
    dict / list
         ↓
    Process data


Example API JSON:

{
    "id": 101,
    "name": "Manish",
    "skills": ["Python", "AWS"]
}


After converting it into Python:

data["name"]

Output:

Manish


data["skills"]

Output:

["Python", "AWS"]


So when working with APIs,
you will frequently:

    1. Receive JSON
    2. Convert/process it
    3. Access dictionary/list values
    4. Send JSON back if required


------------------------------------------------------------
13. JSON + CONFIGURATION FILES
------------------------------------------------------------

JSON can also store application configuration.

Example:

config.json

{
    "database": "production",
    "debug": false,
    "timeout": 30
}


Python:

'''

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(config["timeout"])

'''
Output:

30


------------------------------------------------------------
14. JSON ERRORS
------------------------------------------------------------

Invalid JSON can cause:

    json.JSONDecodeError

Example:

'''

try:
    data = json.loads('{"name": "Manish"')
except json.JSONDecodeError:
    print("Invalid JSON")

'''
Output:

Invalid JSON


IMPORTANT:

When processing JSON from external sources,
API responses, or files, invalid/malformed JSON
can occur.

So JSON can be combined with error handling.


------------------------------------------------------------
15. NESTED JSON
------------------------------------------------------------

JSON can contain nested objects and arrays.

Example:

'''

data = {
    "user": {
        "name": "Manish",
        "skills": ["Python", "AWS"]
    }
}

print(data["user"]["name"])
print(data["user"]["skills"][0])

'''
Output:

Manish
Python


IMPORTANT:

For interviews, you should be comfortable
reading and accessing nested dictionaries/lists.

Typical pattern:

data["key"]["nested_key"]

or:

data["key"][index]


------------------------------------------------------------
16. REAL-WORLD JSON FLOW
------------------------------------------------------------

A very common real-world flow is:

        External System / API
                  ↓
                 JSON
                  ↓
          json.loads() / API
                  ↓
            Python dict/list
                  ↓
             Process data
                  ↓
          Python dict/list
                  ↓
             json.dumps()
                  ↓
                 JSON
                  ↓
        External System / API


For files:

        JSON file
             ↓
        json.load()
             ↓
        Python object
             ↓
        Process / modify
             ↓
        json.dump()
             ↓
        JSON file


------------------------------------------------------------
17. WHAT YOU MUST REMEMBER
------------------------------------------------------------

ABSOLUTE CORE:

    json.loads()
    json.dumps()
    json.load()
    json.dump()


Remember this table:

------------------------------------------------------------
Function       Conversion
------------------------------------------------------------

loads()        JSON STRING → Python

dumps()        Python → JSON STRING

load()         JSON FILE → Python

dump()         Python → JSON FILE

------------------------------------------------------------


EASY MEMORY:

             "S" = STRING

loads()  → STRING → Python
dumps()  → Python → STRING


             NO "S" = FILE

load()   → FILE → Python
dump()   → Python → FILE


------------------------------------------------------------
18. INTERVIEW CHECKLIST
------------------------------------------------------------

You should be comfortable with:

✓ What is JSON?
✓ Why is JSON used?
✓ import json
✓ json.loads()
✓ json.dumps()
✓ json.load()
✓ json.dump()
✓ JSON ↔ Python conversion
✓ JSON + file handling
✓ indent
✓ encoding="utf-8"
✓ JSON + APIs
✓ Nested JSON
✓ JSONDecodeError
✓ Reading and processing JSON data


------------------------------------------------------------
19. FAANG / PROJECT LEVEL MENTAL MODEL
------------------------------------------------------------

Don't try to memorize everything.

Remember:

                JSON
                  |
        ---------------------
        |                   |
      STRING              FILE
        |                   |
     loads()              load()
        ↓                   ↓
      Python              Python


      Python
        |
   ----------------
   |              |
 dumps()         dump()
   ↓              ↓
JSON string    JSON file


The main skill is:

READ JSON
    ↓
UNDERSTAND STRUCTURE
    ↓
CONVERT TO PYTHON
    ↓
ACCESS / PROCESS DATA


And:

CREATE PYTHON DATA
    ↓
CONVERT TO JSON
    ↓
STORE / SEND DATA


============================================================
                    FINAL REVISION
============================================================

JSON = standard data format.

Python dict ≠ JSON.

4 CORE FUNCTIONS:

    loads() → JSON string → Python
    dumps() → Python → JSON string

    load()  → JSON file → Python
    dump()  → Python → JSON file


"s" = String
No "s" = File


JSON is heavily used with:

    APIs
    Files
    Configuration
    Web applications
    Cloud applications
    Data exchange


For interviews:

The most important thing is understanding
the 4 functions and knowing how to read,
convert, access, and process JSON data.

============================================================
'''