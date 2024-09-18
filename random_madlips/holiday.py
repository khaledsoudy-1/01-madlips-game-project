# A Holiday Adventure MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective (exciting): ")
    adj2 = input("Adjective (colorful): ")
    holiday = input("Holiday: ")
    name = input("Name: ")
    location = input("Location: ")
    food = input("Holiday Food: ")
    activity = input("Activity: ")
    item = input("Holiday Item: ")
    friend = input("Friend's Name: ")
    surprise = input("Surprise Gift: ")
    
    # Create the Mad Libs story
    holiday_madlip = f"""
Title: {name}'s {holiday} Extravaganza

This year, {name} had an {adj1} {holiday} celebration at {location}. The house was decorated with {adj2} lights and {holiday} decorations.

For the big feast, everyone enjoyed delicious {food} while {name} and their friend, {friend}, played {activity} in the yard. The highlight of the day was when {name} received a {surprise} as a {holiday} gift, which was the perfect ending to an {adj1} holiday.
"""
    
    # Print the Mad Libs story
    print(holiday_madlip)

if __name__ == '__main__':
    madlip()


