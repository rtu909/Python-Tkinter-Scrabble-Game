from wordChecks import *
class checkBoardRight:
    def occupiedTile(self, row, col, word, board):
        row = int(row)
        colcount = int(col)
        wordUp = word.upper()
        print(wordUp)
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
            else:   
                print(colcount, "col")
                print(row, "row")
                #print(board)
                print(board[row])
                print(board[row][colcount], "board char")
                print(char)
                print("occupiedTile error")
                return False
        return True
    
    def adjWordCheck(self, row, col, word, board):
        #checking for a word being placed right
        wordCheck = wordChecks()
        colCount = int(col)
        
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
                    word = word + board[rown][colCount]
                corrWords = corrWords and wordCheck.checkInDict(word)
        return corrWords
    
    def outOfBounds(self, row, col, word, board):
        row = int(row)
        col = int(col)
        print("outofbounds", (col <= 14 and row <= 14 and col + len(word) <= 14))
        return (col <= 14 and row <= 14 and col + len(word) <= 14)
    
    def placementCheck(self, row, col, word, board, count):
        colcount = int(col)
        wordUp = word.upper()
        if int(count) == 0:
            if (int(row) == 7) and (int(col) == 7):
                return True
            else:
                print("placement check error")
                return False
        else:
            return True
            
            
    def rightCheck(self, row, col, word, board, count):
        #and self.neighbourTiles(row, col, word, board)
        return self.occupiedTile(row, col, word, board) and self.outOfBounds(row, col, word, board) and self.placementCheck(row, col, word, board, count)

class checkBoardDown:
    def occupiedTile(self, row, col, word, board):
        rowcount = int(row)
        col = int(col)
        wordUp = word.upper()
        for char in wordUp:
            if board[rowcount][col] == "0":
                rowcount += 1
            elif board[rowcount][col] == char: #matches char
                rowcount += 1
            else:    
                print("occupiedTile error")
                return False
        return True

    def adjWordCheck(self, row, col, word, board):
        #checking for a word being placed downwards
        wordCheck = wordChecks()
        rowCount = int(row)
        
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
                corrWords = corrWords and wordCheck.checkInDict(word)
        return corrWords

    def outOfBounds(self, row, col, word, board):
        col = int(col)
        row = int(row)
        return (col <= 14 and row <= 14 and row + len(word) <= 14)
    
    def placementCheck(self, row, col, word, board, count):
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
        
    def downCheck(self, row, col, word, board, count):
        #and self.neighbourTiles(row, col, word, board)
        return self.occupiedTile(row, col, word, board) and self.outOfBounds(row, col, word, board) and self.placementCheck(row, col, word, board, count)
    