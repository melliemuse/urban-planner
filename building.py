import datetime


class Building: 
    def __init__(self, name, time, owner, address, stories):
        self.designer = name
        self.date_constructed = time 
        self.owner = owner
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = date.datetime.now()
        print(self.date_constructed)

building_test = Building("Hancock", "a bygone era", "Frank Lloyd Wright", "Wacker", "tall tales")

building_test.construct()
    # def purchase():

# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories
# Once defined this way, you can send those values as parameters when you create each instance

#  eight_hundred_eighth = Building("800 8th Street", 12)
# Creating Your Buildings
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.