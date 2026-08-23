try:

  year = int(input("\nEnter year: "))

  if year <= 0:
    print('Enter valid year')
    exit()

  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f'Yes {year} is a leap year.')
  else:
    print(f'{year} Not a leap year.')

except ValueError:
  print('Please enter numbers only.')