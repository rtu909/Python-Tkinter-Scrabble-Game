from wordChecks import *
from Board import *
import copy

## @file boardChecks.py
#  @author The Trifecta
#  @brief This method implements the checks for whether a given word can be inputted on to the board.
#  @date Apr.06,2020

#  @brief Performs board checks for words inputted in the horizontal right direction.
class checkBoardRight:

	## @brief checks whether a tile in chosen word placement is occupied or not.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to update with valid word.
    #  @returns boolean indicating whether board has tiles occupying chosen word placement.
    def occupiedTile(word, row, col, board):
        row = int(row)
        colcount = int(col)
        wordUp = word.upper()
        matchesTile = False
        for char in wordUp:
            if board[row][colcount] == "0":
                colcount += 1
            elif board[row][colcount] == char: #matches char
                colcount += 1
                matchesTile = True
            else:
                return False
        return matchesTile and True

    ## @brief Updates the current board object.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to update with valid word.
    #  @returns board object with word added to it.
    def updateArray(word, row, col, adjBoard):
        countCol = int(col)
        for char in word:
            char = char.upper()
            adjBoard[int(row)][countCol] = char
            countCol += 1
        return adjBoard

	## @brief Checks whether an inputted word is forming more words with adjacently existing words.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to check from.
    #  @returns boolean indicating that more words can be formed with adjacently existing words.
    def adjWordCheck(word, row, col, board):
        #checking for a word being placed right
        colCount = int(col)
        corrWords = True
        findWord = ""
        #create copy of board for checking placement
        adjBoard = copy.deepcopy(board)

        adjBoard = checkBoardRight.updateArray(word, row, col, adjBoard)
        for char in word:
            if  adjBoard[int(row)-1][colCount] == "0" and adjBoard[int(row) + 1][colCount] == "0":
                colCount += 1
            else:
                findWord = ""
                rowCount = int(row)
                while adjBoard[rowCount][colCount] != "0":
                    rowCount += 1
                end = rowCount
                rowCount = int(row)
                while adjBoard[rowCount][colCount] != "0" :
                    rowCount -= 1
                rowCount += 1
                begin = rowCount
                for rown in range(begin, end):
                    findWord = findWord + adjBoard[rown][colCount]
                wordExists = checkInDict(findWord)
                corrWords = corrWords and wordExists
                colCount += 1
        return corrWords

	## @brief Checks if a words inputted placement goes out of boards bounds.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to check from.
    #  @returns boolean indicating that word placement is within board bounds.
    def outOfBounds(word, row, col, board):
        row = int(row)
        col = int(col)
        return (col <= 14 and row <= 14 and col + len(word) <= 14)

	## @brief performs a placement check using above defined functions.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object check from.
	#  @param5 integer indicating number of words currently on board.
    #  @returns boolean indicating a valid word placement on current state of board.
    def placementCheck(word, row, col, board, count):
        colcount = int(col)
        wordUp = word.upper()
        if int(count) == 0:
            if (int(row) == 7) and (int(col) == 7):
                return True
            else:
                return False
        else:
            return checkBoardRight.occupiedTile(word,row, col, board)

	## @brief final check for a word inputted in the right direction.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object check from.
	#  @param5 integer indicating number of words currently on board.
    #  @returns boolean indicating whether a word can be placed in the right direction or not.
    def rightCheck(word, row, col, board, count):
        return checkBoardRight.outOfBounds(word, row, col, board) and checkBoardRight.placementCheck(word, row, col, board, count) and checkBoardRight.adjWordCheck(word, row, col, board)

#  @brief Performs board checks for words inputted in the vertical down direction.
class checkBoardDown:
    
	## @brief checks whether a tile in chosen word placement is occupied or not.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to update with valid word.
    #  @returns boolean indicating whether board has tiles occupying chosen word placement.
    def occupiedTile(word, row, col, board):
        wordUp = word.upper()
        rowcount = int(row)
        col = int(col)
        matchesTile = False
        for char in wordUp:
            if board[rowcount][col] == "0":
                rowcount += 1
            elif board[rowcount][col] == char: #matches char
                rowcount += 1
                matchesTile = True
            else:
                return False
        return matchesTile and True

	## @brief Updates the current board object.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to update with valid word.
    #  @returns board object with word added to it.
    def updateArray(word, row, col, adjBoard):
        countRow = int(row)
        for char in word:
            char = char.upper()
            adjBoard[countRow][int(col)] = char
            countRow += 1
        return adjBoard

	## @brief Checks whether an inputted word is forming more words with adjacently existing words.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to check from.
    #  @returns boolean indicating that more words can be formed with adjacently existing words.
    def adjWordCheck(word, row, col, board):
        #checking for a word being placed downwards
        rowCount = int(row)
        corrWords = True
        findWord = ""
        adjBoard = copy.deepcopy(board)
        adjBoard = checkBoardDown.updateArray(word, row, col, adjBoard)
        for char in word:
            if adjBoard[rowCount][int(col)-1] == "0" and adjBoard[rowCount][int(col)+1] == "0":
                rowCount += 1
            else:
               findWord = ""
               colCount = int(col)
               while adjBoard[rowCount][colCount] != "0":
                   colCount += 1
               end = colCount
               colCount = int(col)
               while adjBoard[rowCount][colCount] != "0" :
                   colCount -= 1
               colCount += 1
               begin = colCount
               for coln in range(begin, end):
                   findWord = findWord + adjBoard[rowCount][coln]
               wordExists = checkInDict(findWord)
               corrWords = corrWords and wordExists
               rowCount += 1

        return corrWords

	## @brief Checks if a words inputted placement goes out of boards bounds.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object to check from.
    #  @returns boolean indicating that word placement is within board bounds.
    def outOfBounds(word, row, col, board):
        col = int(col)
        row = int(row)
        return (col <= 14 and row <= 14 and row + len(word) <= 14)

	## @brief performs a placement check using above defined functions.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object check from.
	#  @param5 integer indicating number of words currently on board.
    #  @returns boolean indicating a valid word placement on current state of board.
    def placementCheck(word, row, col, board, count):
        rowCount = int(row)
        colCount = int(col)
        wordUp = word.upper()
        if int(count) == 0:
            if (int(row) == 7) and (int(col) == 7):
                return True
            else:
                return False
        else:
            return checkBoardDown.occupiedTile(word, row, col, board)

	## @brief final check for a word inputted in the down direction.
    #  @param1 string for the word to be added to the game board.
    #  @param2 integer for the row of starting tile.
    #  @param3 integer for the column of starting tile.
    #  @param4 board object check from.
	#  @param5 integer indicating number of words currently on board.
    #  @returns boolean indicating whether a word can be placed in the down direction or not.
    def downCheck(word, row, col, board, count):
        return checkBoardDown.outOfBounds(word, row, col, board) and checkBoardDown.placementCheck(word, row, col,board, count) and checkBoardDown.adjWordCheck(word, row, col, board)
