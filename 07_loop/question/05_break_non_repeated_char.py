# Given a string, find the first non-repeated character.
# eg: teeter - first non-repeated is r

user_input = input('Enter any string : ').strip().lower()

for char in user_input:
  print(char)
  if user_input.count(char) == 1:
    print(f'First none repeative charcter is : {char}')
    break










print()
# Method2
user_input = input("Enter any string: ").strip().lower()

found = False      # Initially assume no answer exists

for char in user_input:
    if user_input.count(char) == 1:
        print(f"First non-repeated character is: {char}")
        found = True      # We found the answer
        break

if not found:
    print("No non-repeated character found.")