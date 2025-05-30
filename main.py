import random
def main():
   secret_number = random.randint(1,100)
   highscore = 0
   isrunning = True
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
                   break
               case 2:
                   print("Great! You have selected the Medium difficulty level.")
                   break
               case 3:
                   print("Great! You have selected the Hard difficulty level.")
                   break
               case _:
                   print("Please enter a valid level!")
       except ValueError:
           print("Please enter a number!")
   print("Let's start the game!\n")
if __name__ == "__main__":
    main()