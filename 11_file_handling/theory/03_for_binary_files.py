'''
              BINARY FILES
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
         rb        wb       ab
       read       write    append
          │        │        │
          └────────┼────────┘
                   ↓
                 bytes
                   │
          ┌────────┴────────┐
          ↓                 ↓
      small files       large files
       read()          chunks


important commands:
# Read binary
with open("image.jpg", "rb") as file:
    data = file.read()

# Write binary
with open("copy.jpg", "wb") as file:
    file.write(data)

# Append binary
with open("data.bin", "ab") as file:
    file.write(b"new data")

# Pointer
file.tell()
file.seek(0)

# Large files
file.read(1024)     
'''


'''
BINARY FILE HANDLING
====================

1. WHAT IS A BINARY FILE?
==========================

A binary file stores data as raw bytes rather than normal
human-readable text.

Common binary files:

    .jpg   → Images
    .png   → Images
    .pdf   → Documents
    .mp3   → Audio
    .mp4   → Video
    .zip   → Compressed files
    .exe   → Executable files

Simple idea:

    Text file
        ↓
    Characters / text
        ↓
    str

    Binary file
        ↓
    Raw bytes
        ↓
    bytes


2. WHY DO WE USE BINARY MODE?
=============================

Normal text mode tells Python:

    "Treat this file as text."

Binary mode tells Python:

    "Treat this file as raw bytes."

Example:

    Text:
        open("data.txt", "r", encoding="utf-8")

    Binary:
        open("image.jpg", "rb")

Here:

    r → read
    b → binary

Therefore:

    rb = read binary


3. BINARY FILE MODES
====================

The normal file modes can be combined with "b".

    rb  → Read binary
    wb  → Write binary
    ab  → Append binary

Other combinations:

    rb+ → Read + write binary
    wb+ → Write + read binary
    ab+ → Append + read binary

Most important for now:

    rb
    wb
    ab


4. rb — READ BINARY
====================

Use "rb" when you want to read a binary file.

Example:

    with open("image.jpg", "rb") as file:
        data = file.read()

    print(type(data))

Output:

    <class 'bytes'>

WHY?

Because binary data is represented by Python using
the "bytes" data type.

Use "rb" when:

    → Reading an image
    → Reading a PDF
    → Reading a video
    → Reading an audio file
    → Reading any other binary file


5. wb — WRITE BINARY
====================

Use "wb" when you want to write binary data to a file.

Example:

    data = b"Hello Python"

    with open("data.bin", "wb") as file:
        file.write(data)

Here:

    b"Hello Python"

is a bytes object.

IMPORTANT:

"wb" behaves like "w".

If the file already exists:

    old content
        ↓
       wb
        ↓
    old content is overwritten


6. ab — APPEND BINARY
=====================

Use "ab" when you want to add binary data
to the end of an existing binary file.

Example:

    with open("data.bin", "ab") as file:
        file.write(b"New data")

Existing data remains.

    Old data
       +
    New data


7. STR VS BYTES
===============

Normal text:

    text = "Hello"

    type(text)

Result:

    str


Binary:

    data = b"Hello"

    type(data)

Result:

    bytes


Remember:

    str   → Text
    bytes → Binary data


8. WHAT DOES b"Hello" MEAN?
===========================

The "b" before the string means that Python should
represent it as bytes.

Example:

    text = "Hello"
    binary = b"Hello"

    print(type(text))
    print(type(binary))

Output:

    <class 'str'>
    <class 'bytes'>


9. WHY DON'T WE USE encoding="utf-8" IN BINARY MODE?
=====================================================

For text files:

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

Encoding is used when Python needs to interpret
bytes as text characters.

But binary mode works directly with bytes.

Therefore:

    with open("image.jpg", "rb") as file:
        data = file.read()

We normally do NOT use:

    encoding="utf-8"

with binary mode.

Mental model:

    TEXT

    File
      ↓
    bytes
      ↓
    encoding
      ↓
    str


    BINARY

    File
      ↓
    bytes


10. EXAMPLE — READING AN IMAGE
==============================

    with open("photo.jpg", "rb") as file:
        data = file.read()

    print(type(data))
    print(len(data))

Output might be:

    <class 'bytes'>
    250000

The "250000" means approximately 250,000 bytes
were read from the file.

WHERE IS THIS USED?

    → File uploads
    → Image processing
    → File transfer
    → Storage systems
    → APIs
    → Cloud applications


11. EXAMPLE — COPYING AN IMAGE ⭐
=================================

Suppose we have:

    photo.jpg

and want:

    photo_copy.jpg

Code:

    with open("photo.jpg", "rb") as source:
        data = source.read()

    with open("photo_copy.jpg", "wb") as destination:
        destination.write(data)

WORKFLOW:

    photo.jpg
       ↓
      rb
       ↓
     bytes
       ↓
      wb
       ↓
    photo_copy.jpg

WHY?

Because we are reading the original file as bytes
and writing exactly those bytes into another file.

This preserves the binary data.


12. WHY "rb" AND "wb" ARE IMPORTANT FOR FILE COPYING
=====================================================

For an image, don't do:

    open("photo.jpg", "r")

because you're asking Python to treat binary data
as text.

Instead:

    open("photo.jpg", "rb")

Similarly, when creating the copy:

    open("photo_copy.jpg", "wb")

So:

    Source → rb
    Destination → wb


13. FILE POINTER ALSO WORKS WITH BINARY FILES
==============================================

Binary files also have a file pointer.

    tell()
        → tells the current position

    seek()
        → moves the current position


Example:

    with open("photo.jpg", "rb") as file:

        print(file.tell())

        data = file.read(10)

        print(file.tell())

        file.seek(0)

        print(file.tell())


Concept:

    File:
    ┌─────────────────────────────┐
    │ binary data                 │
    └─────────────────────────────┘
      ↑
      pointer

    tell()
      ↓
    "Where am I?"

    seek(0)
      ↓
    "Move to the beginning."


14. WHY WOULD WE USE seek() WITH BINARY FILES?
===============================================

Suppose:

    with open("data.bin", "rb") as file:

        first = file.read(10)

        file.seek(0)

        again = file.read(10)

First read:

    bytes 0 → 9

Then:

    seek(0)

moves the pointer back to:

    byte 0

Then the next read starts again from byte 0.


15. READING LARGE BINARY FILES ⭐⭐⭐
====================================

Suppose:

    movie.mp4 = 10 GB

Don't always do:

    with open("movie.mp4", "rb") as file:
        data = file.read()

Why?

Because Python may try to load the entire file
into RAM.

Instead, read the file in chunks.

Example:

    with open("movie.mp4", "rb") as file:

        while True:

            chunk = file.read(1024)

            if not chunk:
                break

            # Process the chunk


Here:

    1024 = 1024 bytes

Instead of:

    10 GB
      ↓
    RAM


we do:

    1024 bytes
        ↓
    process
        ↓
    1024 bytes
        ↓
    process
        ↓
       ...


16. WHY CHUNK PROCESSING?
=========================

Imagine:

    File = 20 GB
    RAM  = 8 GB

Reading everything:

    file.read()
        ↓
    potentially huge memory usage


Chunk processing:

    1 MB
      ↓
    process
      ↓
    1 MB
      ↓
    process
      ↓
    1 MB
      ↓
      ...


This keeps memory usage much lower.

WHERE IS THIS USED?

    → Large videos
    → Large images
    → Large PDFs
    → File uploads
    → File downloads
    → Cloud storage
    → Data processing


17. PRACTICAL EXAMPLE — LARGE FILE COPY
========================================

    with open("large_video.mp4", "rb") as source:

        with open("copy.mp4", "wb") as destination:

            while True:

                chunk = source.read(1024 * 1024)

                if not chunk:
                    break

                destination.write(chunk)


Here:

    1024 * 1024 ≈ 1 MB

So the program does:

    Read 1 MB
        ↓
    Write 1 MB
        ↓
    Read 1 MB
        ↓
    Write 1 MB
        ↓
       ...


18. with open() IS STILL PREFERRED
==================================

Binary files should also use:

    with open(...)

Example:

    with open("image.jpg", "rb") as file:
        data = file.read()

WHY?

Because Python automatically closes the file
when the "with" block finishes.

Therefore:

    with open()
        ↓
    work with file
        ↓
    automatically close


19. BINARY FILE + EXCEPTION HANDLING
====================================

Binary files can also produce errors.

For example, if the file doesn't exist:

    FileNotFoundError

Example:

    try:

        with open("photo.jpg", "rb") as file:
            data = file.read()

    except FileNotFoundError:

        print("Image not found")


20. TEXT VS BINARY — FINAL COMPARISON
=====================================

    TEXT FILE

    open("data.txt", "r", encoding="utf-8")
                ↓
              str


    BINARY FILE

    open("image.jpg", "rb")
                ↓
              bytes


Important difference:

    Text → characters / str
    Binary → bytes


21. MOST COMMON BINARY OPERATIONS
=================================

READ:

    with open("image.jpg", "rb") as file:
        data = file.read()


WRITE:

    with open("data.bin", "wb") as file:
        file.write(b"Hello")


APPEND:

    with open("data.bin", "ab") as file:
        file.write(b"New data")


COPY:

    with open("image.jpg", "rb") as source:
        data = source.read()

    with open("copy.jpg", "wb") as destination:
        destination.write(data)


LARGE FILE:

    with open("large.mp4", "rb") as file:

        while True:

            chunk = file.read(1024 * 1024)

            if not chunk:
                break

            # process chunk


22. IMPORTANT RULES TO REMEMBER
===============================

    rb = Read Binary
    wb = Write Binary
    ab = Append Binary

    Binary data = bytes

    b"Hello" = bytes

    Binary mode normally does not use encoding="utf-8"

    with open() = preferred way

    tell() = current pointer position

    seek() = move pointer

    read() = read data

    Large files = process in chunks


23. FINAL MENTAL MODEL
======================

                    BINARY FILE
                         │
                         ↓
                       bytes
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
             rb         wb         ab
           Read        Write      Append
              │          │          │
              └──────────┼──────────┘
                         ↓
                    with open()
                         │
                         ↓
                    Safe handling


24. ONE-LINE MEMORY TRICK
=========================

    rb = Read Binary
    wb = Write Binary
    ab = Append Binary

    str   = text
    bytes = binary

    seek() = move pointer
    tell() = check pointer

    read() = read data
    write() = write data

    Large file → read in chunks


BINARY FILE HANDLING =

    Python
       ↓
    read/write
       ↓
    raw bytes
       ↓
    images / PDFs / videos / audio / other binary files
'''