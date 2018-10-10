#! python3
# RpgGridGenerator.py - automates production of a grid for creating an RPG game
# usage: add a letter to list[] to produce larger grids
#        only produces square grids

list = ['a', 'b', 'c', 'd', 'e', 'f']

for letter in list:
	for s in range (len(list)):
		#keeps player from going off the grid (left)
		if s >0:
			left = letter+str(s-1)
		else: 
			left = letter+str(s)
		#keeps player from going off the grid (right)
		if s < len(list)-1:
			right = letter + str(s+1)
		else:
			right = letter + str(s)
		
		#index is used to change the N-S location of player
		index = list.index(letter)

		#keeps player from going off the grid (up)
		if index == 0:
			up = list[index]+str(s)
		else:	
			up = list[index-1]+str(s)
		#keeps player from going off the grid (down)
		if index == len(list)-1:
			down = list[index]+str(s)
		else:
			down = list[index+1]+str(s)


		s = (str(s)+"""\': {ZONE_NAME: '', 
					  DESCRIPTION: 'description',
				      EXAMINATION: 'examine',
				      SOLVED: False,
				      UP: \'"""+up+"""\',
				      DOWN: \'"""+down+"""\',
				      LEFT: \'"""+ left+"""\',
				      RIGHT: \'"""+right+"""\'},"""+'\n')
		print("'" + letter + s)


