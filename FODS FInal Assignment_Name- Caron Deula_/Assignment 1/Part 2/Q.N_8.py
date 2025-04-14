import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("We've selected a number between 1 and 100.")
print("You have 5 attempts to guess the correct number.")

# Counter for the number of guesses
attempts = 0
max_attempts = 5

# Game loop
while (attempts < max_attempts):
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Increment the attempt counter
    attempts += 1

    # Check the guess and provide feedback
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print(f"YEAHH!! Correct number! You guessed it in {attempts} attempts.")
        break

    # Check if the player has used all attempts
    if attempts == max_attempts and guess != answer:
        print(f"Ooops.....!Game Over! You've used all {max_attempts} attempts.")
        print(f"The correct number was {answer}.")

print("Thank you for playing!")