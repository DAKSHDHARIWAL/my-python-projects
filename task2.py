import random

def play_game():
    # Random number 
    secret_number = random.randint(1, 100)
    
    max_attempts = 7
    attempt = 0

    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 100")
    print(f"You have {max_attempts} attempts\n")

    while attempt < max_attempts:
        try:
            guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        attempt += 1

        if guess == secret_number:
            print(f" Correct! You guessed the number in {attempt} attempts.")
            break
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print("Too low! Try again.\n")

    else:
        print(f"\n❌ Game Over! The correct number was {secret_number}")



play_game()