import sys
from random_madlips import adventure, football, holiday, love, school, space, travel
import random

# A function for getting a random madlip
def get_random_madlip():
    random_choice = random.choice([adventure, football, holiday, love, school, space, travel])
    return random_choice.madlip()

get_random_madlip()

# Ask user if they want to play again.
print("Play again ?!")

while True:
    playagain = input("Y for Yes\nQ to Quit\n")
    
    if playagain.lower() in ['y', 'q']:
        break

   
if playagain.lower() == 'y':
    print("==== Welcome Back 😍 ====")
    get_random_madlip()
    
if playagain.lower() == 'q':
    print("🎉🎉Thank you for playing!\nBye 👋")
    sys.exit()
    
    