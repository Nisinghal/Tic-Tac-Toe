import random 
# There are 2 players: player1 and player2
player1 = 1
player2 = 2

# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1 = 0    
tile2 = 0
tile3 = 0
tile4 = 0
tile5 = 0
tile6 = 0
tile7 = 0
tile8 = 0
tile9 = 0

c0 = 0
c1 = 0
c2 = 0

# turn variable defines whose turn is now

turn = player1
BS = str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)

def update(x):
	global BS
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	global turn

	if x==1:
		tile1=turn
	elif x==2:
		tile2=turn
	elif x==3:
		tile3=turn
	elif x==4:
		tile4=turn
	elif x==5:
		tile5=turn
	elif x==6:
		tile6=turn
	elif x==7:
		tile7=turn
	elif x==8:
		tile8=turn
	elif x==9:
		tile9=turn


	BS = str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)


def validmove(move) :
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	#is move tile number?
	# print(type(move))
	if move == 0 : return True
	else : return False

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""

	#do we have player number
	#do we take turn
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	something(BS)
	WinFlag = 0
	if tile1 == 2 and ((tile2 == 2 and tile3 == 2) or (tile5 == 2 and tile9 == 2) or (tile4 == 2 and tile7 == 2)) :
				WinFlag = 2
	elif tile2 == 2 and tile5 == 2 and tile8 == 2 :
				WinFlag = 2
	elif tile3 == 2 and ((tile5 == 2 and tile7 == 2) or (tile6 == 2 and tile9 == 2)) :
				WinFlag = 2
	elif tile4 == 2 and tile5 == 2 and tile6 == 2 :
				WinFlag = 2
	elif tile7 == 2 and tile8 == 2 and tile9 == 2 :
				WinFlag = 2

	if tile1 == 1 and ((tile2 == 1 and tile3 == 1) or (tile5 == 1 and tile9 == 1) or (tile4 == 1 and tile7 == 1)):
				WinFlag = 1
	elif tile2 == 1 and tile5 == 1 and tile8 == 1:
				WinFlag = 1
	elif tile3 == 1 and (((tile5 == 1 and tile7 == 1) or (tile6==1 and tile9==1))):
				WinFlag = 1
	elif tile4 == 1 and tile5 == 1 and tile6 == 1 :
				WinFlag = 1
	elif tile7 == 1 and tile8 == 1 and tile9 == 1 :
				WinFlag = 1
	# print (tile1, tile2, tile3)
	# print (tile4, tile5, tile6)
	# print (tile7, tile8, tile9)
	# print ('WF', WinFlag)
	# print ()

	return WinFlag

