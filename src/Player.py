from Bag import *
from Rack import *

## @file Player.py
#  @author The Trifecta
#  @brief This method implements the back end model of a player of the game. 
#         Initializes the player's rack, and allows you to set/get a player name
#  @date Apr.06,2020
class Player:
   
   ## @brief Intializes a player instance. Creates the player's rack by creating an instance of that class.
   #  @param1 bag that is used to create the players rack.
    def __init__(self, bag):
        self.rack = Rack(bag)
        self.score = 0

	## @brief returns the users rack as a string.
	#  @return a string where each character is a part of the users rack.
    def getRackStr(self):
        #Returns the player's rack.
        return self.rack.getRackStr()

	## @brief returns the users rack as an array.
	#  @return the rack object.
    def getRackArr(self):
        #Returns the player's rack in the form of an array.
        return self.rack.getRackArr()

	## @brief Increases the players score.
   	#  @param1 increase is the amount by which players score gets increased.
    def increaseScore(self, increase):
        #Increases the player's score by a certain amount. Takes the increase (int) as an argument and adds it to the score.
        if increase >= 0:
            self.score += increase
        else:
            raise ValueError("Not a valid score amount")

	## @brief returns players score.
	#  @return score.
    def getScore(self):
        #Returns the player's score
        return self.score