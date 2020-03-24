from wordChecks import *
from Board import *
import copy

class checkBoardRight:
    wordCheck = wordChecks()

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

    #update copy of board with the word to be tested for adding
    def updateArray(word, row, col, adjBoard):
        countCol = int(col)
        for char in word:
            char = char.upper()
            adjBoard[int(row)][countCol] = char
            countCol += 1
        return adjBoard

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
                wordExists = checkBoardRight.checkInDict(findWord)
                corrWords = corrWords and wordExists
                colCount += 1
        return corrWords

    def checkInDict(word):
       dicfile = open('dic.txt', 'r')
       file1 = dicfile.read()
       file1 = file1.split("\n")
       word = word.upper()
       if word in file1:
           checksBool = True
       else:
           checksBool = False
       dicfile.close()
       return checksBool

    def outOfBounds(word, row, col, board):
        row = int(row)
        col = int(col)
        print("in bounds", (col <= 14 and row <= 14 and col + len(word) <= 14))
        return (col <= 14 and row <= 14 and col + len(word) <= 14)

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

    def rightCheck(word, row, col, board, count):
        return checkBoardRight.outOfBounds(word, row, col, board) and checkBoardRight.placementCheck(word, row, col, board, count) and checkBoardRight.adjWordCheck(word, row, col, board)

class checkBoardDown:
    wordCheck = wordChecks()

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

    def updateArray(word, row, col, adjBoard):
        countRow = int(row)
        for char in word:
            char = char.upper()
            adjBoard[countRow][int(col)] = char
            countRow += 1
        return adjBoard

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
               wordExists = checkBoardRight.checkInDict(findWord)
               corrWords = corrWords and wordExists
               rowCount += 1

        return corrWords

    def checkInDict(word):
        dicfile = open('dic.txt', 'r')
        file1 = dicfile.read()
        file1 = file1.split("\n")
        word = word.upper()
        if word in file1:
            checksBool = True
        else:
            checksBool = False
        return checksBool

    def outOfBounds(word, row, col, board):
        col = int(col)
        row = int(row)
        return (col <= 14 and row <= 14 and row + len(word) <= 14)

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

    def downCheck(word, row, col, board, count):
        return checkBoardDown.outOfBounds(word, row, col, board) and checkBoardDown.placementCheck(word, row, col,board, count) and checkBoardDown.adjWordCheck(word, row, col, board)
