class Tile:
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """

    def __init__(self, letter):
        LETTER_VALUES = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5,
        "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
        "Y": 4, "Z": 10}
        #Initializes the tile class. Takes the letter as a string, and the dictionary of letter values as arguments
        self.letter = letter.upper()
        self.score = 0
        if self.letter in LETTER_VALUES:
            self.score = LETTER_VALUES[self.letter]
        else:
            self.score = 0

    def getLetter(self):
        #Returns the tile's letter (string).
        return self.letter

    def getScore(self):
        #Returns the tile's score value.
        return self.score