<<<<<<< HEAD

class endTurn:

=======
## @file endTurn.py
#  @author Lucia Cristiano
#  @brief This program performs various functions neeeded to update the front end after a move is validated. 
#  @date Feb.12,2020
class endTurn:

    ## @brief updates the back end version of the board with the valid word.
    #  @param1 an integer that represents the row of an the back end array.
    #  @param2 an integer that represents the column of the back end array.
    #  @param3 a string that represents the direction of the word placed on the board.
    #  @param4 a string that represents the word being placed on the board.
>>>>>>> f48988856355d7dd7df4d1df71dbb0cfc3d1686e
    def updateBackBoard(row, col, dir, word):
        if(dir.lower() = "right")
            countCol = col
            for char in word:
                backBoard[row][countCol] = char
                countCol ++
        elif(dir.lower() = "down")
            countRow = row
            for char in word:
                backBoard[col][countRow] = char
                countRow ++
<<<<<<< HEAD
    
    def updateFrontBoard():
        
=======
    ## @brief updates the back end version of the board with the valid word.
    #  @param1 an integer that represents the row of an the back end array.
    #  @param2 an integer that represents the column of the back end array.
    #  @param3 a string that represent the direction of the word placed on the board.
    #  @param4 a string that represents the word being placed on the board.
    #  @returns a list of tuples representing the row, column and text needed to be changed in the front end
    def updateFrontBoard(row, col, dir, word):
        frontList = []
        if(dir.lower() = "right")
            countCol = col
            for char in word:
                configTuple = (row, countCol, char)
                frontList.append(configTuple)
                countCol ++
        elif(dir.lower() = "down")
            countRow = row
            for char in word:
                configTuple = (countRow, col, char)
                frontList.append(configTuple)
                countRow ++
        return frontList
    
    def calculateScore():
    
    ## @brief checks if the game has been won
    #  @return returns a bool to represent win state or not
    def checkWinState():
        return Rack.getRackLength == 0 && Bag.getRemainingTiles == 0
>>>>>>> f48988856355d7dd7df4d1df71dbb0cfc3d1686e
