import random
def user_input():
    while True:
        try:
            chances = int(input("Enter your choice : "))
            match chances:
                case 1:
                    print("Great! You have selected the Easy difficulty level.")
                    return 10
                case 2:
                    print("Great! You have selected the Medium difficulty level.")
                    return 5
                case 3:
                    print("Great! You have selected the Hard difficulty level.")
                    return 3
                case _:
                    print("Please enter a valid level!")
                    continue
        except ValueError:
            print("Please enter a number!")
            continue
def main():
    highscore = 0
    games_played = 0
    isrunning = True
    while isrunning:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("If you guess the number out of range, your chances will be reduced.")
        print("You can guess the number in 3 different difficulty levels.\n")
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        secret_number = random.randint(1,100)
        low_number = 1
        high_number = 100
        chances = user_input()
        guesses = 1
        print(f"You have {chances} chances to guess the number.")
        while True:
            guess = input(f"Guess the number (between {low_number} and {high_number}) - Chances left: {chances} : ")
            if not guess.isdigit() or guess == "" :  # Check if input is a digit and not empty
                print("Please enter a valid number!")
                continue
            guess = int(guess)
            if guess == 0 or guess < 0:
                print("Please enter a valid number!")
                continue
            elif guess < low_number or guess > high_number:
                print(f"Please enter a number between {low_number} and {high_number}!")
                continue
            elif guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                games_played += 1
                if chances > highscore:
                    highscore = guesses 
                    print(f"New high score: {highscore} chances only!")
                break
            else:
                chances -= 1
                guesses += 1
                if chances == 0:
                    print(f"Sorry, you've run out of chances. The secret number was {secret_number}.")
                    games_played += 1
                    break
                if guess < secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.") 
            if guess < secret_number:
                low_number = max(low_number, guess + 1)  # Pastikan tidak lebih kecil dari batas bawah
            elif guess > secret_number:
                high_number = min(high_number, guess - 1)  # Pastikan tidak lebih besar dari batas atas
        while True:
            try:
                choice = int(input("Do you want to play again? (1 for Yes, 0 for No): "))
                if choice == 1:
                    break
                elif choice == 0:
                    print("Thank you for playing! Goodbye!")
                    isrunning = False
                    print(f"Your best: guessed in {highscore} tries!")
                    return
                else:
                    print("Please enter a valid choice (1 or 0).")
            except ValueError:
                print("Please enter a number (1 or 0).")
        
if __name__ == "__main__":
    main()