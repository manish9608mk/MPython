# problem: read a text file and count the number of words
# text file name: count.txt

with open("count.txt", 'r', encoding="utf-8") as file:
  read_file = file.read().split(' ')
  print(read_file)

  print("Word count: ", len(read_file))


# steps:
# 1. Read complete file data
# 2. Split data into individual words
# 3. Count words using len()

'''
File
 ↓
read()
 ↓
split()
 ↓
len()
 ↓
Word Count
'''

