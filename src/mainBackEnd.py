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
wordChecks = wordChecks()
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

#rack1 = Rack(mainBag)
tile1 = Tile("D")
tile2 = Tile("O")
tile3 = Tile("G")
player1.rack.rack.append(tile1)
player1.rack.rack.append(tile2)
player1.rack.rack.append(tile3)

b1 = wordChecks.checkRack("gibberish",player1.rack.getRackStr())
b2 = wordChecks.checkInDict("dog")
print(b1)
print(b2)
print(player1.rack.getRackLength())

frontEndMain()
