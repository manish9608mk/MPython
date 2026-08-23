import random

# part 1 - user guessing computer secret number
def guess(x):
  random_number = random.randint(1, x)
  guess = 0

  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print('Sorry, guess again. Too low.')
    elif guess > random_number:
      print('Sorry, guess again. Too high.')

  print(f'Yay, congrats. you have guess the number {random_number}, Correctly!!')

# part 2 - computer guessing our secrect number
def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    if low != high:
     guess = random.randint(low, high)
    else:
      guess = low # could also be high b/c low = high
    feedback = input(f'Is {guess} too high (H), too low (L), correct (C)').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f'Yay! The computer your gussed your number, {guess}, correctly!')    

guess(10)
print('--------------')
computer_guess(10)


