# Number Guessing Game

import random

number = random.randrange(1, 20)
guess = int(input("Please enter any number between 1 - 20: "))
while guess != number:
    if guess < number:
        print("{} is lower than the correct Guess!".format(guess))
        guess = int(input("Please enter another number between {} and 20: ".format(guess)))
    elif guess > number:
        print("{} is higher than the correct Guess!".format(guess).format(guess))
        guess = int(input("Please enter another number between 1 and {}: ".format(guess)))
    else:
        break
print("Congratulations! You gessed it right!!")