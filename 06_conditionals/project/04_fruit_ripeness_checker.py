fruit = 'Banana'
color = input('Please enter your banana color: ').strip().lower()
# .strip() starting aur ending ke extra spaces remove karta hai.

if fruit == 'Banana':
  if color == 'green':
     print('unriped')
  elif color == 'brown':
     print('overriped')
  elif color == 'yellow':
     print('ripe')
  else:
     print('Sorry, only three color allowed')
    


print('------------ using dictionary --------------')


status = {
    "green": "Unripe",
    "yellow": "Ripe",
    "brown": "Overripe"
}

color = input("Enter banana color: ").strip().lower()

if color in status:
    print(status[color])
else:
    print("Invalid color")

  
  


