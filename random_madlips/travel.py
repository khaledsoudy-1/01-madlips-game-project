# A Travel Adventure MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective (exciting): ")
    adj2 = input("Adjective (unexpected): ")
    name = input("Name: ")
    country = input("Country: ")
    city = input("City: ")
    transport = input("Mode of Transportation: ")
    noun1 = input("Noun (item): ")
    activity = input("Travel Activity: ")
    noun2 = input("Noun (souvenir): ")
    friend = input("Friend's Name: ")
    
    # Create the Mad Libs story
    travel_madlip = f"""
Title: {name}'s {adj1} Trip to {country}

Last summer, {name} decided to take a {adj1} trip to {city}, {country}. They traveled by {transport}, and brought along a {noun1} for the journey.

While exploring {city}, {name} and their friend, {friend}, did lots of {activity}. The highlight of the trip was when they discovered a {adj2} {noun2} in the market!

After an amazing trip filled with adventure and surprises, {name} couldn't wait to plan their next trip.
"""
    
    # Print the Mad Libs story
    print(travel_madlip)

if __name__ == '__main__':
    madlip()
