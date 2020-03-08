from Bag import *
from Rack import *

class Player:
    """
    Creates an instance of a player. Initializes the player's rack, and allows you to set/get a player name.
    """
    def __init__(self, bag):
        #Intializes a player instance. Creates the player's rack by creating an instance of that class.
        #Takes the bag as an argument, in order to create the rack.
        self.rack = Rack(bag)
        self.score = 0

    def getRackStr(self):
        #Returns the player's rack.
        return self.rack.getRackStr()

    def getRackArr(self):
        #Returns the player's rack in the form of an array.
        return self.rack.getRackArr()

    def increaseScore(self, increase):
        #Increases the player's score by a certain amount. Takes the increase (int) as an argument and adds it to the score.
        self.score += increase

    def getScore(self):
        #Returns the player's score
        return self.score