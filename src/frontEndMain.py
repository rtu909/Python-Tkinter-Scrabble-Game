from tkinter import *
from example import *
from boardGUI import *

#Naming Conventions for Variables
#ending in R for Windows
#ending in L for labels
#inding in B for buttons

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

		To play a tile, click and drag the tile to the board.
		\tNote: When you play a tile, make sure that it snaps into a space.
		\tIf it doesn't, then it didn't place and you have to do it again.
		"#" tiles are blank tiles. They can be played as any letter.
		If you can't find any words to make, you can exchange. Exchanging
		You get a certain amount of points based on the letters you played.
		Special Score Tiles:
		\tTWS (triple word score): Multiplies your score for that turn by 3.
		\tDWS (double word score): Multiplies your score for that turn by 2.
		\tTLS (triple letter score): Multiplies your score for that letter by 3.
		\tDLS (double letter score): Multiplies your score for that letter by 2.

		Once you play a word, you draw tiles until you have seven again.
		The game ends when there are no tiles left in the bag."""
		#Displays label with Scrabble Game instructions.
		instrL = Label(instructR, text = strInstruct)
		instrL.grid(row = 0, column = 0)
		#Closes the window once the button is pressed.
		closeB = Button(instructR, text = "Close Instructions", command = instructR.destroy)
		closeB.grid(row = 1, column = 0)

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


	
