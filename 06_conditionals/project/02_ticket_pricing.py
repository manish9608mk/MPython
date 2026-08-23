# Movie ticket pricing based on age
# $12 for adults (18+), $8 for children
# Everyone gets a $2 discount on Wednesday

# Method-1 without user input
age = 22
day = "wednesday"

price = 12 if age >= 18 else 8   #kkb in this question

if day == "wednesday":
    price -= 2
    # price = price -2

print(price)




print()
# method 2 - with user input
age = int(input("Please enter your age: "))
day = input("Please enter the day: ").lower()

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print(f"Ticket price: ${price}")