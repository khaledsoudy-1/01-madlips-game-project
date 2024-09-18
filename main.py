from random_madlips import adventure, football, holiday, love, school, space, travel
import random

# A function for getting a random madlip
def get_random_madlip():
    random_choice = random.choice([adventure, football, holiday, love, school, space, travel])
    return random_choice.madlip()

while True:
    # Print a welcome message
    print("==== Welcome to The Madlips Game 🤖 ====")
    print("Please, enter the following:\n")
    
    # Call the function inside the loop
    get_random_madlip()
    
    # Ask user if they want to play again.
    print("Play again ?!")
    
    playagain = input("Y for Yes\nQ to Quit\n").lower().strip()
    
    # Enter the following loop only if wrong input was given.
    while playagain not in ["y", "q"]:
        playagain = input("Y for Yes\nQ to Quit\n")
        
    # If user wants to play again.
    if playagain == 'y':
        # Print a welcome back message
        print("\n==== Welcome Back 😍 ====")
        print("Please, enter the following:\n")
        get_random_madlip()

    # If user does not want to play again.
    if playagain == 'q':
        print("\n🎉🎉Thank you for playing!\nBye 👋")
        break
    