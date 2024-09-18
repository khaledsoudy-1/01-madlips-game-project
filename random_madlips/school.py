# A School Adventure MadLip

def madlip():
    # Get user input for the Mad Libs story
    adj1 = input("Adjective (exciting): ")
    adj2 = input("Adjective (funny): ")
    subject = input("School Subject: ")
    name = input("Name: ")
    teacher = input("Teacher's Name: ")
    place = input("Place in School (e.g., classroom, gym): ")
    item = input("School Item: ")
    activity = input("School Activity: ")
    friend = input("Friend's Name: ")
    surprise = input("Surprise or Event: ")
    
    # Create the Mad Libs story
    school_madlip = f"""
Title: {name}'s School Shenanigans

On a {adj1} school day, {name} was in their {adj2} {subject} class with {teacher}. The class was held in the {place}, where everyone was excited to start the day's {activity}.

During the lesson, {name} discovered a hidden {item} and decided to use it to pull off a {surprise}. Their friend, {friend}, joined in the fun, and the entire class ended up having an unforgettable time filled with laughter and surprise moments.
"""
    
    # Print the Mad Libs story
    print(school_madlip)

if __name__ == '__main__':
    madlip()

