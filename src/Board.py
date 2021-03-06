## @file Board.py
#  @author The Trifecta
#  @brief This method implements the back end model of the board for the Scrabble game.
#  @date Apr.06,2020
class Board:
	## @brief initializes the board object.
    def __init__(self):
        self.backBoard = [["0" for col in range(0, 15)] for row in range(0, 15)]

	## @brief returns board object.
	#  @return backBoard.
    def getBoard(self):
        return self.backBoard

    ## @brief updates the back end version of the board with the valid word.
    #  @param1 an integer that represents the row of the starting tile.
    #  @param2 an integer that represents the column of starting tile.
    #  @param3 a string that represents the direction of the word placed on the board.
    #  @param4 a string that represents the word being placed on the board.
	#  @exceptions ValueError if word does not meet board constraints.
    def updateBackBoard(self, word, row, col, dir):
        dirLower = dir.lower()
        wordUp = word.upper()
        row = int(row)
        col = int(col)
        if row > 14 or col > 14 or len(word) > 14:
            raise ValueError("Word is out of bounds")
        if(dirLower == "right"):
            countCol = int(col)
            for char in wordUp:
                char = char.upper()
                self.backBoard[int(row)][int(countCol)] = char
                countCol += 1
        elif(dirLower == "down"):
            countRow = int(row)
            for char in word:
                char = char.upper()
                self.backBoard[int(countRow)][int(col)] = char
                countRow += 1
        else:
            raise ValueError("Not a valid direction")
