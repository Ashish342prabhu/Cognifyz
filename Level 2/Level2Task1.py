import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != number:
    if guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    guess = int(input("Guess again: "))
if guess == number:
    print("Congratulations! You guessed the number correctly.")