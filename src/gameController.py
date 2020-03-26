from tkinter import *
from Board import *
from Bag import *
from Player import *
from Rack import *
from Tiles import *
from boardChecks import *
from wordChecks import *
from endTurn import *

turn = 1
roundCount = 0
player1Rack = ""
player2Rack = ""
p1 = ""
p2 = ""
class backEnd:
    mainBoard = Board()
    mainBag = Bag()
    checkBoardRight = checkBoardRight()
    checkBoardDown = checkBoardDown()
    endTurn = endTurn()
    player1 = Player(mainBag)
    player2 = Player(mainBag)
    player1Rack = player1.rack.getRackStr()
    player2Rack = player2.rack.getRackStr()

    def updateGUI(updateList, tileArray):
        for tuple in updateList:
            tileArray[tuple[0]][tuple[1]].configure("text", str(tuple[2]))

    def clearEntry(entryBoxes):
        entryBoxes[0].delete(0, "end")
        entryBoxes[1].delete(0, "end")
        entryBoxes[2].delete(0, "end")
        entryBoxes[3].delete(0, "end")
        entryBoxes[4].delete(0, "end")
        entryBoxes[5].delete(0, "end")

    def skipTurn(turnLabel, rackLabel):
        global turn, roundCount, p1, p2
        if roundCount != 0:
            if (turnLabel['text'] == "Player " + p1 + "'s turn"):
                turnLabel.configure(text = "Player " + p2 + "'s turn")
            else:
                turnLabel.configure(text = "Player " + p1 + "'s turn")
            if turn == 1:
                player2Rack = backEnd.player2.rack.getRackStr()
                rackLabel.configure(text = player2Rack)
                turn = 2
            elif turn == 2:
                player1Rack = backEnd.player1.rack.getRackStr()
                rackLabel.configure(text = player1Rack)
                turn = 1
            roundCount += 1

    def exchangeTiles(exchangedTiles, label, turnLabel, entryBoxes, labels):
        global turn, roundCount, p1, p2
        validMoveL = labels[4]
        validMove = True
        exchangedTiles = exchangedTiles.upper()
        if (turnLabel['text'] == "Player " + p1 + "'s turn"):
                turnLabel.configure(text = "Player " + p2 + "'s turn")
        else:
                turnLabel.configure(text = "Player " + p1 + "'s turn")
        if turn == 1:
            player1Rack = backEnd.player1.rack.getRackStr()
            for char in exchangedTiles:
                if char not in player1Rack:
                    validMoveL.configure(text = "Invalid Exchange Tile Not in Rack")
                    validMove = validMove and False
            if validMove:
                validMoveL.configure(text = "")
                endTurn.exchangeTile(exchangedTiles, backEnd.player1.rack)
                player2Rack = backEnd.player2.rack.getRackStr()
                label.configure(text = player2Rack)
                turn = 2
        else:
            player2Rack = backEnd.player2.rack.getRackStr()
            for char in exchangedTiles:
                if char not in player2Rack:
                    validMoveL.configure(text = "Invalid Exchange Tile Not in Rack")
                    validMove = validMove and False
            if validMove:
                validMoveL.configure(text = "")
                endTurn.exchangeTile(exchangedTiles, backEnd.player2.rack)
                player1Rack = backEnd.player1.rack.getRackStr()
                label.configure(text = player1Rack)
                turn = 1
        backEnd.clearEntry(entryBoxes)
        #roundCount += 1

    def scoreBoard(root, frame, score1Label, score2Label):
         global p1, p2
         winnerStr = ""
         if (int(score1Label['text']) > int(score2Label['text'])):
            winnerStr =  p1 + " is the winner!"
            winnerL.configure(text = p1 + " is the winner!")
         else:
            winnerStr =  p2 + " is the winner!"
            winnerL.configure(text = p2 + " is the winner!")
         frame.destroy()
         root.destroy()
         scoreBoardR = Tk()
         scoreBoardR.title('Score Board')
         winnerL = Label(scoreBoardR, text = "")
         winnerL.grid(row = 0, column = 0)
         winnerL.configure(text = winnerStr)
         closeB = Button(scoreBoardR, text = "Close Score Board", command = scoreBoardR.destroy)
         closeB.grid(row = 1, column = 0)
         scoreBoardRoot.mainloop()


    def completeTurn(root, frame, playerMove, label, entryBoxes, player, tileArray):
        global turn, roundCount, p1, p2
        winState = False
        winState = endTurn.checkWinState(backEnd.player1.rack, backEnd.player2.rack, backEnd.mainBag)
        # if roundCount == 3:
        #     winState = True
        if winState:
            #popup winner and destroy all windows
            score1Label = label[1]
            score2Label = label[2]
            backEnd.scoreBoard(root, frame, score1Label, score2Label)
        else:
            dirLower = playerMove[3].lower()
            wordUp = playerMove[0].upper()
            sharedLetters = playerMove[4]
            row = playerMove[1]
            col = playerMove[2]
            validMoveL = label[4]
            turnLabel = label[3]
            rackLabel = label[0]
            score1Label = label[1]
            score2Label = label[2]
            score = endTurn.calculateScore(wordUp, row, col, dirLower)
            player.increaseScore(score)
            #use to configure button to have correct letters
            frontList = endTurn.updateFrontBoard(wordUp, row, col, dirLower)
            backEnd.mainBoard.updateBackBoard(wordUp, row, col, dirLower)
            backEnd.updateGUI(frontList, tileArray)
            endTurn.removeTile(wordUp, player.rack)
            validMoveL.configure(text = "")
            backEnd.clearEntry(entryBoxes)
            roundCount += 1
            if (turnLabel['text'] == "Player " + p1 + "'s turn"):
                turnLabel.configure(text = "Player " + p2 + "'s turn")
                score1Label.configure(text = player.getScore())
            else:
                turnLabel.configure(text = "Player " + p1 + "'s turn")
                score2Label.configure(text = player.getScore())
            if turn == 1:
                player2Rack = backEnd.player2.rack.getRackStr()
                rackLabel.configure(text = player2Rack)
                turn = 2
            elif turn == 2:
                player1Rack = backEnd.player1.rack.getRackStr()
                rackLabel.configure(text = player1Rack)
                turn = 1

    def endChecks(root, frame, playerMove, labels, entryBoxes, player, tileArray):
        global roundCount
        dirLower = playerMove[3].lower()
        wordUp = playerMove[0].upper()
        sharedLetters = playerMove[4]
        row = playerMove[1]
        col = playerMove[2]
        validMoveL = labels[4]
        validTurn = False
        if sharedLetters == "":
            validTurn = checkRack(wordUp, player.rack.getRackStr())
            validTurn = validTurn and checkInDict(wordUp)
        else:
            rackWord = wordUp
            for char in sharedLetters:
                rackWord = rackWord.replace(char, "")
            validTurn = checkRack(rackWord, player.rack.getRackStr())
            validTurn = validTurn and checkInDict(wordUp)
        backEnd.clearEntry(entryBoxes)
        if validTurn:
            if dirLower == "down":
                validTurn = checkBoardDown.downCheck(wordUp, row, col, backEnd.mainBoard.getBoard(), roundCount)
                if validTurn:
                    backEnd.completeTurn(root, frame, playerMove, labels, entryBoxes, player, tileArray)
                else:
                    validMoveL.configure(text = "Invalid move please try again")

            elif dirLower == "right":
                validTurn = checkBoardRight.rightCheck(wordUp, row, col, backEnd.mainBoard.getBoard(), roundCount)
                if validTurn:
                    backEnd.completeTurn(root, frame, playerMove, labels, entryBoxes, player, tileArray)
                else:
                    validMoveL.configure(text = "Invalid move please try again")
            else:
                validMoveL.configure(text = "Invalid move please try again")
        else:
            validMoveL.configure(text = "Invalid move please try again")

    def endMove(root, frame, word, row, col, dir, sharedLetters, labels, entryBoxes, tileArray, p1Name, p2Name):
        global turn
        global p1, p2
        p1 = p1Name
        p2 = p2Name
        playerMove = (word, row, col, dir, sharedLetters)
        if turn == 1:
            backEnd.endChecks(root, frame, playerMove, labels, entryBoxes, backEnd.player1, tileArray)
        elif turn == 2:
            backEnd.endChecks(root, frame, playerMove, labels, entryBoxes, backEnd.player2, tileArray)