def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""

	c0 = 0
	global BS
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	global turn


	for i in BS:
		if i=='0':
			c0+=1
	
	tileno=random.randint(1,9)
	
	# i=0
	# while (i+1<=tileno):
	# 	if int(BS[i])!=0:
	# 		tileno+=1
	# 	i+=1
	# print("what")


	##### infinite loop

	while int(BS[tileno-1])!=0 and BS.count('0')>0:
		tileno=random.randint(1,9)
	
	# BS=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)

	# print(BS[:3])
	# print(BS[3:6])
	# print(BS[6:])
	# print()
	return tileno

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""	
	global BS
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	global t

	x = 0
	#completing sequence to win
	
	if tile1 == turn :
		if   tile3 == turn and validmove(tile2) :
			x = turn
		elif tile9 == turn and validmove(tile5) :
			x = 5
		elif tile7 == turn and validmove(tile5) :
			x = 5
		elif tile2 == turn and validmove(tile3) :
			x = 3
		elif tile5 == turn and validmove(tile9) :
			x = 9
		elif tile4 == turn and validmove(tile7) :
			x = 7
	elif tile2 == turn :
		if   tile3 == turn and validmove(tile1) :
			x = 1
		elif tile5 == turn and validmove(tile8) :
			x = 8
		elif tile8 == turn and validmove(tile5) :
			x = 5
	elif tile3 == turn :
		if   tile5 == turn and validmove(tile7) :
			x = 7
		elif tile7 == turn and validmove(tile5) :
			x = 5
		elif tile6 == turn and validmove(tile9) :
			x = 9
		elif tile9 == turn and validmove(tile6) :
			x = 6
	elif tile4 == turn :
		if tile7 == turn and validmove(tile1) :
			x = 1
		elif tile5 == turn and validmove(tile6) :
			x = 6
		elif tile6 == turn and validmove(tile5) :
			x = 5
	elif tile5 == turn :
		if tile6 == turn and validmove(tile4) :
			x = 4
		elif tile7 == turn and validmove(tile3) :
			x = 3
		elif tile8 == turn and validmove(tile2) :
			x = 2
		elif tile9 == turn and validmove(tile1) :
			x = 1
	elif tile6 == turn and tile9 == turn and validmove(tile3) :
			x = 3
	elif tile7 == turn :
		if tile8 == turn and validmove(tile9) :
			x = 9
		elif tile9 == turn and validmove(tile8) :
			x = 8
	elif tile8 == turn:
		if tile9 == turn and validmove(tile7) :
			x = 7

	#blocking opponent's sequence
	if turn==1:
		if tile1==2:
			if tile3==2 and validmove(tile2):
				x = 2
			elif tile9==2 and validmove(tile5):
				x = 5
			elif tile7==2 and validmove(tile5):
				x = 5
			elif tile2==2 and validmove(tile3):
				x = 3
			elif tile5==2 and validmove(tile9):
				x = 9
			elif tile4==2 and validmove(tile7):
				x = 7
		elif tile2==2:
			if tile3==2 and validmove(tile1):
				x = 1
			elif tile5==2 and validmove(tile8):
				x = 8
			elif tile8==1 and validmove(tile5):
				tx = 5
		elif tile3==2:
			if tile5==2 and validmove(tile7):
				x = 7
			elif tile7==2 and validmove(tile5):
				x = 5
			elif tile6==2 and validmove(tile9):
				x = 9
			elif tile9==2 and validmove(tile6):
				x = 6
		elif tile4==2:
			if tile7==2 and validmove(tile1):
				x = 1
			elif tile5==2 and validmove(tile6):
				x = 6
			elif tile6==2 and validmove(tile5):
				x = 5
		elif tile5==2:
			if tile6==2 and validmove(tile4):
				x = 4
			elif tile7==2 and validmove(tile3):
				x = 3
			elif tile8==2 and validmove(tile2):
				x = 2
			elif tile9==2 and validmove(tile1):
				x = 1
		elif tile6==2:
			if tile9==2 and validmove(tile3):
				x = 3
		elif tile7==2:
			if tile8==2 and validmove(tile9):
				x = 9
			elif tile9==2 and validmove(tile8):
				x = 8
		elif tile8==2:
			if tile9==2 and validmove(tile7):
				x = 7

	if turn==2:
		# print ("YESSS")
		if tile1==1:
			if tile3==1 and validmove(tile2):
				x = 2
			elif tile9==1 and validmove(tile5):
				x = 5
			elif tile7==1 and validmove(tile4):
				x = 4
			elif tile2==1 and validmove(tile3):
				x = 3
			elif tile5==1 and validmove(tile9):
				x = 9
			elif tile4==1 and validmove(tile7):
				x = 7
		elif tile2==1:
			if tile3==1 and validmove(tile1):
				x = 1
			elif tile5==1 and validmove(tile8):
				x = 8
			elif tile8==1 and validmove(tile5):
				x = 5
		elif tile3==1:
			if tile5==1 and validmove(tile7):
				x = 7
			elif tile7==1 and validmove(tile5):
				x = 5
			elif tile6==1 and validmove(tile9):
				x = 9
			elif tile9==1 and validmove(tile6):
				x = 6
		elif tile4==1:
			if tile7==1 and validmove(tile1):
				x = 1
			elif tile5==1 and validmove(tile6):
				x = 6
			elif tile6==1 and validmove(tile5):
				x = 5
		elif tile5==1:
			if tile6==1 and validmove(tile4):
				x = 4
			elif tile7==1 and validmove(tile3):
				x = 3
			elif tile8==1 and validmove(tile2):
				x = 2
			elif tile9==1 and validmove(tile1):
				x = 1
		elif tile6 == 1 and tile9 == 1 and validmove(tile3):
				x = 3
		elif tile7==1:
			if tile8==1 and validmove(tile9):
				x = 9
			elif tile9==1 and validmove(tile8):
				x = 8
		elif tile8==1 and tile9==1 and validmove(tile7):
				x = 7

	if x==0:
		# print('here')
		x=takeNaiveMove()
		return x
	return x
	
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	c1 = 0
	c2 = 0
	global BS
	for i in BS:
		if i == '1' :
			c1 += 1
		elif i == '2' :
			c2 += 1

	if c1 == c2 or c1 == (c2+1) :
		return True 
	else :
		return False

