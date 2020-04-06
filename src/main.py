from tkinter import *
from widgetCreation import *
from gameController import *

## @file main.py
#  @author The Trifecta
#  @brief This module the front end of the Scrabble game.
#  @date Apr.06,2020

## @brief Initializing the introductory window to the scrabble game.
class frontEndMain:

	## @brief initializes the window for the introduction of the Scrabble game.
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1500x900")
        self.root.title("Scrabble")
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

    ## @brief Method pops up window that display instructions to the player.
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
        \t to finsh your turn press the "END MOVE" button.
        \t To skip your turn, press the "SKIP TURN" button.
        \t To exchange tiles type the letters that you want to change
        \t with nothing to separate them. Then press the "EXCHANGE TILES" button.
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

    ## @brief Allows the player to enter their names and stores the values.
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

	## @brief #destroys the window when the game is done
    def destroyWindow(self):
        self.startF.destroy()
        self.introF.destroy()

class BoardFrame:
	## @brief initializes and maintains the scrabble board.
    #  @param1 root window in which game is being implemented.
    #  @param2 frame containing the various board components.
    #  @param3 player1's name.
    #  @param4 player2's name.
    def scrabbleBoard(root, frame, player1Name, player2Name):
        #Tile array used to access tiles to update them.
        global tileArray
        tileArray = []

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
            makeLabels(boardF, 0, col, str(col-1))
        #Loop that creates the labels for the rows of the board.
        for row in range(1, 16):
            makeLabels(boardF, row, 0, str(row-1))

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
        #Buttons for end move, skip turns and exchange tiles.
        endMoveB = Button(boardF, text = "End Move", command=lambda: backEnd.endMove(root, boardF, inputWordE.get(), inputRowE.get(), inputColE.get(), inputDirE.get(), inputWordSharedE.get(), labelTuple, entryTuple, tileArray, p1Name, p2Name))
        endMoveB.grid(row = 11, column = 17)
        skipTurnB = Button(boardF, text = "Skip Turn", command=lambda: backEnd.skipTurn(turnL, playerRackL))
        skipTurnB.grid(row = 11, column = 18)
        exchangeTilesB = Button(boardF, text = "Exchange Tiles", command=lambda: backEnd.exchangeTiles(inputWordExchangeE.get(), playerRackL, turnL, entryTuple, labelTuple))
        exchangeTilesB.grid(row = 11, column = 19)
        #empty label as a buffer
        emptyL2 = Label(boardF, text = " ")
        emptyL2.grid(row = 0,column = 16,rowspan = 15)
        #The label and input boxes for word, row, column and direction.
        playerRackL = Label(boardF, text = backEnd.player1Rack)
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
        #tuples of information to be passed into the game controller
        labelTuple = (playerRackL, p1ScoreValL, p2ScoreValL, turnL, validMoveL)
        entryTuple = (inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE)

        #creating tiles
        for row in range(1, 16):
            tileRow = []
            for column in  range(1, 16):
                tile = makeButtons(boardF, "floral white", row, column, "")
                tileRow.append(tile)
            tileArray.append(tileRow)

        #configuring tiles with colour and text
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

frontEndView = frontEndMain()
gameController = backEnd()
