from wordChecks import *
class checkBoardRight:
    def occupiedTile(self, row, col, input, arr):
        colcount = 0
        for char in input:
            if arr[row][colcount] == "0":
                colcount += 1
            elif arr[row][colcount] == char: #matches char
                colcount += 1
            else:   
                return False
        return True
    
    def neighbourTiles(self, row, col, input, arr):
        colcount = 0
        rowcount = 0
        boolCheck = True
        for char in input:
            while arr[row][colcount] != "0":
                colcount += 1
            last = arr[row][colcount]
            lastRow = row
            lastCol = colcount
            while arr[row][colcount] != "0":
                colcount -= 1
            first = arr[row][colcount]
            firstRow = row
            firstCol = colcount
            for i in range(first.col, last.col):
                word = word + arr[row][i].getLetter
            boolCheck = boolCheck and checkInDict(word)
        
        return boolCheck
            
        
    def outOfBounds(self, row, col, input, arr):
        return (col <= 14 and row <= 14 and row + len(input) <= 14)
        
    def rightCheck(self, row, col, input, arr):
        return occupiedTile(row, col, input, arr) and neighbourTiles(row, col, input, arr) and outOfBounds(row, col, input, arr)

class checkBoardDown:
    def occupiedTile(self, row, col, input, arr):
        rowcount = 0
        for char in input:
            if arr[rowcount][col] == "0":
                rowcount += 1
            elif arr[rowcount][col] == char: #matches char
                rowcount += 1
            else:    
                return False
        return True
    
    def neighbourTiles(self, row, col, input, arr):
        colcount = 0
        rowcount = 0
        boolCheck = True
        for char in input:
            while arr[rowcount][col] != "0":
                rowcount += 1
            last = arr[rowcount][col]
            lastRow = rowcount
            lastCol = col
            while arr[rowcount][col] != 0:
                rowcount -= 1
            first = arr[rowcount][col]
            firstRow = rowcount
            firstCol = col
            for i in range(firstRow, lastRow):
                word = word + arr[i][col].getLetter
            #boolCheck = boolCheck and checkDict(word)
        
        return boolCheck
    
    def outOfBounds(self, row, col, input, arr):
        return (col <= 14 and row <= 14 and col + len(input) <= 14)
        
    def downCheck(self, row, col, input, arr):
        return occupiedTile(row, col, input, arr) and neighbourTiles(row, col, input, arr) and outOfBounds(row, col, input, arr)
    