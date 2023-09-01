import random
lower_limit = 1
upper_limit = 100

# Generate a random number within the specified range
random_number = random.randint(lower_limit, upper_limit)
num_guesses = 0
max_guesses = 5
while num_guesses < max_guesses:
    guess = int(input("Guess the number between {} and {}: ".format(lower_limit, upper_limit)))
    num_guesses += 1
    if guess == random_number:
        print("Congratulations! You guessed the number in {} guesses.".format(num_guesses))
        break
    elif guess > random_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

if num_guesses == max_guesses:
    print("Sorry, you ran out of guesses. The number was {}.".format(random_number))