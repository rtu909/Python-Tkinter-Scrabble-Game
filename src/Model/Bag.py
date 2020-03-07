from Tiles import *
from random import shuffle

## @file Bag.py
#  @author The Trifecta
#  @brief This method implements the back end model of the bag for the Scrabble game.
#  @date Feb.15,2020
class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    ## @brief initializes the bag model by calling the initBag() method, which adds the default 100 tiles to the bag.
    def __init__(self):
        self.bag = []
        self.initBag()

    ## @brief Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
    #  @param1 a tile object that represents the letter tile.
    #  @param2 the number of tiles being added to the back.
    def addToBag(self, tile, numOfTiles):
        
        for i in range(numOfTiles):
            self.bag.append(tile)

    ## @brief initializes the bag with the 100 letter tiles needed to play the game.
    def initBag(self):
        #Added 1 extra A and S tile compared to regular scrabble game to compensate for removal of blank tile.
        self.addToBag(Tile("A"), 10)
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
        self.addToBag(Tile("S"), 5)
        self.addToBag(Tile("T"), 6)
        self.addToBag(Tile("U"), 4)
        self.addToBag(Tile("V"), 2)
        self.addToBag(Tile("W"), 2)
        self.addToBag(Tile("X"), 1)
        self.addToBag(Tile("Y"), 2)
        self.addToBag(Tile("Z"), 1)
        shuffle(self.bag)

    ## @brief Removes a tile from the bag.
    #  @return Returns the tile from the end of the bag.
    def takeFromBag(self):
        return self.bag.pop()

    ## @brief Returns the number of tiles left in the bag.
    #  @return Number of tiles left in the bag.
    def getRemainingTiles(self):
        return len(self.bag)