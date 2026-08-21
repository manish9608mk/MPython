name = input('What is your name: ')
superpower = input('What is your superpower? ')
weakness = input('What is your weakness? ')
country = input('Which country do you protect? ')
hero_name = input('What is your superhero name? ')

print('\nBreaking News!\n')

print("Superhero "+ hero_name + ", also known as " + name + ", has arrived in " + country + "\nWith the power of " + superpower + ", no villain stands a chance.\nHowever, the hero must avoid " + weakness + " at all costs.\nThe people of " + country + " call " + hero_name + " their greatest protector.\n")


# print using f string

story = f""" Superhero {hero_name}, also known as {name }, has arrived in {country}\n With the power of {superpower}, no villain stands a chance.\n However, the hero must avoid {weakness} at all costs.\n The people of {country} call {hero_name} their greatest protector.\n """

print(story)

print('====================================\n'+'Thanks for playing!\n'+'====================================')


# Is project me hamne ye topics cover kiye:
# print()	
# input()	
# Variables	
# Strings	
# String Concatenation (+)	
# f-Strings	
# Triple Quotes	
# Escape Characters (\n)





