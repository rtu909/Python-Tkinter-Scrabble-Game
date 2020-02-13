class checkBoardRight:
    def occupiedTile(row, col, input, arr):
        colcount = 0
        for char in input:
            if arr[row][colcount] == 0:
                colcount++
            else if arr[row][colcount].getLetter == char: #matches char
                colcount++
            else    
                return false
    
    def neighbourTiles(row, col, input, arr):
        colcount = 0
        rowcount = 0
        boolCheck = true
        for char in input:
            while arr[row][colcount] != 0:
                colcount++
            last = arr[row][colcount]
            while arr[row][colcount] != 0:
                colcount--
            first = arr[row][colcount]
            for i in range(first.col, last.col):
                word = word + arr[i][col].getLetter
            boolCheck = boolCheck and checkDict(word)
        
        return boolCheck
            
        
    def outOfBounds(row, col, input, arr):
        return (col <= 14 and row <= 14 and row + len(input) <= 14)

class checkBoardDown:
    def occupiedTile(row, col, input, arr):
        rowcount = 0
        for char in input:
            if arr[rowcount][col] == 0:
                rowcount++
            else if arr[rowcount][col].getLetter == char: #matches char
                rowcount++
            else    
                return false
    
    def neighbourTiles(row, col, input, arr):
        colcount = 0
        rowcount = 0
        boolCheck = true
        for char in input:
            while arr[rowcount][col] != 0:
                rolcount++
            last = arr[rowcount][col]
            lastRow = rowcount
            lastCol = col
            while arr[rowcount][col] != 0:
                rolcount--
            first = arr[rowcount][col]
            firstRow = rowcount
            firstCol = col
            for i in range(firstRow, lastRow):
                word = word + arr[i][col].getLetter
            boolCheck = boolCheck and checkDict(word)
        
        return boolCheck
    
    def outOfBounds(row, col, input, arr):
        return (col <= 14 and row <= 14 and col + len(input) <= 14)
    