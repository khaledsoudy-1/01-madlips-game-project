# A Love Story MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective (romantic): ")
    adj2 = input("Adjective (unexpected): ")
    name = input("Name: ")
    place = input("Place (e.g., park, café): ")
    verb1 = input("Verb (action): ")
    noun1 = input("Noun (gift or object): ")
    noun2 = input("Noun (emotion): ")
    verb2 = input("Verb (something you do for love): ")
    famous_person = input("Famous Person: ")
    
    # Create the Mad Libs story
    love_madlip = f"""
Title: {name}'s Unexpected Romance

It was a {adj1} afternoon when {name} went to the {place}. While there, they {verb1} and unexpectedly bumped into someone who handed them a {noun1}.

Feeling {adj2}, {name} started to feel a strong sense of {noun2}. To win their heart, {name} decided to {verb2} and even enlisted the help of {famous_person}!

In the end, love was found, and it was the beginning of a beautiful new chapter.
"""
    
    # Print the Mad Libs story
    print(love_madlip)

if __name__ == '__main__':
    madlip()

