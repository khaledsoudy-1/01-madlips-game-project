# A Football Match MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective (intense): ")
    adj2 = input("Adjective (funny): ")
    name = input("Name: ")
    team = input("Football Team: ")
    position = input("Position on the field: ")
    action = input("Verb (action on the field): ")
    noun1 = input("Noun (object): ")
    friend = input("Friend's Name: ")
    score = input("Score (e.g., 2-1): ")
    
    # Create the Mad Libs story
    football_madlip = f"""
Title: {name}'s Big Football Match

It was a {adj1} day for {name}, who was playing for {team} as the {position}. The crowd was going wild as {name} made a {adj2} move and {action} the {noun1} across the field.

The game was neck and neck, but thanks to {name}'s skill and teamwork with their friend {friend}, the score became {score}. The match ended with cheers, and {name} was hailed as the hero of the game!
"""
    
    # Print the Mad Libs story
    print(football_madlip)

if __name__ == '__main__':
    madlip()


