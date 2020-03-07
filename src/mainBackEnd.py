import sys
sys.path.insert(0, 'C:/Users/Raymond/Documents/XA3/thetrifecta_scrabble/src/Model')

from Board import *
from Bag import *
from Player import *
from Rack import *
from Tiles import *
from boardChecks import *
from wordChecks import *
from endTurn import *
from frontEndMain import*

mainBoard = Board()
mainBag = Bag()
player1 = Player(mainBag)
player2 = Player(mainBag)

print(player1.getRackStr())
for tile in player1.getRackArr():
	print(tile.getLetter() + " " + str(tile.getScore()))
#print(player1.getRackArr())
print(player1.getScore())
print(mainBoard.getBoard())
for row in mainBoard.getBoard():
    for col in row:
        print(col)

print(mainBag.getRemainingTiles())

frontEndMain()
