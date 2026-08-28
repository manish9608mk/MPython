# File handling practice


#ex1 without 'with' ismein close() karna parta hai 
file = open("basic.txt",'w')

file.write("Welcome to the universe \n")
file.write("Hello world \n")

file.writelines(['Mango \n', 'Apple \n', 'Banana \n', 'Orange \n' ])

file.close() # kam hone ke baad always karna hota hai




#ex2 using 'with' close() automatic ho jata hai karna nahi parta hai 
#ex1 same kam using with 
with open("basic.txt", 'r') as file:
  print(file.read(5)) # read 5 character only - Welco
  print(file.readline()) # read one line at a time only - me to the universe
  print(file.readline()) # now it reads next line - Hello world

  print(file.read()) 
  '''
  Mango 
  Apple 
  Banana 
  Orange
  '''

  #ex3
  # file.read() # it gives empty list because, we are read file already using file.read()
  # lakin mai fir bhi chata hu ki file ko read karna hai toh file.seek(0) use karo 
  file.seek(0) # seek used to change the position 
  readlines_list = file.readlines()
  print(readlines_list)
  print(file.tell()) # tell that current postion 


