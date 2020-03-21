from wordChecks import *
class checkBoardRight:

    def occupiedTile(word, row, col, board):
        row = int(row)
        colcount = int(col)
        wordUp = word.upper()
        print(wordUp)
        matchesTile = False
        for char in wordUp:
            if board[row][colcount] == "0":
                print(board[row])
                print(board[row][colcount])
                colcount += 1
                print(colcount)
            elif board[row][colcount] == char: #matches char
                print(board[row])
                print(board[row][colcount])
                colcount += 1
                print(colcount)
                matchesTile = True
            else:
                print(colcount, "col")
                print(row, "row")
                print(board[row])
                print(board[row][colcount], "board char")
                print(char)
                print("occupiedTile error")
                return False
        print(matchesTile and True)
        return matchesTile and True

    def adjWordCheck(word, row, col, board):
        #checking for a word being placed right
        colCount = int(col)
        corrWords = True
        for char in word:
            if board [int(row)-1][colCount] == "0" and board[int(row) + 1][colCount] == "0":
                colCount += 1
            else:
                rowCount = int(row)
                while board[rowCount][colCount] != "0" :
                    rowCount += 1
                end = colCount
                while board[rowCount][colCount] != "0" :
                    rowCount -= 1
                begin = colCount
                for rown in range(begin, end):
                    word = word + board[row][colCount]
                boow = wordCheck.checkInDict(word)
                corrWords = corrWords and boow
        return corrWords

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
                print("placement check error")
                return False
        else:
            return checkBoardRight.occupiedTile(word,row, col, board)

    def rightCheck(word, row, col, board, count):
        return checkBoardRight.outOfBounds(word, row, col, board) and checkBoardRight.placementCheck(word, row, col, board, count) and checkBoardRight.adjWordCheck(word, row, col, board)

class checkBoardDown:
    def occupiedTile(word, row, col, board):
        wordUp = word.upper()
        rowcount = int(row)
        col = int(col)
        for char in wordUp:
            if board[rowcount][col] == "0":
                rowcount += 1
            elif board[rowcount][col] == char: #matches char
                rowcount += 1
            else:
                print("occupiedTile error")
                return False
        return True

    def adjWordCheck(word, row, col, board):
        #checking for a word being placed downwards
        rowCount = int(row)
        corrWords = True
        for char in word:
            if board [rowCount][int(col)-1] == "0" and board[rowCount][int(col)+1] == "0":
                rowCount += 1
            else:
                colCount = int(col)
                while board[rowCount][colCount] != "0" :
                    colCount += 1
                end = colCount
                while board[rowCount][colCount] != "0" :
                    colCount -= 1
                begin = colCount
                for coln in range(begin, end):
                    word = word + board[rowCount][coln]
                boow = wordCheck.checkInDict(word)
                corrWords = corrWords and boow
        return corrWords

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
            return True

    def downCheck(word, row, col, board, count):
        return checkBoardDown.occupiedTile(word, row, col, board) and checkBoardDown.outOfBounds(word, row, col, board) and checkBoardDown.placementCheck(word, row, col,board, count) and checkBoardDown.adjWordCheck(word, row, col, board)

wordCheck = wordChecks()
