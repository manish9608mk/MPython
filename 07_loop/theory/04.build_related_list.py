# some usecase of loop - for 

# eg1 
numbers = [1,3,5,7,4,45456]
squares =[]

for num in numbers:
  square = num ** 2
  squares.append(square)

print(f'Numbers: {numbers}') 
print(f'Squares: {squares}\n') 


# ex2 - iterating numbers 
# suppose we have to print square of 1 to 100 so, in this case we can do it manually like [1,2,3,....100] but it so complex we can makes mistakes so, in such conditions we can use range() eg. range(100) it goes to 1 to 99

for num in range(101):
  print(num ** 2)


# eg3 - looping over indices of a list 
# range(4) this is hard coding if we more item in list then we may occur error so, insted of this we can use len(x)
print()

x = ['red', 'green', 'blue', 'pink']
for i in range(len(x)):
  print("The value at index", i, "is", x[i])



# some usecase of loop - while
# eg4 - implementing log2 or log base 2 of some number n 
print()

n = 100
num_divides = 0

while n != 1:
  n = n // 2 # n/2 it gives float value so we use n//2
  num_divides += 1

print("The total number of times it took to get to 1 is : ", num_divides)  


'''
Why is this related to log₂(n)?
Look at this table:

|  n | Divisions to reach 1 |
|    | -------------------  |
|  2 |                    1 |
|  4 |                    2 |
|  8 |                    3 |
| 16 |                    4 |
| 32 |                    5 |
| 64 |                    6 |

'''

