import sys
sys.path.insert(0, 'C:/Users/Raymond/Documents/XA3/thetrifecta_scrabble/src/Model')
from tkinter import *
from Board import *
from Bag import *
from Player import *
from Rack import *
from Tiles import *
from boardChecks import *
from wordChecks import *
from endTurn import *

global turn, player1Rack, player2Rack, roundCount
turn = 1
roundCount = 0

#Initializing the introductory window to the scrabble game.
class frontEndMain:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1500x900")
        self.root.title("Scrabble")
        #root.iconbitmap(r'scrabbleS.ico')
        self.startF = Frame(self.root)
        self.introF = Frame(self.root)
        self.introF.grid(row = 0,column = 0)
        welcomeL = Label(self.introF, text = "Welcome to Scrabble")
        welcomeL.grid(row = 0, column = 0)

        instructionsB = Button(self.introF, text = "Instructions", command=lambda: frontEndMain.instructions(self))
        instructionsB.grid(row = 1, column = 0)

        startB = Button(self.introF, text = "Start Game", command=lambda: frontEndMain.getPlayerName(self))
        startB.grid(row = 2, column = 0)

        self.root.mainloop()

    # def scoreBoard(self):
    #     self.startF.destroy()
    #     self.introF.destroy()
    #     scoreBoardR = Toplevel()
    #     scoreBoardR.title('Score Board')
    #
    #     #Displays label with Scrabble Game instructions.
    #     #instrL = Label(instructR, text = strInstruct)
    #     #instrL.grid(row = 0, column = 0)
    #     #Closes the window once the button is pressed.
    #     closeB = Button(scoreBoardR, text = "Close Score Board", command = scoreBoardR.destroy)
    #     closeB.grid(row = 1, column = 0)

    # Method pops up window that display instructions to the player.
    def instructions(self):
        instructR = Toplevel()
        instructR.title('Instructions')

        strInstruct = """Instructions for Scrabble:
        You get a rack of 7 tiles to start the game. You must play words with these
        7 tiles so that each word formed vertically and horizontally is a word.

        \tNote: Whenever you play a word, make sure that it touches at least
        \tone other letter on the board (not diagonally.)
        \tThe first move must touch the star in the middle of the board.

        To make a move input the desired word and the starting location of the
        \t word on the board by specifying the row and column number.
        \t Also enter the direction, indicated by writing
        \t "DOWN" for vertical and "RIGHT" for horizontal tile.
        Special Score Tiles:
        \tTWS (triple word score): Multiplies your score for that turn by 3.
        \tDWS (double word score): Multiplies your score for that turn by 2.
        \tTLS (triple letter score): Multiplies your score for that letter by 3.
        \tDLS (double letter score): Multiplies your score for that letter by 2.

        Once you play a word, your rack will be automatically updated with tiles
        \t so that you have seven again.
        The game ends when there are no tiles left in the bag."""
        #Displays label with Scrabble Game instructions.
        instrL = Label(instructR, text = strInstruct)
        instrL.grid(row = 0, column = 0)
        #Closes the window once the button is pressed.
        closeB = Button(instructR, text = "Close Instructions", command = instructR.destroy)
        closeB.grid(row = 1, column = 0)

    #Allows the player to enter their names and stores the values.
    def getPlayerName(self):
        self.introF.grid_remove()
        self.startF.grid(row = 0, column = 0)
        p1L = Label(self.startF, text = "Enter Name of Player One")
        p1L.grid(row = 0, column = 0)
        play1E = Entry(self.startF)
        play1E.grid(row = 0, column = 1)

        p2L = Label(self.startF, text = "Enter Name of Player Two")
        p2L.grid(row = 2, column = 0)
        play2E = Entry(self.startF)
        play2E.grid(row = 2, column = 1)

        playB = Button(self.startF, text = "Let's play", command = lambda: BoardFrame.scrabbleBoard(self.root, self.startF, play1E.get(), play2E.get()))
        playB.grid(row = 3, column = 1)
    
    def destroyWindow(self):
        self.startF.destroy()
        self.introF.destroy()

