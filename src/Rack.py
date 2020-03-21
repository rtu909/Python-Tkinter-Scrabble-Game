from Bag import *

class Rack:
    """
    Creates each player's 'dock', or 'hand'. Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        #Initializes the player's rack/hand. Takes the bag from which the racks tiles will come as an argument.
        self.rack = []
        self.bag = bag
        self.initialize()

    def addToRack(self):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(self.bag.takeFromBag())

    def initialize(self):
        #Adds the initial 7 tiles to the player's hand.
        for i in range(7):
            self.addToRack()

    def getRackStr(self):
        #Displays the user's rack in string form.
        return ", ".join(str(tile.getLetter()) for tile in self.rack)

    def getRackArr(self):
        #Returns the rack as an array of tile instances
        return self.rack

    def removeFromRack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def getRackLength(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenishRack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        while self.getRackLength() < 7 and self.bag.getRemainingTiles() > 0:
            self.addToRack()
