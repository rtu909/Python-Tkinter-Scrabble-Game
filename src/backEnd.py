from tkinter import *
from Board import *
from Bag import *
from Player import *
from Rack import *
from Tiles import *
from boardChecks import *
from wordChecks import *
from endTurn import *

global turn, player1Rack, player2Rack, roundCount, p1,p2
turn = 1
roundCount = 0

class backEnd:

    mainBoard = Board()
    mainBag = Bag()
    wordChecks = wordChecks()
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

    def clearEntry(inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE):
        inputWordE.delete(0, "end")
        inputRowE.delete(0, "end")
        inputColE.delete(0, "end")
        inputDirE.delete(0, "end")
        inputWordSharedE.delete(0, "end")
        inputWordExchangeE.delete(0, "end")

    def skipTurn(turnLabel, rackLabel):
        global turn, roundCount
        print("working")
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

    def exchangeTiles(exchangeTiles, label, turnLabel):
        global turn, roundCount, p1, p2
        if (turnLabel['text'] == "Player " + p1 + "'s turn"):
                turnLabel.configure(text = "Player " + p2 + "'s turn")
        else:
                turnLabel.configure(text = "Player " + p1 + "'s turn")
        if turn == 1:
            endTurn.exchangeTile(exchangeTiles, backEnd.player1.rack)
            player2Rack = backEnd.player2.rack.getRackStr()
            label.configure(text = player2Rack)
            turn = 2
        else:
            endTurn.exchangeTile(exchangeTiles, backEnd.player2.rack)
            player1Rack = backEnd.player1.rack.getRackStr()
            label.configure(text = player1Rack)
            turn = 1
        roundCount += 1

    def scoreBoard(root, frame, score1Label, score2Label):
         #scoreBoardR = Toplevel()
         #scoreBoardR.title('Score Board')

         #winnerL = Label(scoreBoardR, text = "")
         #winnerL.grid(row = 0, column = 0)
         winnerStr = ""
         if (int(score1Label['text']) > int(score2Label['text'])):
            winnerStr =  p1 + " is the winner!"
            #winnerL.configure(text = p1Name + " is the winner!")
         else:
            winnerStr =  p2 + " is the winner!"
            #winnerL.configure(text = p2Name + " is the winner!")
         frame.destroy()
         root.destroy()
         scoreBoardR = Tk()
         #scoreBoardR = Toplevel(scoreBoardRoot)
         scoreBoardR.title('Score Board')
         winnerL = Label(scoreBoardR, text = "")
         winnerL.grid(row = 0, column = 0)
         winnerL.configure(text = winnerStr)
         closeB = Button(scoreBoardR, text = "Close Score Board", command = scoreBoardR.destroy)
         closeB.grid(row = 1, column = 0)
         scoreBoardRoot.mainloop()
         #Displays label with Scrabble Game instructions.
         #instrL = Label(instructR, text = strInstruct)
         #instrL.grid(row = 0, column = 0)
         #Closes the window once the button is pressed.


    def completeTurn(root, frame, word, row, col, dir, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL, tileArray):
        global turn, roundCount
        winState = endTurn.checkWinState(backEnd.player1.rack, backEnd.player2.rack, backEnd.mainBag)
        # if roundCount == 3:
        #     winState = True
        if winState:
            #popup winner and destroy all windows
            backEnd.scoreBoard(root, frame, score1Label, score2Label)
        else:
            dirLower = dir.lower()
            wordUp = word.upper()
            score = endTurn.calculateScore(row, col, dirLower, wordUp)
            player.increaseScore(score)
            #use to configure button to have correct letters

            frontList = endTurn.updateFrontBoard(row, col, dirLower, wordUp)
            backEnd.mainBoard.updateBackBoard(row, col, dirLower, wordUp)
            print(backEnd.mainBoard.getBoard())
            backEnd.updateGUI(frontList, tileArray)
            endTurn.removeTile(wordUp, player.rack)
            validMoveL.configure(text = "")
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

    def endChecks(root, frame, word, row, col, dir, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters, tileArray):
        global roundCount
        dirLower = dir.lower()
        wordUp = word.upper()
        if sharedLetters == "":
            validTurn = wordChecks.checkRack(wordUp, player.rack.getRackStr())
            validTurn = validTurn and wordChecks.checkInDict(wordUp)
            print("sharedletters", validTurn)
        else:
            rackWord = wordUp
            for char in sharedLetters:
                rackWord = rackWord.replace(char, "")
            validTurn = wordChecks.checkRack(rackWord, player.rack.getRackStr())
            validTurn = validTurn and wordChecks.checkInDict(wordUp)
        backEnd.clearEntry(inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE)
        if validTurn:
            if dirLower == "down":
                validTurn = checkBoardDown.downCheck(row, col, wordUp, backEnd.mainBoard.getBoard(), roundCount)
                if validTurn:
                    backEnd.completeTurn(root, frame, wordUp, row, col, dirLower, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL, tileArray)
                else:
                    print("failure in down")
                    validMoveL.configure(text = "Invalid move please try again")

            elif dirLower == "right":
                validTurn = checkBoardRight.rightCheck(row, col, wordUp, backEnd.mainBoard.getBoard(), roundCount)
                print(validTurn, "dir right")
                if validTurn:
                    backEnd.completeTurn(root, frame, wordUp, row, col, dirLower, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL, tileArray)
                else:
                    print("failure in dir right")
                    validMoveL.configure(text = "Invalid move please try again")
        else:
            print("failure in shared")
            validMoveL.configure(text = "Invalid move please try again")

    def endMove(root, frame, word, row, col, dir, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters, tileArray, p1Name, p2Name):
        global turn
        global p1, p2
        p1 = p1Name
        p2 = p2Name
        dirLower = dir.lower()
        wordUp = word.upper()
        validTurn = False
        winState = False
        print(word + "," + row + "," + col + "," + dir + str(turn))
        if turn == 1:
            backEnd.endChecks(root, frame, wordUp, row, col, dirLower, backEnd.player1, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters, tileArray)
        elif turn == 2:
            backEnd.endChecks(root, frame, wordUp, row, col, dirLower, backEnd.player2, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters, tileArray)
