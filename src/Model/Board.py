
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
        if(dir.lower() == "right"):
            countCol = col
            for char in word:
                self.backBoard[row][countCol] = char
                countCol += 1 
        elif(dir.lower() == "down"):
            countRow = row
            for char in word:
                self.backBoard[col][countRow] = char
                countRow += 1