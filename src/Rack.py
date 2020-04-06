from Bag import *
## @file Rack.py
#  @author The Trifecta
#  @brief This method implements the back end model of each player's 'dock', or 'hand' for the Scrabble game. 
#         Allows players to add, remove and replenish the number of tiles in their rack.
#  @date Apr.06,2020
class Rack:
    
	## @brief initializes the rack by randomly picking tiles from the scrabble bag.
	#  @param1 bag from which to take tiles from.
    def __init__(self, bag):
        #Initializes the player's rack/hand. Takes the bag from which the racks tiles will come as an argument.
        self.rack = []
        self.bag = bag
        self.initialize()

	## @brief initializes a users rack using the addToRack Method.
    def initialize(self):
        #Adds the initial 7 tiles to the player's hand.
        FULL_RACK = 7 #constant for a full rack
        for i in range(FULL_RACK):
            self.addToRack()

	## @brief randomly chooses a tile to add to a users rack.
    def addToRack(self):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(self.bag.takeFromBag())

	## @brief returns the users rack as a string.
	#  @return a string where each character is a part of the users rack.
    def getRackStr(self):
        #Displays the user's rack in string form.
        return ", ".join(str(tile.getLetter()) for tile in self.rack)

	## @brief returns the users rack as an array.
	#  @return the rack object.
    def getRackArr(self):
        #Returns the rack as an array of tile instances
        return self.rack
		
	## @brief removes a tile from the rack.
	#  @param1 tile to be removed from rack.
    def removeFromRack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

	## @brief returns size of rack.
	#  @return the length of the rack list.
    def getRackLength(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

	## @brief Adds tiles to the rack depending on current size of rack.
    def replenishRack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        FULL_RACK = 7
        while self.getRackLength() < FULL_RACK and self.bag.getRemainingTiles() > 0:
            self.addToRack()
