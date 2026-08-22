'''
FILE HANDLING
==============
- File handling allows a program to communicate with data stored in files.

- File handling means using Python to create, open, read, write, modify, and manage files stored on a computer's storage.

- File handling means using Python to work with files:
create, open, read, write, update, and manage files.

File handling = Python ↔ Files on your computer

Simple flow:

    File
      ↓
    open()
      ↓
    read / write
      ↓
    close()


1. OPENING A FILE
=================

Syntax:

    open("filename", "mode")

Example:

    file = open("data.txt", "r")

Preferred way:

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

"with" automatically closes the file.


2. FILE MODES
=============

r  → Read
     File must exist.

w  → Write
     Creates file if it does not exist.
     Overwrites existing content.

a  → Append
     Adds new content at the end.

x  → Create
     Creates a new file.
     Gives an error if the file already exists.

r+ → Read + Write
w+ → Read + Write + overwrite existing content
a+ → Read + Append

Easy memory:

    r → read
    w → write / overwrite
    a → add at the end
    x → create new


3. READING A FILE
=================

read()
    → Reads the entire file.

readline()
    → Reads one line.

readlines()
    → Reads all lines and returns a list.

Example:

    with open("data.txt", "r") as file:
        data = file.read()


4. WRITING TO A FILE
====================

write()
    → Writes a string to the file.

    file.write("Hello Python")

writelines()
    → Writes multiple strings.

    file.writelines(["Python\n", "DSA\n"])

Important:
writelines() does NOT automatically add "\n".


5. with open() ⭐
=================

Preferred way to work with files.

    with open("data.txt", "r") as file:
        data = file.read()

The file is automatically closed after the
"with" block finishes.

This is called a Context Manager.


6. close()
===========

close() releases the file resource.

Manual way:

    file = open("data.txt", "r")
    data = file.read()
    file.close()

With "with open()", closing happens automatically.


7. FILE PATHS
=============

Relative path:

    open("data.txt")

Means the path is relative to the
current working directory.

Absolute path:

    open("/Users/name/project/data.txt")

Gives the complete location of the file.


8. ENCODING
===========

Use UTF-8 for normal text files:

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

UTF-8 helps Python correctly handle
different characters and languages.


9. FILE POINTER
===============

Python keeps track of its current position
inside a file.

tell()
    → Tells the current position.

seek()
    → Moves the file pointer.

Example:

    file.tell()
    file.seek(0)

Easy memory:

    tell() → Where am I?
    seek() → Go to this position.


10. TEXT VS BINARY FILES
========================

Text file:

    open("data.txt", "r")

Binary file:

    open("image.jpg", "rb")

"b" means Binary.

Binary mode is commonly used for:

    Images
    PDFs
    Audio
    Video


11. pathlib ⭐
==============

pathlib provides a modern way to work
with file and directory paths.

    from pathlib import Path

    path = Path("data.txt")

Check if path exists:

    path.exists()

Check if it is a file:

    path.is_file()

Check if it is a directory:

    path.is_dir()

Read text:

    path.read_text(encoding="utf-8")

Write text:

    path.write_text("Hello", encoding="utf-8")


12. FILE HANDLING + EXCEPTIONS
==============================

Files can cause errors.

Common errors:

FileNotFoundError
    → File does not exist.

PermissionError
    → Program does not have permission.

Example:

    try:
        with open("data.txt", "r") as file:
            data = file.read()

    except FileNotFoundError:
        print("File not found")


==================================================
INTERVIEW / PROJECT QUICK RECALL
==================================================

Need to read?
    → "r"

Need to overwrite/write?
    → "w"

Need to add at the end?
    → "a"

Need to create a new file?
    → "x"

Need to read everything?
    → read()

Need one line?
    → readline()

Need all lines as a list?
    → readlines()

Need to write?
    → write()

Need multiple strings?
    → writelines()

Need automatic closing?
    → with open()

Need current file position?
    → tell()

Need to move file position?
    → seek()

Need to work with paths?
    → pathlib

Need to handle file errors?
    → try / except


MOST IMPORTANT TEMPLATE
=======================

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()


FINAL MENTAL MODEL
==================

    OPEN
      ↓
    READ / WRITE
      ↓
    AUTOMATICALLY CLOSE


MOST IMPORTANT THINGS TO REMEMBER

    r = read
    w = write / overwrite
    a = append
    x = create
    with open() = preferred way
    tell() = current position
    seek() = move position
    pathlib = work with paths
    try/except = handle file errors


File handling means:
How can my Python program safely work with
data stored in files?
'''