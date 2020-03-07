from graphics import *

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}
				 
SCORE_TYPES = {"Normal": 0, "DLS": 1, "DWS": 2, "TLS": 3

#Use below lists when making tiles on window(was trying to ease your job with this).
DLS_Tiles = [[0, 3], [0, 11], [2, 6], [2, 8], [3, 0], [3, 7], [3, 14], [6, 2], [6, 6], [6, 8], [6, 12], [7, 3], 
			[7, 11], [8, 2], [8, 6], [8, 8], [8, 12], [11, 0], [11, 7], [11, 14], [12, 6], [12, 8], [14, 3], [14, 11]]
			
DWS_Tiles = [[1, 1], [1, 13], [2, 2], [2, 12], [3, 3], [3, 11], [4, 4], [4, 10], 
			[10, 4], [10, 10], [11, 3], [11, 11], [12, 2], [12, 12], [13, 1], [13, 3]]
			
TLS_Tiles = [[1, 5], [1, 9], [5, 1], [5, 5], [5, 9], [5, 13], [9, 1], [9, 5], [9, 9], [9, 13], [13, 5], [13, 9]]

class Tile:
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """
    def __init__(self, letter):
        #Initializes the tile class. Takes the letter as a string, and the dictionary of letter values as arguments.
		self.letter = ''
		self.type = ""
		self.score = 0
        '''self.letter = letter.upper()
		self.tile_shape = 
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0'''
			
	def setLetter(self, new_letter): #Made if else statements from constructor into a setter function which can be called whenever tile letter is to be changed.
		self.letter = new_letter.upper() #Supposed to be used when game is updating the board based on players inputted word.
		if self.letter in LETTER_VALUES:
			self.score = LETTER_VALUES.[self.letter]
			
    def getLetter(self):
        #Returns the tile's letter (string).
        return self.letter

    def getScore(self):
        #Returns the tile's score value.
        return self.score