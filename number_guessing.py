import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    number_guessing_game()
