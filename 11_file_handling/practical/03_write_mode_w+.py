# mode: w+ (write plus read)

with open("write_plus_read.txt", 'w+', encoding="utf-8") as file:

  file.write(" Hello नमस्ते ") # Write data into the file
  file.seek(0) # Move file pointer back to the beginning
  read = file.read() # Read the data

  print(read)

'''
write()
   ↓
pointer moves forward
   ↓
read()
   ↓
reads from CURRENT pointer
'''
