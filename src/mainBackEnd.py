import sys
sys.path.insert(0, 'C:/Users/Raymond/Documents/XA3/thetrifecta_scrabble/src/Model')

#from Board import *
from Bag import *
from Player import *
from Rack import *
#from Tiles import *
#from boardChecks import *
from wordChecks import *
from endTurn import *
from frontEndMain import*

self.mainBoard = Board()
self.mainBag = Bag()
self.player1 = Player(mainBag)
self.player2 = Player(mainBag)


frontEndMain()

	
	
	
	
	