def game(gametype=1) :
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	global turn
	global BS
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	global t

	if gametype==1:
		t=0
		while t<9 and validBoard():
			# print("what")
			turn=player1
			update(takeNaiveMove())
			t+=1
			if win():
				return 1
			if t==9:
				return 0

			turn=player2
			update(takeNaiveMove())
			t+=1
			if win():
				return 2

		else: return 0

	if gametype==2:
		t=0
		while t<9 and validBoard():
			# print("what")
			turn=player1
			update(takeNaiveMove())
			t+=1
			if win()==1:
				return 1
			elif win()==2:
				return 2
			if t==9:
				return 0

			turn=player2
			update(takeStrategicMove())
			t+=1
			if win()==2:
				return 2
			elif win()==1:
				return 1
			##not stopping after 2 wins
			##index error in (1,c0)

		else: return 0


	elif gametype==3:
		t=0
		while t<9 and validBoard():
			# print("what")
			if win()==2:
				return 2
			turn=player1
			update(takeStrategicMove())
			t+=1
			if win()==1:
				return 1

			if t==9:
				return 0

			turn=player2
			update(takeStrategicMove())
			t+=1
			if win():
				return 2

		else: return 0
def reset() :
	global turn
	global tile1    
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	global BS
	turn = player1
	tile1 = 0    
	tile2 = 0
	tile3 = 0
	tile4 = 0
	tile5 = 0
	tile6 = 0
	tile7 = 0
	tile8 = 0
	tile9 = 0
	BS = '000000000'

def game1(n) :
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	c=0
	#o=0
	for i in range(n):
		reset()
		if game(1)==1:
			c+=1
			# print(c)	
			#print(c)
	# o=o+1
	# print(o)		
	return c/n

def game2(n) :
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	c=0
	for i in range(n):
		if game(2)==1:
			c+=1
		reset()
	return c/n

def game3(n) :
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	c=0
	for i in range(n):
		if game(3)==1:
			c+=1
		reset()              
	return c/n
def SampleState(ss):
	global BS
	global turn
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
	if ss==1:
		BS='010212200'
	elif ss==2:
		BS='121012110'
	elif ss==3:
		BS='121012120'
	elif ss==4:
		BS='121002120'
	elif ss==5:
		BS='211121212'
	elif ss==6:
		BS='122212101'
	elif ss==7:
		BS='121212101'
	elif ss==8:
		BS='121012121'
	elif ss==9:
		BS='101212221'
	elif ss==10:
		turn=1
		BS='120000102' 
	elif ss==11:
		BS='121012121'
	elif ss==12:
		BS='101212221'
	# tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9=int(BS[0]),int(BS[1]),int(BS[2]),int(BS[3]),int(BS[4]),int(BS[5]),int(BS[6]),int(BS[7]),int(BS[8])
	return BS

def something(BS):
		
		global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9
		tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9=int(BS[0]),int(BS[1]),int(BS[2]),int(BS[3]),int(BS[4]),int(BS[5]),int(BS[6]),int(BS[7]),int(BS[8])
		

# BS=(SampleState(6))
# something(BS)
# print(win())
# for i in range(1,7):

# 	SampleState(i)
# 	print (tile1, tile2, tile3)
# 	print (tile4, tile5, tile6)
# 	print (tile7, tile8, tile9)

# 	print(win())
# 	print(validBoard())
# 	print ()





# result=game(3)
# if result==1:
# 	print('P1wins')
# elif result==2:
# 	print('P2wins')
# else: print('Draw')

# print(game1(10000),'g1')
# print(game2(10000),'g2')
# print(game3(10000),'g3')
