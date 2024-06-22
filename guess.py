import random

def guessing_game():
    number = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while attempts < 5:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed the number in {attempts} attempts.")
            break

    if guess != number:
        print(f"Sorry, the number I was thinking of was {number}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()
