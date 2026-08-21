marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:    # now -ve and >100 are also check
  print('Invalid Input')
  exit()

if marks >= 90:
  grade = "A"
elif marks >= 80:
  grade = "B"
elif marks >= 70:
  grade = "C"
elif marks >= 60:
  grade = "D"
else:
  grade = "F"

print(f"Student, your marks are {marks} and your grade is {grade}.")