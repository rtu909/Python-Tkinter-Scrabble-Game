from tkinter import *

#Naming Conventions for Variables
#ending in R for Windows
#ending in L for labels
#inding in B for buttons

root = Tk()
root.geometry("1500x700")
root.title("Scrabble")

def instructions():
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
    instrL = Label(instructR, text=strInstruct)
    instrL.grid(row=0, column=0)
    closeB = Button(instructR, text="Close Instructions", command=instructR.destroy)
    closeB.grid(row=1, column=0)


introF = Frame(root)
introF.grid(row=0,column=0)
welcomeL = Label(introF, text="Welcome to Scrabble")
welcomeL.grid(row=0, column=0)

def startGame():
    introF.grid_remove()
    startF = Frame(root)
    playB = Button(root, text="Let's play", command=lambda: scrabbleGame(nameP1, nameP2))
    playB.grid(row=5, column=1)
    startF.grid(row=0, column=0)
    p1L = Label(root, text="Enter Name of Player One")
    p1L.grid(row=3, column=0)
    play1E = Entry(root)
    play1E.grid(row = 3, column=1)

    p2L = Label(root, text="Enter Name of Player Two")
    p2L.grid(row=4, column=0)
    play2E = Entry(root)
    play2E.grid(row = 4, column=1)
    nameP1 = play1.get()
    nameP2 = play2.get()


instructionsB = Button(introF, text="Instructions", command=instructions)
instructionsB.grid(row=1, column=0)

startB = Button(introF, text="Start Game", command=startGame)
startB.grid(row=2, column=0)


def scrabbleGame(play1Name, play2Name):
    return





root.mainloop()
