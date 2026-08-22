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