class BoardFrame:
    global tileArray

    tileArray = []
    curWord = ""
    curRow = 0
    curCol = 0
    curDir = ""
    # def getMove(word, row, col, dir):
    #   print(word)
    #   print(row)
    #   print(col)
    #   print(dir)
    #     curWord = word
    #     curRow = row
    #     curCol = col
    #     curDir = dir

    def updateGUI(updateList):
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
            if (turnLabel['text'] == "Player " + p1Name + "'s turn"):
                turnLabel.configure(text = "Player " + p2Name + "'s turn")
            else:
                turnLabel.configure(text = "Player " + p1Name + "'s turn")
            if turn == 1:
                player2Rack = player2.rack.getRackStr()
                rackLabel.configure(text = player2Rack)
                turn = 2
            elif turn == 2:
                player1Rack = player1.rack.getRackStr()
                rackLabel.configure(text = player1Rack)
                turn = 1
            roundCount += 1
    
    def exchangeTiles(exchangeTiles, label, turnLabel):
        global turn, roundCount
        if (turnLabel['text'] == "Player " + p1Name + "'s turn"):
                turnLabel.configure(text = "Player " + p2Name + "'s turn")
        else:
                turnLabel.configure(text = "Player " + p1Name + "'s turn")
        if turn == 1:
            endTurn.exchangeTile(exchangeTiles, player1.rack)
            player2Rack = player2.rack.getRackStr()
            label.configure(text = player2Rack)
            turn = 2
        else:
            endTurn.exchangeTile(exchangeTiles, player2.rack)
            player1Rack = player1.rack.getRackStr()
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
            winnerStr =  p1Name + " is the winner!"
            #winnerL.configure(text = p1Name + " is the winner!")
         else:
            winnerStr =  p2Name + " is the winner!"
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
         

    def completeTurn(root, frame, word, row, col, dir, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL):
        global turn, roundCount
        winState = endTurn.checkWinState(player1.rack, player2.rack, mainBag)
        if winState:
            #popup winner and destroy all windows
            BoardFrame.scoreBoard(root, frame, score1Label, score2Label)
        else:
            dirLower = dir.lower()
            wordUp = word.upper()
            score = endTurn.calculateScore(row, col, dirLower, wordUp)
            player.increaseScore(score)
            #use to configure button to have correct letters

            frontList = endTurn.updateFrontBoard(row, col, dirLower, wordUp)
            mainBoard.updateBackBoard(row, col, dirLower, wordUp)
            print(mainBoard.getBoard())
            BoardFrame.updateGUI(frontList)
            endTurn.removeTile(wordUp, player.rack)
            validMoveL.configure(text = "")
            roundCount += 1
            if (turnLabel['text'] == "Player " + p1Name + "'s turn"):
                turnLabel.configure(text = "Player " + p2Name + "'s turn")
                score1Label.configure(text = player.getScore())
            else:
                turnLabel.configure(text = "Player " + p1Name + "'s turn")
                score2Label.configure(text = player.getScore())
            if turn == 1:
                player2Rack = player2.rack.getRackStr()
                rackLabel.configure(text = player2Rack)
                turn = 2
            elif turn == 2:
                player1Rack = player1.rack.getRackStr()
                rackLabel.configure(text = player1Rack)
                turn = 1

    def endChecks(root, frame, word, row, col, dir, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters):
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
        BoardFrame.clearEntry(inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE)
        if validTurn:
            if dirLower == "down":
                #validTurn = True
                validTurn = checkBoardDown.downCheck(row, col, wordUp, mainBoard.getBoard(), roundCount)
                
                if validTurn:
                    BoardFrame.completeTurn(root, frame, wordUp, row, col, dirLower, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL)
                else:
                    #label popup for try again
                    #print("Try again")
                    print("failure in down")
                    validMoveL.configure(text = "Invalid move please try again")

            elif dirLower == "right":
                #validTurn = True 
                validTurn = checkBoardRight.rightCheck(row, col, wordUp, mainBoard.getBoard(), roundCount)
                print(validTurn, "dir right")
                if validTurn:
                    BoardFrame.completeTurn(root, frame, wordUp, row, col, dirLower, player, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, validMoveL)
                else:
                    #label popup for try again
                    #print("Try again")
                    print("failure in dir right")
                    validMoveL.configure(text = "Invalid move please try again")
        else:
            #label popup for try again
            #print("Try again")
            print("failure in shared")
            validMoveL.configure(text = "Invalid move please try again")

    def endMove(root, frame, word, row, col, dir, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters):
        global turn
        dirLower = dir.lower()
        wordUp = word.upper()
        validTurn = False
        winState = False
        print(word + "," + row + "," + col + "," + dir + str(turn))
        if turn == 1:
            BoardFrame.endChecks(root, frame, wordUp, row, col, dirLower, player1, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters)
        elif turn == 2:
            BoardFrame.endChecks(root, frame, wordUp, row, col, dirLower, player2, rackLabel, score1Label, score2Label, turnLabel, inputWordE, inputRowE, inputColE, inputDirE,inputWordSharedE, inputWordExchangeE, validMoveL, sharedLetters)
    def updateLabelText(self, label):
        if (label['text'] == "Player " + p1Name + "'s turn"):
            label.configure(text = "Player " + p2Name + "'s turn")
        else:
            label.configure(text = "Player " + p1Name + "'s turn")

    def scrabbleBoard(root, frame, player1Name, player2Name):
        #Hide the playerInput grid
        frame.grid_remove()
        #Storing the names of players for the turn label.
        global p1Name, p2Name, turn
        p1Name = player1Name
        p2Name = player2Name

        #Creating the frame that the Scrabble game is played on.
        boardF = Frame(root)
        boardF.grid(row = 0,column = 0)
        #Creating labels for the outside of the board.
        #Creating empty label for spacing purposes.
        emptyL1 = Label(boardF, text = " ")
        emptyL1.grid(row = 0, column = 0)
        #Loop that creates the labels for the columns of the board.
        for col in range(1, 16):
            boardLabel(boardF, 0, col, str(col-1))
        #Loop that creates the labels for the rows of the board.
        for row in range(1, 16):
            boardLabel(boardF, row, 0, str(row-1))

        #Loop that creates the buttons that make up the board of the game.
        #Creating the side panel for playing the game.
        #Creating a turn label that tells which player's turn it currently is.
        turnL = Label(boardF, text = "Player " + str(p1Name) + "'s turn")
        turnL.grid(row = 2, column = 17)
        #Creating labels for the player's score
        p1ScoreL = Label(boardF, text = str(p1Name) + "'s Score")
        p1ScoreL.grid(row = 3, column = 17)
        p2ScoreL = Label(boardF, text = str(p2Name) + "'s Score")
        p2ScoreL.grid(row = 3, column = 18)
        #labels for the values of the score
        p1ScoreValL = Label(boardF, text = "0")
        p1ScoreValL.grid(row = 4, column = 17)
        p2ScoreValL = Label(boardF, text = "0")
        p2ScoreValL.grid(row = 4, column = 18)
        #Buttons for end move and exchange tiles.
        endMoveB = Button(boardF, text = "End Move", command=lambda: BoardFrame.endMove(root, boardF, inputWordE.get(),
        inputRowE.get(), inputColE.get(), inputDirE.get(), playerRackL, p1ScoreValL, p2ScoreValL, turnL,
        inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE, validMoveL, inputWordSharedE.get()))
        endMoveB.grid(row = 11, column = 17)
        skipTurnB = Button(boardF, text = "Skip Turn", command=lambda: BoardFrame.skipTurn(turnL, playerRackL))
        skipTurnB.grid(row = 11, column = 18)
        exchangeTilesB = Button(boardF, text = "Exchange Tiles", command=lambda: BoardFrame.exchangeTiles(inputWordExchangeE.get(), playerRackL, turnL))
        exchangeTilesB.grid(row = 11, column = 19)
        #empty label as a buffer
        emptyL2 = Label(boardF, text = " ")
        emptyL2.grid(row = 0,column = 16,rowspan = 15)
        #The label and input for word, row, column and direction.
        playerRackL = Label(boardF, text = player1Rack)
        playerRackL.grid(row = 5, column = 17)
        validMoveL = Label(boardF, text = "")
        validMoveL.grid(row = 6, column = 17)
        inputWordL = Label(boardF, text = "Enter word")
        inputWordL.grid(row = 7, column = 17)
        inputWordE = Entry(boardF)
        inputWordE.grid(row = 7, column = 18)
        inputWordSharedL = Label(boardF, text = "Enter Shared Letters")
        inputWordSharedL.grid(row = 7, column = 19)
        inputWordSharedE = Entry(boardF)
        inputWordSharedE.grid(row = 7, column = 20)
        inputWordExchangeL = Label(boardF, text = "Enter Tiles to Exchange")
        inputWordExchangeL.grid(row = 8, column = 19)
        inputWordExchangeE = Entry(boardF)
        inputWordExchangeE.grid(row = 8, column = 20)
        inputRowL = Label(boardF, text = "Enter row")
        inputRowL.grid(row = 8, column = 17)
        inputRowE = Entry(boardF)
        inputRowE.grid(row = 8, column = 18)
        inputColL = Label(boardF, text = "Enter column")
        inputColL.grid(row = 9, column = 17 )
        inputColE = Entry(boardF)
        inputColE.grid(row = 9, column = 18)
        inputDirL = Label(boardF, text = "Enter direction")
        inputDirL.grid(row = 10, column = 17)
        inputDirE = Entry(boardF)
        inputDirE.grid(row = 10, column = 18)

        #i_word = inputWordE.get()

        for row in range(1, 16):
            tileRow = []
            for column in  range(1, 16):
                tile = ColorButton(boardF, "floral white", row, column, "")
                tileRow.append(tile)
            tileArray.append(tileRow)

        tileArray[0][0].configure("text", "TWS")
        tileArray[0][0].configure("bg", "LightGoldenrod1")
        tileArray[0][3].configure("text", "DLS")
        tileArray[0][3].configure("bg", "Light Blue")
        tileArray[0][7].configure("text", "TWS")
        tileArray[0][7].configure("bg", "LightGoldenrod1")
        tileArray[0][11].configure("text", "DLS")
        tileArray[0][11].configure("bg", "Light Blue")
        tileArray[0][14].configure("text", "TWS")
        tileArray[0][14].configure("bg", "LightGoldenrod1")

        tileArray[1][1].configure("text", "DWS")
        tileArray[1][1].configure("bg", "Pink")
        tileArray[1][5].configure("text", "TLS")
        tileArray[1][5].configure("bg", "pale green")
        tileArray[1][9].configure("text", "TLS")
        tileArray[1][9].configure("bg", "pale green")
        tileArray[1][13].configure("text", "DWS")
        tileArray[1][13].configure("bg", "Pink")

        tileArray[2][2].configure("text", "DWS")
        tileArray[2][2].configure("bg", "Pink")
        tileArray[2][6].configure("text", "DLS")
        tileArray[2][6].configure("bg", "Light Blue")
        tileArray[2][8].configure("text", "DLS")
        tileArray[2][8].configure("bg", "Light Blue")
        tileArray[2][12].configure("text", "DWS")
        tileArray[2][12].configure("bg", "Pink")

        tileArray[3][0].configure("text", "DLS")
        tileArray[3][0].configure("bg", "Light Blue")
        tileArray[3][3].configure("text", "DWS")
        tileArray[3][3].configure("bg", "Pink")
        tileArray[3][7].configure("text", "DLS")
        tileArray[3][7].configure("bg", "Light Blue")
        tileArray[3][11].configure("text", "DWS")
        tileArray[3][11].configure("bg", "Pink")
        tileArray[3][14].configure("text", "DLS")
        tileArray[3][14].configure("bg", "Light Blue")

        tileArray[4][4].configure("text", "DWS")
        tileArray[4][4].configure("bg", "Pink")
        tileArray[4][10].configure("text", "DWS")
        tileArray[4][10].configure("bg", "Pink")

        tileArray[5][1].configure("text", "TLS")
        tileArray[5][1].configure("bg", "pale green")
        tileArray[5][5].configure("text", "TLS")
        tileArray[5][5].configure("bg", "pale green")
        tileArray[5][9].configure("text", "TLS")
        tileArray[5][9].configure("bg", "pale green")
        tileArray[5][13].configure("text", "TLS")
        tileArray[5][13].configure("bg", "pale green")

        tileArray[6][2].configure("text", "DLS")
        tileArray[6][2].configure("bg", "Light Blue")
        tileArray[6][6].configure("text", "DLS")
        tileArray[6][6].configure("bg", "Light Blue")
        tileArray[6][8].configure("text", "DLS")
        tileArray[6][8].configure("bg", "Light Blue")
        tileArray[6][12].configure("text", "DLS")
        tileArray[6][12].configure("bg", "Light Blue")

        tileArray[7][0].configure("text", "TWS")
        tileArray[7][0].configure("bg", "LightGoldenrod1")
        tileArray[7][3].configure("text", "DLS")
        tileArray[7][3].configure("bg", "Light Blue")
        tileArray[7][7].configure("text", "★")
        tileArray[7][7].configure("bg", "Pink")
        tileArray[7][11].configure("text", "DLS")
        tileArray[7][11].configure("bg", "Light Blue")
        tileArray[7][14].configure("text", "TWS")
        tileArray[7][14].configure("bg", "LightGoldenrod1")

        tileArray[8][2].configure("text", "DLS")
        tileArray[8][2].configure("bg", "Light Blue")
        tileArray[8][6].configure("text", "DLS")
        tileArray[8][6].configure("bg", "Light Blue")
        tileArray[8][8].configure("text", "DLS")
        tileArray[8][8].configure("bg", "Light Blue")
        tileArray[8][12].configure("text", "DLS")
        tileArray[8][12].configure("bg", "Light Blue")

        tileArray[9][1].configure("text", "TLS")
        tileArray[9][1].configure("bg", "pale green")
        tileArray[9][5].configure("text", "TLS")
        tileArray[9][5].configure("bg", "pale green")
        tileArray[9][9].configure("text", "TLS")
        tileArray[9][9].configure("bg", "pale green")
        tileArray[9][13].configure("text", "TLS")
        tileArray[9][13].configure("bg", "pale green")

        tileArray[10][4].configure("text", "DWS")
        tileArray[10][4].configure("bg", "Pink")
        tileArray[10][10].configure("text", "DWS")
        tileArray[10][10].configure("bg", "Pink")

        tileArray[11][0].configure("text", "DLS")
        tileArray[11][0].configure("bg", "Light Blue")
        tileArray[11][3].configure("text", "DWS")
        tileArray[11][3].configure("bg", "Pink")
        tileArray[11][7].configure("text", "DLS")
        tileArray[11][7].configure("bg", "Light Blue")
        tileArray[11][11].configure("text", "DWS")
        tileArray[11][11].configure("bg", "Pink")
        tileArray[11][14].configure("text", "DLS")
        tileArray[11][14].configure("bg", "Light Blue")

        tileArray[12][2].configure("text", "DWS")
        tileArray[12][2].configure("bg", "Pink")
        tileArray[12][6].configure("text", "DLS")
        tileArray[12][6].configure("bg", "Light Blue")
        tileArray[12][8].configure("text", "DLS")
        tileArray[12][8].configure("bg", "Light Blue")
        tileArray[12][12].configure("text", "DWS")
        tileArray[12][12].configure("bg", "Pink")

        tileArray[13][1].configure("text", "DWS")
        tileArray[13][1].configure("bg", "Pink")
        tileArray[13][5].configure("text", "TLS")
        tileArray[13][5].configure("bg", "pale green")
        tileArray[13][9].configure("text", "TLS")
        tileArray[13][9].configure("bg", "pale green")
        tileArray[13][13].configure("text", "DWS")
        tileArray[13][13].configure("bg", "Pink")

        tileArray[14][0].configure("text", "TWS")
        tileArray[14][0].configure("bg", "LightGoldenrod1")
        tileArray[14][3].configure("text", "DLS")
        tileArray[14][3].configure("bg", "Light Blue")
        tileArray[14][7].configure("text", "TWS")
        tileArray[14][7].configure("bg", "LightGoldenrod1")
        tileArray[14][11].configure("text", "DLS")
        tileArray[14][11].configure("bg", "Light Blue")
        tileArray[14][14].configure("text", "TWS")
        tileArray[14][14].configure("bg", "LightGoldenrod1")

class boardLabel:
    def __init__(self, frame, row, column, text):
        self.frame = frame
        self.row = row
        self.column = column
        self.text = text

        self.label = Label(self.frame, text = self.text)
        self.label.grid(row = self.row, column = self.column)

class ColorButton:
        def __init__(self, frame, colour, row, column, text):
            self.frame = frame
            self.colour = colour
            self.row = row
            self.column = column
            self.text = text

            if colour == "":
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, text=self.text)
            else:
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, bg = self.colour, text=self.text)


            self.button.grid(row = self.row, column = self.column)
        def configure(self, attribute, text):
            self.button[attribute] = text

#Initializing the back end components of the game.
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

frontEndView = frontEndMain()
