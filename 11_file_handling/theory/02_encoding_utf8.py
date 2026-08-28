'''
ENCODING = "UTF-8"
===================

What is encoding?
-----------------

Encoding is the process of converting characters/text into
bytes so that computers can store or transmit them.

Decoding is the reverse:

    Text
      ↓
   Encoding
      ↓
    Bytes

    Bytes
      ↓
   Decoding
      ↓
    Text


UTF-8
=====

UTF-8 is a standard character encoding used to represent text.

It supports a very large range of characters, including:

    English
    Numbers
    Symbols
    Hindi
    Chinese
    Japanese
    Emojis
    etc.


Why use encoding="utf-8"?
=========================

When working with text files, explicitly specifying UTF-8
helps Python correctly encode and decode text.

Example:

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Hello नमस्ते 😊")


Reading:

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()


Without the correct encoding, Python may produce an error
such as:

    UnicodeDecodeError

or text may be displayed incorrectly.


Encoding in File Handling
==========================

Writing:

    Python text
         ↓
    UTF-8 encoding
         ↓
       Bytes
         ↓
       File


Reading:

       File
         ↓
       Bytes
         ↓
    UTF-8 decoding
         ↓
    Python text


Important
=========

For normal text files, use:

    encoding="utf-8"

Example:

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()


    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Hello Python")


Easy Memory Trick
=================

    Encoding → Text → Bytes

    Decoding → Bytes → Text

    UTF-8 → Standard text encoding


One-Line Definition
===================

encoding="utf-8" tells Python to use UTF-8 to correctly
convert between text (characters) and bytes when reading
or writing a text file.
'''