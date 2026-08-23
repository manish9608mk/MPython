'''
JSON IN PYTHON

JSON = JavaScript Object Notation.

JSON is a common text format used to:
- store structured data
- exchange data between applications
- send/receive data through APIs
- store configuration data
- store application data in .json files

Example JSON:

{
    "name": "Manish",
    "age": 23,
    "skills": ["Python", "AWS", "Docker"],
    "is_student": true
}


WHY IS JSON IMPORTANT?

Python programs often need to communicate with:
- REST APIs
- Web applications
- Cloud services
- Databases
- Other programs

JSON is one of the most common formats used for this communication.


PYTHON ↔ JSON

Python object                 JSON
------------                  ----
dict              ↔          object
list              ↔          array
str               ↔          string
int / float       ↔          number
True              ↔          true
False             ↔          false
None              ↔          null


IMPORTANT JSON FUNCTIONS:

json.dumps()
    Python object → JSON string

json.loads()
    JSON string → Python object

json.dump()
    Python object → JSON file

json.load()
    JSON file → Python object


MENTAL MODEL:

Python object
      |
      | dumps()
      ↓
 JSON string
      |
      | loads()
      ↓
Python object


Python object
      |
      | dump()
      ↓
 JSON file
      |
      | load()
      ↓
Python object


INTERVIEW MEMORY:

s = string
f = file

dumps  → Python → string
loads  → string → Python

dump   → Python → file
load   → file → Python


JSON IS NOT A PYTHON DATA TYPE.

Python has:
- dict
- list
- str
- int
- float
- bool
- None

JSON is a data format.

Python's json module helps convert
between Python objects and JSON.



                    JSON
                      │
             ┌────────┴────────┐
             │                 │
          STRING              FILE
             │                 │
         loads()             load()
             ↓                 ↓
          Python             Python


          Python
             │
       ┌─────┴─────┐
       │           │
    dumps()       dump()
       ↓           ↓
 JSON STRING    JSON FILE
'''


'''
Just remember this table:
| Function  | Direction                | Use when      |
| --------- | ------------------------ | --------------|
| dumps() | Python → JSON string | API/network/string  |
| loads() | JSON string → Python | API response/string |
| dump()  | Python → JSON file   | Save data           |
| load()  | JSON file → Python   | Read data           |


Most important distinction:

dump/load → file
dumps/loads → string


'''

'''
WHEN TO USE dump, dumps, load, loads
====================================

1. dumps()
-----------

Python object → JSON string

Use when:
- You want JSON data in memory as a string.
- You need to send JSON data through an API/network.
- You want to convert a Python object into JSON text.

Example:

data = {"name": "Manish"}

json_string = json.dumps(data)

# json_string is a string


2. loads()
-----------

JSON string → Python object

Use when:
- You already have JSON data as a string.
- You received JSON from an API/network.
- You want to convert JSON text into a Python object.

Example:

json_string = '{"name": "Manish"}'

data = json.loads(json_string)

# data is a Python dictionary


3. dump()
----------

Python object → JSON file

Use when:
- You want to permanently save Python data
  into a .json file.

Example:

data = {"name": "Manish"}

with open("data.json", "w") as file:
    json.dump(data, file)


4. load()
----------

JSON file → Python object

Use when:
- You already have a .json file.
- You want to read the JSON file
  and use its data in Python.

Example:

with open("data.json", "r") as file:
    data = json.load(file)


EASY MEMORY TRICK
=================

             STRING        FILE

Python →     dumps()       dump()
              ↓              ↓
             JSON           JSON
             string         file

JSON →       loads()       load()
              ↓              ↓
            Python         Python


REMEMBER:

dumps  → Python → JSON STRING
loads  → JSON STRING → Python

dump   → Python → JSON FILE
load   → JSON FILE → Python


REAL-WORLD EXAMPLES
===================

API response:
JSON string → Python
       ↓
    loads()


API request:
Python → JSON string
       ↓
    dumps()


Save application data:
Python → JSON file
       ↓
     dump()


Read saved data:
JSON file → Python
       ↓
     load()


ONE-LINE INTERVIEW RULE
=======================

"s" means STRING.

dump  = Python → file
load  = file → Python

dumps = Python → string
loads = string → Python
'''