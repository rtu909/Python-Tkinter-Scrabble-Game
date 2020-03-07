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

    def addToBag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initBag(self):
        #Adds the intiial 100 tiles to the bag.
        self.add_to_bag(Tile("A"), 9)
        self.add_to_bag(Tile("B"), 2)
        self.add_to_bag(Tile("C"), 2)
        self.add_to_bag(Tile("D"), 4)
        self.add_to_bag(Tile("E"), 12)
        self.add_to_bag(Tile("F"), 2)
        self.add_to_bag(Tile("G"), 3)
        self.add_to_bag(Tile("H"), 2)
        self.add_to_bag(Tile("I"), 9)
        self.add_to_bag(Tile("J"), 9)
        self.add_to_bag(Tile("K"), 1)
        self.add_to_bag(Tile("L"), 4)
        self.add_to_bag(Tile("M"), 2)
        self.add_to_bag(Tile("N"), 6)
        self.add_to_bag(Tile("O"), 8)
        self.add_to_bag(Tile("P"), 2)
        self.add_to_bag(Tile("Q"), 1)
        self.add_to_bag(Tile("R"), 6)
        self.add_to_bag(Tile("S"), 4)
        self.add_to_bag(Tile("T"), 6)
        self.add_to_bag(Tile("U"), 4)
        self.add_to_bag(Tile("V"), 2)
        self.add_to_bag(Tile("W"), 2)
        self.add_to_bag(Tile("X"), 1)
        self.add_to_bag(Tile("Y"), 2)
        self.add_to_bag(Tile("Z"), 1)
        self.add_to_bag(Tile("#"), 2)
        shuffle(self.bag)

    def takeFromBag(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def getRemainingTiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)