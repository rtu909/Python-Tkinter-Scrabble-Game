from wordChecks import *
class checkBoardRight:
    def occupiedTile(self, row, col, word, board):
        colcount = col
        for char in word:
            if board[row][colcount] == "0":
                colcount += 1
            elif board[row][colcount] == char: #matches char
                colcount += 1
            else:   
                return False
        return True
    
    def neighbourTiles(self, row, col, word, board):
        colcount = col
        rowcount = row
        boolCheck = True
        for char in word:
            while board[row][colcount] != "0":
                colcount += 1
            last = board[row][colcount]
            lastRow = row
            lastCol = colcount
            while board[row][colcount] != "0":
                colcount -= 1
            first = board[row][colcount]
            firstRow = row
            firstCol = colcount
            for i in range(first.col, last.col):
                word = word + board[row][i]
            boolCheck = boolCheck and wordChecks.checkInDict(word)
        
        return boolCheck
            
        
    def outOfBounds(self, row, col, word, board):
        return (col <= 14 and row <= 14 and col + len(word) <= 14)
    
    def placementCheck(self, row, col, word, board, count):
        if count == 0:
            if (row == 7) and (col == 7):
                return True
            else:
                return False
        else:
            if board[row][col] == word[0]:
                return True
            else:
                return False
        
    def rightCheck(self, row, col, word, board, count):
        return checkBoardRight.occupiedTile(row, col, word, board) and checkBoardRight.neighbourTiles(row, col, word, board) and checkBoardRight.outOfBounds(row, col, word, board) and checkBoardRight.placementCheck(row, col, word, board, count)

class checkBoardDown:
    def occupiedTile(self, row, col, word, board):
        rowcount = 0
        for char in word:
            if board[rowcount][col] == "0":
                rowcount += 1
            elif board[rowcount][col] == char: #matches char
                rowcount += 1
            else:    
                return False
        return True
    
    def neighbourTiles(self, row, col, word, board):
        colcount = 0
        rowcount = 0
        boolCheck = True
        for char in word:
            while board[rowcount][col] != "0":
                rowcount += 1
            last = board[rowcount][col]
            lastRow = rowcount
            lastCol = col
            while board[rowcount][col] != 0:
                rowcount -= 1
            first = board[rowcount][col]
            firstRow = rowcount
            firstCol = col
            for i in range(firstRow, lastRow):
                word = word + board[i][col].getLetter
            #boolCheck = boolCheck and checkDict(word)
        
        return boolCheck
    
    def outOfBounds(self, row, col, word, board):
        return (col <= 14 and row <= 14 and row + len(word) <= 14)
        
    def downCheck(self, row, col, word, board):
        return occupiedTile(row, col, word, board) and neighbourTiles(row, col, word, board) and outOfBounds(row, col, word, board)
    