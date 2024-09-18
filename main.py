from random_madlips import adventure, football, holiday, love, school, space, travel
import random

def get_random_madlip():
    random_choice = random.choice([adventure, football, holiday, love, school, space, travel])
    return random_choice.madlip()

get_random_madlip()
