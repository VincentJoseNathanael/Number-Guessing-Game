import random
def main():
    secret_number = random.randint(1,100)
    highscore = 0
    isrunning = True
    chances = 0
    low_number = 1
    high_number = 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while isrunning:
        try:
            level = int(input("Enter your choice : "))
            match level:
                case 1:
                    print("Great! You have selected the Easy difficulty level.")
                    chances = 10
                    break
                case 2:
                    print("Great! You have selected the Medium difficulty level.")
                    chances = 5
                    break
                case 3:
                    print("Great! You have selected the Hard difficulty level.")
                    chances = 3
                    break
                case _:
                    print("Please enter a valid level!")
        except ValueError:
            print("Please enter a number!")
        print("Let's start the game!\n")
    while isrunning:
        guess = input(f"Guess the number (between {low_number} and {high_number}) - Chances left: {chances} : ")
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue
        guess = int(guess)
        if guess < low_number or guess > high_number:
            print(f"Please enter a number between {low_number} and {high_number}!")
            continue
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            if chances > highscore:
                highscore = chances
                print(f"New high score: {highscore} chances left!")
            break
        else:
            chances -= 1
            if chances == 0:
                print(f"Sorry, you've run out of chances. The secret number was {secret_number}.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
                if guess > low_number or low_number == 1:
                    low_number = guess + 1
            else:
                print("Too high! Try again.")  
                if guess < high_number or high_number == 100: 
                    high_number = guess - 1
            
  
             
if __name__ == "__main__":
    main()