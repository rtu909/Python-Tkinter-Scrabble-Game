from wordChecks import *
class checkBoardRight:
    def occupiedTile(self, row, col, word, board):
        row = int(row)
        colcount = int(col)
        wordUp = word.upper()
        for char in wordUp:
            if board[row][colcount] == "0":
                colcount += 1
            elif board[row][colcount] == char: #matches char
                colcount += 1
            else:   
                print("occupiedTile error")
                return False
        return True
    
    # def neighbourTiles(self, row, col, word, board):
    #     # wordChecks = wordChecks()
    #     # colcount = int(col)
    #     # rowcount = int(row)
    #     # boolCheck = True
    #     # #row = int(row)
    #     # for char in word:
    #     #     newWord = ""
    #     #     while board[row][colcount] != "0":
    #     #         colcount += 1
    #     #         #while
    #     #     #last = (row,colcount)
    #     #     lastRow = row
    #     #     lastCol = colcount
    #     #     # while board[row][colcount] != "0":
    #     #     #     colcount -= 1
    #     #     #first = (row,colcount)
    #     #     #firstRow = row
    #     #     #firstCol = colcount
    #     #     for i in range(first[1], last[1]):
    #     #         newWord = newWord + board[row][i]
    #     #     boolCheck = boolCheck and wordChecks.checkInDict(newWord)
    #     return boolCheck
            
        
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
    
    # def neighbourTiles(self, row, col, word, board):
    #     colcount = int(col)
    #     rowcount = int(row)
    #     col = int(col)
    #     row = int(row)
    #     boolCheck = True
    #     for char in word:
    #         while board[rowcount][col] != "0":
    #             rowcount += 1
    #         last = board[rowcount][col]
    #         lastRow = rowcount
    #         lastCol = col
    #         while board[rowcount][col] != 0:
    #             rowcount -= 1
    #         first = board[rowcount][col]
    #         firstRow = rowcount
    #         firstCol = col
    #         for i in range(firstRow, lastRow):
    #             word = word + board[i][col].getLetter
    #         #boolCheck = boolCheck and checkDict(word)
        
    #     return boolCheck
    
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
    