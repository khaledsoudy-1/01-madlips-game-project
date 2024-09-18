# A Space Adventure MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    noun1 = input("Noun (space object): ")
    noun2 = input("Noun (equipment): ")
    name = input("Name: ")
    alien = input("Alien Species: ")
    planet = input("Planet Name: ")
    verb = input("Verb: ")
    food = input("Space Food: ")
    
    # Create the Mad Libs story
    space_madlip = f"""
Title: {name}'s Galactic Quest

In a faraway galaxy, {name} set off on a {adj1} adventure to explore the {noun1}. Along the way, they encountered a {adj2} {alien} who was using a {adj3} {noun2}.

The {alien} invited {name} to their home planet, {planet}, where they spent the day {verb} and eating delicious {food}. By the end of the journey, {name} and the {alien} had become best friends, and {name} couldn't wait for their next {adj1} adventure.
"""
    
    print(space_madlip)

if __name__ == '__main__':
    madlip()