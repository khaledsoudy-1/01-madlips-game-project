# An Adventure MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    noun = input("Noun: ")
    name = input("Name: ")
    f_person = input("Famous Person: ")
    animal = input("Animal: ")
    obj = input("Object: ")
    activity = input("Activity: ")
    substance = input("Substance: ")
    
    # Create the Mad Libs story
    adventure_madlip = f"""
Title: {name}'s Wacky Adventure

One day, {name} went to a {adj1} park with a {noun}. They ran into {f_person}, who was with a {adj2} {animal}.

{f_person} asked for a {adj3} {obj} to help with a {activity}. After helping out, {name} and the {animal} ended up covered in {substance}, laughing all the way home.
"""
    
    # Print the Mad Libs story
    print(adventure_madlip)

if __name__ == '__main__':
    madlip()


