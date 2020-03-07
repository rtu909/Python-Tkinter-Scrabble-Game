from Tiles import *
from random import shuffle

class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    def __init__(self):
        #Creates the bag full of game tiles, and calls the initialize_bag() method, which adds the default 100 tiles to the bag.
        #Takes no arguments.
        self.bag = []
        self.initialize_bag()

    def addToBag(self, tile, numOfTiles):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(numOfTiles):
            self.bag.append(tile)

    def initBag(self):
        #Adds the intiial 100 tiles to the bag.
        self.addToBag(Tile("A"), 9)
        self.addToBag(Tile("B"), 2)
        self.addToBag(Tile("C"), 2)
        self.addToBag(Tile("D"), 4)
        self.addToBag(Tile("E"), 12)
        self.addToBag(Tile("F"), 2)
        self.addToBag(Tile("G"), 3)
        self.addToBag(Tile("H"), 2)
        self.addToBag(Tile("I"), 9)
        self.addToBag(Tile("J"), 9)
        self.addToBag(Tile("K"), 1)
        self.addToBag(Tile("L"), 4)
        self.addToBag(Tile("M"), 2)
        self.addToBag(Tile("N"), 6)
        self.addToBag(Tile("O"), 8)
        self.addToBag(Tile("P"), 2)
        self.addToBag(Tile("Q"), 1)
        self.addToBag(Tile("R"), 6)
        self.addToBag(Tile("S"), 4)
        self.addToBag(Tile("T"), 6)
        self.addToBag(Tile("U"), 4)
        self.addToBag(Tile("V"), 2)
        self.addToBag(Tile("W"), 2)
        self.addToBag(Tile("X"), 1)
        self.addToBag(Tile("Y"), 2)
        self.addToBag(Tile("Z"), 1)
        self.addToBag(Tile("#"), 2)
        shuffle(self.bag)

    def takeFromBag(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def getRemainingTiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)