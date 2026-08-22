# Python module from the standard library.
# json is used to store Python data in JSON format
# and read JSON data back into Python.
import json


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_data():
    """
    Load saved YouTube video data from the JSON file.

    If the file does not exist or contains invalid JSON,
    return an empty list so the application can start safely.
    """

    try:
        # "r" = read mode
        # encoding="utf-8" = properly handle text characters
        with open("youtube.txt", "r", encoding="utf-8") as file:

            # json.load() reads JSON data from the file
            # and converts it into Python objects.
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        # If the file does not exist or JSON is invalid,
        # start with an empty list.
        return []


# ---------------------------------------------------------
# SAVE DATA
# ---------------------------------------------------------

def save_data_helper(videos):
    """
    Save the current video list into the JSON file.
    """

    # "w" = write mode
    # It creates the file if it does not exist.
    # If the file exists, its old content is replaced.
    with open("youtube.txt", "w", encoding="utf-8") as file:

        # json.dump() converts Python data into JSON
        # and writes it directly into the file.
        #
        # indent=4 makes the JSON file easier for humans to read.
        json.dump(videos, file, indent=4)


# ---------------------------------------------------------
# LIST ALL VIDEOS
# ---------------------------------------------------------

def list_all_videos(videos):
    """
    Display all stored YouTube videos.
    """

    print("\n")
    print("-" * 70)

    # enumerate() gives us both:
    # index -> position of the video
    # video -> actual video dictionary
    #
    # start=1 makes the displayed numbering start from 1
    # because users normally count from 1.
    for index, video in enumerate(videos, start=1):

        print(
            f"{index}. {video['name']}, "
            f"Duration: {video['time']}"
        )

    print("-" * 70)


# ---------------------------------------------------------
# ADD VIDEO
# ---------------------------------------------------------

def add_video(videos):
    """
    Add a new video to the video list
    and save the updated list to the file.
    """

    # input() always returns a string.
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    # Add a new dictionary to the list.
    videos.append({
        "name": name,
        "time": time
    })

    # Save the updated list permanently.
    save_data_helper(videos)


# ---------------------------------------------------------
# UPDATE VIDEO
# ---------------------------------------------------------

def update_video(videos):
    """
    Update the details of an existing video.
    """

    # Show videos first so the user knows
    # which video number they want to update.
    list_all_videos(videos)

    try:
        # input() returns a string,
        # so convert it to int because we need a number.
        index = int(
            input("Enter the video number to update: ")
        )

    except ValueError:

        # Handles input such as:
        # abc, hello, 2.5, etc.
        print("Please enter a valid number.")
        return

    # User numbering starts from 1.
    # Python list indexing starts from 0.
    #
    # Therefore:
    # user enters 1 -> videos[0]
    # user enters 2 -> videos[1]
    #
    # This condition checks whether the entered
    # video number actually exists.
    if 1 <= index <= len(videos):

        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")

        # index - 1 converts user numbering
        # into Python's 0-based list index.
        videos[index - 1] = {
            "name": name,
            "time": time
        }

        # Save the updated data to the file.
        save_data_helper(videos)

    else:
        print("Invalid video number!")


# ---------------------------------------------------------
# DELETE VIDEO
# ---------------------------------------------------------

def delete_video(videos):
    """
    Delete a video from the list
    and save the updated list.
    """

    # Show videos so the user can choose one.
    list_all_videos(videos)

    try:
        # Convert user input from string to integer.
        index = int(
            input("Enter the video number to be deleted: ")
        )

    except ValueError:

        print("Please enter a valid number.")
        return

    # Validate that the video number exists.
    if 1 <= index <= len(videos):

        # Delete the selected video.
        #
        # Again, index - 1 converts the user's
        # 1-based number into Python's 0-based index.
        del videos[index - 1]

        # Save the updated list.
        save_data_helper(videos)

    else:
        print("Invalid video number!")


# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

# main() is the main entry point of the application.
# It controls the overall flow of the program.
def main():

    # Load existing videos when the application starts.
    videos = load_data()

    # Keep showing the menu until the user chooses Exit.
    while True:

        # Display the available options to the user.
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        try:
            # input() returns a string,
            # so convert it to an integer.
            choice = int(
                input("Enter your choice: ")
            )

        except ValueError:

            # Prevent the program from crashing
            # if the user enters non-numeric input.
            print("Please enter a valid number.")
            continue

        # match-case is useful when we have
        # multiple fixed choices.
        match choice:

            case 1:
                list_all_videos(videos)

            case 2:
                add_video(videos)

            case 3:
                update_video(videos)

            case 4:
                delete_video(videos)

            case 5:
                # break exits the while loop
                # and therefore exits the application.
                break

            case _:
                # "_" is the default case.
                # It runs when none of the above cases match.
                print("Invalid choice!")


# ---------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------

# __name__ is a special Python variable.
#
# When this file is executed directly:
#     __name__ == "__main__"
#
# When this file is imported into another Python file:
#     __name__ is the module's name.
#
# Therefore, main() runs only when this file
# is executed directly.
if __name__ == "__main__":
    main()


