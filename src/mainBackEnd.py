from Model/Board import *
from Model/Bag import *
from Model/Player import *
from Model/Rack import *
from Model/Tiles import *
from boardChecks import *
from wordChecks import *
from endTurn import *

class mainBackEnd:
	mainBoard = Board.Board()
	player1 = Player.Player()
	player2 = Player.Player()
	mainBag = Bag.Bag()
	
