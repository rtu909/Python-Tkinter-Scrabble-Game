from tkinter import *

root = Tk()
root.title("Scrabble")

def instructions():
    strInstruct = """Instructions for Scrabble:
    You get a rack of 7 tiles to start the game. You must play words with these
    7 tiles so that each word formed vertically and horizontally is a word.
    
    \tNote: Whenever you play a word, make sure that it touches at least
    \tone other letter on the board (not diagonally.)
    \tThe first move must touch the star in the middle of the board.
    
    To play a tile, click and drag the tile to the board.
    \tNote: When you play a tile, make sure that it snaps into a space.
    \tIf it doesn't, then it didn't place and you have to do it again.
    "?" tiles are blank tiles. They can be played as any letter.
    If you can't find any words to make, you can exchange. Exchanging 
    You get a certain amount of points based on the letters you played.
    Special Score Tiles:
    \tTWS (triple word score): Multiplies your score for that turn by 3.
    \tDWS (double word score): Multiplies your score for that turn by 2.
    \tTLS (triple letter score): Multiplies your score for that letter by 3.
    \tDLS (double letter score): Multiplies your score for that letter by 2.
    
    Once you play a word, you draw tiles until you have seven again.
    The game ends when there are no tiles left in the bag."""
    welcome = Label(root, text=strInstruct)
    welcome.grid(row=0, column=0)

def startGame():
    p1Label = Label(root, text="Enter Name of Player One")
    p1Label.grid(row=3, column=0)
    play1 = Entry(root)
    play1.grid(row = 3, column=1)

    p2Label = Label(root, text="Enter Name of Player Two")
    p2Label.grid(row=4, column=0)
    play2 = Entry(root)
    play2.grid(row = 4, column=1)
    nameP1 = play1.get()
    nameP2 = play2.get()

welcome = Label(root, text="Welcome to Scrabble")
welcome.grid(row=0, column=0)

instructionsB = Button(root, text="Instructions", command=instructions)
instructionsB.grid(row=1, column=0)

startB = Button(root, text="Start Game", command=startGame)
startB.grid(row=2, column=0)

 
root.mainloop()