'''
============================================================
                 YOUTUBE MANAGER PROJECT
============================================================

WHAT IS THIS PROJECT?

This is a simple CRUD-style application for managing
YouTube videos.

CRUD means:

C -> Create
R -> Read
U -> Update
D -> Delete


------------------------------------------------------------
1. PROJECT FLOW
------------------------------------------------------------

Application starts
       |
       v
    load_data()
       |
       v
 Read JSON file
       |
       v
 Python list of dictionaries
       |
       v
    Show menu
       |
       +----> List videos
       |
       +----> Add video
       |
       +----> Update video
       |
       +----> Delete video
       |
       +----> Exit


------------------------------------------------------------
2. DATA STRUCTURE
------------------------------------------------------------

Videos are stored as:

[
    {
        "name": "Tum Hi Ho",
        "time": "5 min"
    },
    {
        "name": "Dhun",
        "time": "3 min"
    }
]


In Python:

videos = [
    {"name": "Tum Hi Ho", "time": "5 min"},
    {"name": "Dhun", "time": "3 min"}
]


So we are using:

List
  |
  +-- Dictionary
  |      |
  |      +-- name
  |      +-- time
  |
  +-- Dictionary
         |
         +-- name
         +-- time


------------------------------------------------------------
3. JSON
------------------------------------------------------------

JSON = JavaScript Object Notation.

It is a common format for storing and exchanging data.

Python:

json.dump()
    |
    v
Python object -> JSON file


json.load()
    |
    v
JSON file -> Python object


Important:

json.dump()
    -> writes JSON data to a file.

json.load()
    -> reads JSON data from a file.


------------------------------------------------------------
4. FILE HANDLING
------------------------------------------------------------

with open(...)

is used to safely work with files.

"r" -> read
"w" -> write / overwrite

encoding="utf-8"
    -> specifies how text should be encoded/decoded.


------------------------------------------------------------
5. WHY with open()?
------------------------------------------------------------

Instead of manually doing:

file = open(...)
...
file.close()


we prefer:

with open(...) as file:
    ...


Python automatically closes the file
when the with block finishes.

This is safer and cleaner.


------------------------------------------------------------
6. EXCEPTION HANDLING
------------------------------------------------------------

try:
    code that may fail

except:
    handle the error


Examples in this project:

FileNotFoundError
    -> file does not exist.

json.JSONDecodeError
    -> JSON file contains invalid JSON.

ValueError
    -> user entered something that cannot
       be converted to an integer.


Example:

index = int(input(...))


If user enters:

abc


Python raises:

ValueError


Instead of crashing the application,
we handle the error with try/except.


------------------------------------------------------------
7. enumerate()
------------------------------------------------------------

for index, video in enumerate(videos, start=1):

This gives:

index -> 1, 2, 3, ...
video -> actual dictionary


Without enumerate:

for i in range(len(videos)):
    video = videos[i]


With enumerate:

for index, video in enumerate(videos, start=1):

Cleaner and more Pythonic.


------------------------------------------------------------
8. 1-BASED vs 0-BASED INDEXING
------------------------------------------------------------

User sees:

1. Video A
2. Video B
3. Video C


Python list:

0 -> Video A
1 -> Video B
2 -> Video C


Therefore:

videos[index - 1]


If user enters 3:

videos[3 - 1]

videos[2]


So the third video is selected.


------------------------------------------------------------
9. match-case
------------------------------------------------------------

match choice:

    case 1:
        ...

    case 2:
        ...

    case 3:
        ...

    case _:
        ...


It is useful when we have multiple
fixed choices.

It is similar to switch statements
in many other programming languages.


------------------------------------------------------------
10. __name__ == "__main__"
------------------------------------------------------------

This:

if __name__ == "__main__":
    main()


is used to make sure main() runs only when
the file is executed directly.

Example:

python youtube_manager.py


Then:

__name__ == "__main__"

is True.


But if another Python file imports this module:

import youtube_manager


main() does not automatically run.


This is an important Python concept.


------------------------------------------------------------
11. WHY FUNCTIONS?
------------------------------------------------------------

Instead of putting everything inside main():

def load_data()
def save_data()
def list_all_videos()
def add_video()
def update_video()
def delete_video()


Each function has one main responsibility.

This makes code:

- easier to understand
- easier to test
- easier to maintain
- easier to modify
- easier to debug


This is the beginning of modular programming.


------------------------------------------------------------
12. PROJECT ARCHITECTURE RIGHT NOW
------------------------------------------------------------

main()
  |
  +-- load_data()
  |
  +-- list_all_videos()
  |
  +-- add_video()
  |      |
  |      +-- save_data_helper()
  |
  +-- update_video()
  |      |
  |      +-- save_data_helper()
  |
  +-- delete_video()
         |
         +-- save_data_helper()


This is already better than writing
everything in one huge block of code.


------------------------------------------------------------
13. WHAT THIS PROJECT TEACHES YOU
------------------------------------------------------------

Python Fundamentals
        |
        +-- Variables
        +-- Input / Output
        +-- Conditions
        +-- Loops
        +-- Functions
        +-- Lists
        +-- Dictionaries
        +-- enumerate()
        |
        v
Intermediate Python
        |
        +-- Modules
        +-- File Handling
        +-- JSON
        +-- Exception Handling
        +-- Context Managers
        +-- match-case
        +-- __name__
        |
        v
Project Development
        |
        +-- CRUD
        +-- Data persistence
        +-- Validation
        +-- Error handling
        +-- Separation of responsibilities


------------------------------------------------------------
14. HOW THIS RELATES TO REAL COMPANIES
------------------------------------------------------------

The exact YouTube Manager is a learning project,
but the concepts are used everywhere.

For example:

Real application
       |
       +-- Create data
       +-- Read data
       +-- Update data
       +-- Delete data


This same CRUD idea appears in:

- User management systems
- Product management
- Employee management
- Inventory systems
- Order management
- Banking applications
- Admin dashboards
- REST APIs
- Backend services


However, real production applications usually
do NOT use a JSON file as the main database.

Instead:

Application
     |
     v
Backend / API
     |
     v
Database
     |
     +-- PostgreSQL
     +-- MySQL
     +-- MongoDB
     +-- DynamoDB
     etc.


JSON is still extremely important because APIs
commonly exchange data using JSON.


------------------------------------------------------------
15. HOW THIS PROJECT CAN EVOLVE
------------------------------------------------------------

Level 1 - Current

CLI application
    +
JSON file
    +
CRUD


Level 2

Improve project structure:

youtube_manager/
|
├── main.py
├── services.py
├── storage.py
├── models.py
└── data/
    └── youtube.json


Level 3

Replace JSON file with a database:

Python
   |
   v
SQLAlchemy / database driver
   |
   v
PostgreSQL / MySQL


Level 4

Build a REST API:

Client
   |
   v
FastAPI
   |
   v
Service Layer
   |
   v
Database


Level 5

Production deployment:

Client
   |
   v
Load Balancer
   |
   v
FastAPI application
   |
   +------> PostgreSQL
   |
   +------> Redis
   |
   +------> Object Storage
   |
   +------> Logging / Monitoring


Then you start entering real
backend / cloud engineering territory.


------------------------------------------------------------
16. WHAT YOU SHOULD LEARN NEXT FROM THIS PROJECT
------------------------------------------------------------

When a new concept appears, learn it properly.

JSON
    -> load / dump
    -> serialization / deserialization

Exception Handling
    -> try
    -> except
    -> else
    -> finally
    -> custom exceptions

Context Managers
    -> with
    -> __enter__
    -> __exit__

Modules
    -> import
    -> from ... import
    -> packages

Python Entry Point
    -> __name__
    -> "__main__"

Project Structure
    -> modules
    -> packages
    -> separation of responsibilities

Then later:

Database
    -> SQL
    -> PostgreSQL / MySQL

API
    -> HTTP
    -> REST
    -> FastAPI

Testing
    -> pytest
    -> unit tests

Logging
    -> logging module

Configuration
    -> environment variables
    -> .env

Deployment
    -> Docker
    -> AWS

CI/CD
    -> GitHub Actions

This is how a small Python project can gradually
become a production-style application.


------------------------------------------------------------
17. IMPORTANT INTERVIEW QUESTIONS
------------------------------------------------------------

You should eventually be able to answer:

1. What is JSON?

2. Difference between json.load() and json.loads()?

3. Difference between json.dump() and json.dumps()?

4. Why use with open()?

5. What is a context manager?

6. Why do we use encoding="utf-8"?

7. What happens when FileNotFoundError occurs?

8. What is JSONDecodeError?

9. Why does input() require int() here?

10. Why do we use index - 1?

11. Why use enumerate()?

12. What does match-case do?

13. What is __name__?

14. Why do we use:
        if __name__ == "__main__":

15. Why separate code into functions?

16. What is CRUD?

17. Why is JSON not ideal as a production database?

18. How would you replace the JSON file with PostgreSQL?

19. How would you expose this application as a REST API?

20. How would you deploy this application using Docker
    and AWS?


------------------------------------------------------------
FINAL MENTAL MODEL
------------------------------------------------------------

User
 ↓
main()
 ↓
Choose operation
 ↓
CRUD function
 ↓
Python data structure
 ↓
JSON file
 ↓
Persistent data


Later:

User
 ↓
API
 ↓
Python backend
 ↓
Service layer
 ↓
Database
 ↓
Persistent data


The current project is NOT supposed to be a
production application.

Its purpose is to teach you how Python concepts
work together inside a real application.

Once you understand every line of this project,
you should be able to explain both:

"How does this code work?"

AND

"How would I scale this idea into a real application?"
============================================================
'''