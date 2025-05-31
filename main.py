import random

def get_difficulty():
    """Handle difficulty level selection with clear prompts"""
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy (10 guesses)")
        print("2. Medium (5 guesses)")
        print("3. Hard (3 guesses)")
        
        try:
            choice = int(input("Your choice (1-3): "))
            match choice:
                case 1: 
                    print("Easy mode selected. You get 10 guesses.")
                    return 10
                case 2:
                    print("Medium mode selected. You get 5 guesses.")
                    return 5
                case 3:
                    print("Hard mode selected. You get 3 guesses.")
                    return 3
                case _:
                    print("Please enter 1, 2, or 3!")
        except ValueError:
            print("Numbers only please!")

def play_game():
    """Core game logic"""
    secret = random.randint(1, 100)
    low, high = 1, 100
    max_guesses = get_difficulty()
    guesses_used = 0
    
    while guesses_used < max_guesses:
        remaining = max_guesses - guesses_used
        print(f"\nRange: {low}-{high} | Guesses left: {remaining}")
        
        try:
            guess = int(input("Your guess: "))
            if not 1 <= guess <= 100:
                print("Please enter between 1-100!")
                continue
            if guess < low or guess > high:
                print(f"Please stay within {low}-{high}!")
                continue
                
            guesses_used += 1
            
            if guess == secret:
                print(f"\n🎉 Correct! You guessed it in {guesses_used} tries!")
                return guesses_used
            elif guess < secret:
                print("Too low!")
                low = max(low, guess + 1)
            else:
                print("Too high!")
                high = min(high, guess - 1)
                
        except ValueError:
            print("Numbers only please!")
    
    print(f"\nGame over! The number was {secret}.")
    return None

def main():
    best_score = float('inf')
    games_played = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        result = play_game()
        games_played += 1
        
        if result and result < best_score:
            best_score = result
            print(f"⭐ New record: {best_score} guesses!")
        
        while True:
            choice = input("\nPlay again? (y/n): ").lower()
            if choice in ('y', 'yes'):
                break
            elif choice in ('n', 'no'):
                print(f"\nThanks for playing!")
                if best_score != float('inf'):
                    print(f"Your best game: {best_score} guesses.")
                print(f"Total games played: {games_played}")
                return
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()