import random

# part 1 - user guessing computer secret number : with try except and while True

def guess(x):

    random_number = random.randint(1, x)
    attempts = 0

    while True:

        try:
            user_guess = int(input(f"Guess a number between 1 and {x}: "))

            if user_guess < 1 or user_guess > x:
                print(f"Please enter a number between 1 and {x}.")
                continue

            attempts += 1

            if user_guess < random_number:
                print("Sorry, guess again. Too low.")

            elif user_guess > random_number:
                print("Sorry, guess again. Too high.")

            else:
                print(f"Yay! You guessed the number {random_number} correctly!")
                print(f"You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

guess(10)