
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
            countCol = int(col)
            for char in word:
<<<<<<< HEAD
                backBoard[int(row)][int(countCol)] = char
=======
                self.backBoard[row][countCol] = char
>>>>>>> 96e98d53fd2fb24d0241d3f865981fa337f575e9
                countCol += 1 
        elif(dir.lower() == "down"):
            countRow = int(row)
            for char in word:
<<<<<<< HEAD
                backBoard[int(col)][int(countRow)] = char
=======
                self.backBoard[col][countRow] = char
>>>>>>> 96e98d53fd2fb24d0241d3f865981fa337f575e9
                countRow += 1