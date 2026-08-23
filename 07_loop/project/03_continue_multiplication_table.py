# Print the multiplication table of a given number up to 10, but skip the fifth iteration.

user_input = int(input('\nEnter number for multiplication table : '))

for i in range(1 , 11):
 
  if i == 5:    # detect and Skip the 5th iteration.
    continue

  answer = user_input * i 

  print (f'{user_input} x {i} = {answer}')



'''
continue means:
Skip the remaining code in this iteration and go to the next iteration.
'''