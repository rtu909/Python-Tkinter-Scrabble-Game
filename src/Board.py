
class Board:
    def __init__(self):
        self.backBoard = [["0" for col in range(0, 15)] for row in range(0, 15)]

    def getBoard(self):
        return self.backBoard
    
    ## @brief updates the back end version of the board with the valid word.
    #  @param1 an integer that represents the row of an the back end array.
    #  @param2 an integer that represents the column of the back end array.
    #  @param3 a string that represents the direction of the word placed on the board.
    #  @param4 a string that represents the word being placed on the board.
    def updateBackBoard(self, row, col, dir, word):
        dirLower = dir.lower()
        wordUp = word.upper()
        if(dirLower == "right"):
            countCol = int(col)
            for char in wordUp:
                self.backBoard[int(row)][int(countCol)] = char
                countCol += 1 
        elif(dirLower == "down"):
            countRow = int(row)
            for char in word:
                self.backBoard[int(col)][int(countRow)] = char
                countRow += 1