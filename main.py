from random_madlips import adventure, football, holiday, love, school, space, travel
import random


# Function to get a random madlip
def get_random_madlip():
    random_choice = random.choice([adventure, football, holiday, love, school, space, travel])
    return random_choice.madlip()


# Function to play the Madlips game
def play_madlips():
    playing = True                # Control variable for the loop
    
    while playing:
        # Print instructions for the user
        print("Please, enter the following:\n")
        
        # Display a random madlip
        get_random_madlip()
        
        # Ask user if they want to play again.
        print("Play again ?!")
        playagain = input("Y for Yes\nQ to Quit\n").lower().strip()
        
        # Enter the following loop only if wrong input was given.
        while playagain not in ["y", "q"]:
            playagain = input("Y for Yes\nQ to Quit\n")
        
        # Continue the game if user chooses to play again
        if playagain == 'y':
            # Print a welcome back message
            print("\n==== Welcome Back 😍 ====")
            continue
        
        # Exit the game if user chooses to quit
        if playagain == 'q':
            print("\n🎉🎉Thank you for playing!\nBye 👋")
            playing = False          # Update the control variable to stop the loop


if __name__ == '__main__':
    print("===== Welcome to The Madlips Game 🤖 =====")
    play_madlips()
