'''
WHY FILE HANDLING?

File handling means working with files using Python.

We use it when our program needs to:

1. Read data from a file
   Example: read a .txt, .csv, or log file.

2. Write data to a file
   Example: save user data, results, or logs.

3. Add new data without deleting old data
   Example: append new log entries.

4. Create files
   Example: generate a report file.

5. Process large amounts of data
   Example: read a log file line by line.

6. Store data permanently
   Variables disappear when the program stops,
   but data saved in a file remains.

7. Work with real-world application data
   Example:
   - configuration files
   - logs
   - CSV files
   - JSON files
   - reports
   - text files

Simple mental model:

Program
   |
   |---- Read  ------> File
   |
   |---- Write -----> File
   |
   |---- Append ----> File

IMPORTANT:

File Handling = How we work with files.

Error Handling = How we safely handle problems
                 that may happen while working with files.

Example problems:
- File does not exist
- No permission to access file
- Invalid file path
- Disk/storage problem

So they are different topics,
but they are commonly used together.
'''


# Example 1: try/finally
# Error handling: try, except, finally

file = open("youtube.txt", "w", encoding="utf-8")

try:
    file.write("Using try and finally")
finally:
    file.close()


# Example 2: File handling: with open()
# And for normal file operations, prefer:
with open("youtube.txt", "w", encoding="utf-8") as file:
  file.write("Hello")
# because Python automatically closes the file when the with block ends.
# with open() = preferred way to work with files, because it automatically closes the file after use.



'''
IMPORTANT INTERVIEW POINTS:

open()       → opens a file
"r"          → read
"w"          → write / overwrite
"a"          → append
"x"          → create new file

read()       → read content
write()      → write content

with open()  → automatically closes the file
               and is the preferred approach.

encoding="utf-8" → handles text encoding correctly.

try/except/finally → handles errors and cleanup.

File Handling ≠ Error Handling

File Handling → working with files
Error Handling → handling problems safely
'''