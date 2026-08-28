# File handling practice 
# # append mode; 'a' - add new data after previous old data

# Step 1: Create / overwrite
with open("append_mode.txt", "w", encoding="utf-8") as file:
  file.write("Mango\n")
  file.write("Apple\n")
  file.write("Orange\n")


# Step 2: Append
with open("append_mode.txt", "a", encoding="utf-8") as file:
  file.write("Banana\n")
  file.write("Grapes\n")
  file.writelines(["Sun\n", "Moon\n", "Star\n"])


# Step 3: Verify / Read
with open("append_mode.txt", "r", encoding="utf-8") as file:
  print(file.read())