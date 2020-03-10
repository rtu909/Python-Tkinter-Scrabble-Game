from Tiles import *
from Rack import *
## @file endTurn.py
#  @author Lucia Cristiano
#  @brief This program performs various functions neeeded to update the front end after a move is validated. 
#  @date Feb.12,2020
class endTurn:

    ## @brief updates the back end version of the board with the valid word.
    #  @param1 an integer that represents the row of an the back end array.
    #  @param2 an integer that represents the column of the back end array.
    #  @param3 a string that represent the direction of the word placed on the board.
    #  @param4 a string that represents the word being placed on the board.
    #  @returns a list of tuples representing the row, column and text needed to be changed in the front end
    def updateFrontBoard(self, row, col, dir, word):
        frontList = []
        dirLower = dir.lower()
        if(dirLower == "right"):
            countCol = int(col)
            for char in word:
                configTuple = (int(row), countCol, char)
                frontList.append(configTuple)
                countCol += 1 
        elif(dirLower == "down"):
            countRow = int(row)
            for char in word:
                configTuple = (countRow, int(col), char)
                frontList.append(configTuple)
                countRow += 1
        return frontList
    
    def removeTile(self, word, rack):
        wordUp = word.upper()
        for letter in wordUp:
            for tile in rack.getRackArr():
                if tile.getLetter() == letter:
                    rack.removeFromRack(tile)
        rack.replenishRack()

    def calculateScore(self, row, col, dir, word):
        #Set list used in score calculations.
        #List of premium tiles.
        TWS = [(0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14)]
        DWS = [(1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4),  (13,13), (12, 12), (11,11), (10,10), (7,7)]
        TLS = [(1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9)]
        DLS = [(0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11)]

        #List of letters and their scores.
        LETTER_VALUES = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5,    "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,"Y": 4, "Z": 10}

        multiplierWord = 1
        score = 0
        dirLower = dir.lower()
        if dirLower == "right":
            countCol = int(col)
            for char in word:
                checkPremiumTuple = (int(row), countCol)
                if checkPremiumTuple in TLS:
                    score += LETTER_VALUES[char]*3
                elif checkPremiumTuple in DLS:
                    score += LETTER_VALUES[char]*2
                elif checkPremiumTuple in TWS:
                    multiplierWord *= 3
                    score += LETTER_VALUES[char]
                elif checkPremiumTuple in DWS:
                    multiplierWord *= 2
                    score += LETTER_VALUES[char]
                else:
                    score += LETTER_VALUES[char]
                countCol += 1
            score *= multiplierWord
        elif dirLower == "down":
            countRow = int(row)
            for char in word:
                checkPremiumTuple = (int(countRow), int(col))
                if checkPremiumTuple in TLS:
                    score += LETTER_VALUES[char]*3
                elif checkPremiumTuple in DLS:
                    score += LETTER_VALUES[char]*2
                elif checkPremiumTuple in TWS:
                    multiplierWord *= 3
                    score += LETTER_VALUES[char]
                elif checkPremiumTuple in DWS:
                    multiplierWord *= 2
                    score += LETTER_VALUES[char]
                else:
                    score += LETTER_VALUES[char]
                countRow += 1
            score *= multiplierWord
        return score

    ## @brief checks if the game has been won
    #  @return returns a bool to represent win state or not 
    def checkWinState(self, rack1, rack2, bag):
        emptyRack = (rack1.getRackLength() == 0) or (rack2.getRackLength() == 0)
        if  emptyRack and bag.getRemainingTiles() == 0:
            return True
        else:
            return False
