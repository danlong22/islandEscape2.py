import cmd, textwrap, sys, os, time, random

screen_width = 100

##### player Setup #####
class Player:
	def __init__(self):
		self.location = 'f1'
		self.game_over = False
		self.inventory = []

myPlayer = Player()

#### title screen ####
def title_screen_selections():
	option = input('> ')
	while option.lower() not in ['play', 'help', 'quit']:
		print('Please enter a valid command.')
		option = input('> ')
	if option.lower() == ('play'):
		start_game()
	elif option.lower() == ('help'):
		help_menu()
	elif option.lower() == ('quit'):
		sys.exit()
def title_screen():
	os.system('clS')
	print('###############################')
	print('# Welcome to the Text RPG! #')
	print('###############################')
	print('            -Play-             ')
	print('            -Help-             ')
	print('            -Quit-             ')
	title_screen_selections()

def help_menu():
	os.system('cls')
	print('###############################')
	print('# Welcome to the Text RPG! #')
	print('###############################')
	print('Use Up, Down, Left, or Right to move.')
	print('Type your commands to do them')
	print('Use \"look\" to inspect something')
	print('Good luck and have fun!')
	input('Press Enter to return to the title screen.')
	title_screen()
##### Game interactivity #####
def print_location():
	print('\n' + ('#' * (4 + len(myPlayer.location))))
	print('# '+ zone_map[myPlayer.location][ZONE_NAME] + ' #')
	print(zone_map[myPlayer.location][DESCRIPTION] + ' #')
	print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
	print('\n' + '###################################')
	print('What would you like to do?')
	action = input('> ')
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'inventory', 'dig', 'teleport']
	while action.lower() not in acceptable_actions:
		print('Unknown action, try again')
		action = input('> ')
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() == 'inventory':
		print(myPlayer.inventory)
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())
	# a cheat for testing purposes 
	elif action.lower() == 'dig':
		supplies = input('You find a crate full of supplies buried in the ground. What will you take?')
		myPlayer.inventory.append(supplies)
	# a cheat for testing purposes
	elif action.lower() == 'teleport':
		goto = input ('Where would you like to travel, oh Great One?')
		movement_handler(goto)



def player_move(myAction):
	ask = 'Where do you want to move to?\n'
	dest = input(ask)
	while dest not in ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east']:
		dest = input(ask)
	if dest in ['up', 'north']:
		destination = zone_map[myPlayer.location][UP]
	if dest in ['down', 'south']:
		destination = zone_map[myPlayer.location][DOWN]
	if dest in ['left', 'west']:
		destination = zone_map[myPlayer.location][LEFT]
	if dest in ['right', 'east']:
		destination = zone_map[myPlayer.location][RIGHT]
	movement_handler(destination)
def movement_handler(destination):
	if myPlayer.location == destination:
		print('You cannot go that way.')
		myPlayer.location = destination
	else:
		myPlayer.location = destination
		print('\nYou have moved to the ' + zone_map[myPlayer.location][ZONE_NAME] + '.')
	print_location()
def solving():
	message = textwrap.wrap(zone_map[myPlayer.location][SOLVING], 60)
	for text in message:
		print (text)
	zone_map[myPlayer.location][SOLVED] = True
def player_examine(action):
	for text in textwrap.wrap(zone_map[myPlayer.location][EXAMINATION], width = 60):
		print (text)
	if zone_map[myPlayer.location][SOLVED]:
		for text in textwrap.wrap(zone_map[myPlayer.location][SOLVED_EXAMINATION],width = 60):
			print(text)
	else:
		for text in textwrap.wrap(zone_map[myPlayer.location][UNSOLVED_EXAMINATION], width = 60):
			print(text)

	#coconut beach
	if myPlayer.location == 'f0':
		if zone_map[myPlayer.location][SOLVED] == False:
			myPlayer.inventory.append('coconut husk')
			zone_map[myPlayer.location][SOLVED] = True


	#starting beach
	if myPlayer.location =='f1':
		if 'machetee' in myPlayer.inventory and zone_map[myPlayer.location][SOLVED]==False:
				solving()
				zone_map['f1'][UP] = 'e1'
	#cave entrance
	if myPlayer.location == 'e2':
		if 'machetee' not in myPlayer.inventory:
			print('What\'s this? You found a machetee on the floor.\n machetee added to inventory.')
			myPlayer.inventory.append('machetee')
		if 'torch' in myPlayer.inventory:
			zone_map[myPlayer.location][UP] = 'd2'
			solving()
		else: 
			pass
	#crocodile territory
	if myPlayer.location == 'e3':
		pass
	#bamboo grove
	if myPlayer.location == 'd0':
		if 'sap' in myPlayer.inventory:
			print('One of these shafts might make a good handle for a torch\n')
			myPlayer.inventory.append('torch')
			myPlayer.inventory.remove('sap')
			print('You turn the sap and bamboo shaft into a torch.')
		if 'spear head' in myPlayer.inventory:
			print('One of these bamboo shafts could make a good shaft for a spear if I had some cord to attach this spear head.')
			if 'coconut husk' in myPlayer.inventory:
				input('You bind the spear head to the bamboo shaft with the coconut husk cord.')
				myPlayer.inventory.append('spear')
				myPlayer.inventory.remove('spear head')
				myPlayer.inventory.remove('coconut husk')
		if 'spear' and 'torch' in myPlayer.inventory:
			zone_map[myPlayer.location][SOLVED] = True
	#deep jungle
	if myPlayer.location =='d1':
		if zone_map[myPlayer.location][SOLVED] == False:
			myPlayer.inventory.append('sap')
			solving()
	#deep cave
	if myPlayer.location == 'd2':
		if 'spear' not in myPlayer.inventory and 'spear head' not in myPlayer.inventory:
			input('You stumble in the dark and drop your torch. A peice of rock chips off the wall. It is pointed and razor sharp.')
			input('You put the spear head into your inventory.')
			myPlayer.inventory.append('spear head')
	#tiger territory
	if myPlayer.location == 'c1':
		if 'spear' not in myPlayer.inventory:
			print('You retreat back into the jungle.')
			movement_handler('d1')
		else:
			solving()
			zone_map[myPlayer.location][UP] = 'b1'

	#Ridge
	if myPlayer.location == 'b2':
		if zone_map[myPlayer.location][SOLVED] == False:
			if 'vine' in myPlayer.inventory:
				zone_map[myPlayer.location][DOWN] = 'c2'
				solving()
	#Smooth Pass
	if myPlayer.location == 'b3':
		if 'climbing gear' in myPlayer.inventory:
			solving()
			zone_map[myPlayer.location][UP] = 'a3'

	#plateu
	if myPlayer.location == 'b4':
		if 'axe' not in myPlayer.inventory:
			myPlayer.inventory.append('axe')
			solving()

	#Buggy swamp
	if myPlayer.location == 'a4':
		if zone_map[myPlayer.location][SOLVED] == False:
			if 'fragrant grass' in myPlayer.inventory:
				zone_map[myPlayer.location][SOLVED] = True
			else:
				print( 'You retreat back the way you came.')
				movement_handler('b4')
		if zone_map[myPlayer.location][SOLVED] == True:
			solving()
			zone_map[myPlayer.location][RIGHT] = 'a5'
	#Cabin
	if myPlayer.location == 'a5':
		if zone_map[myPlayer.location][SOLVED] == False:
			solving()
			myPlayer.inventory.append('trap guide')
	#Opposite Bank
	if myPlayer.location == 'f3':
		if zone_map[myPlayer.location][SOLVED]==False:
			#solving() does the fish, so the grass needs to be done manually
			if 'fragrant grass' not in myPlayer.inventory:
				myPlayer.inventory.append('fragrant grass')
				print('This grass might be useful, so you take some.')
			if 'trap guide' in myPlayer.inventory:
				myPlayer.inventory.append('fish')
				solving()
	#Crocodile Territory
	if myPlayer.location == 'e3':
		if zone_map[myPlayer.location][SOLVED] == False:
			if 'fish' in myPlayer.inventory:
				solving()
			else:
				print('A massive crocodile snaps at you. You just barely escape to the southern stream bank.')	
				movement_handler('f3')	
	#stream bank
	if myPlayer.location == 'f2':
		if zone_map[myPlayer.location][SOLVED] == False:
			if 'axe' in myPlayer.inventory:
				solving()
				zone_map[myPlayer.location][RIGHT] = 'f3'
	if myPlayer.location == 'a3':
		myPlayer.game_over = True
	#waterfall
	if myPlayer.location == 'd4':
		if zone_map[myPlayer.location][SOLVED] ==False:
			myPlayer.inventory.append('vine')
			solving()
	if myPlayer.location == 'c2':
		if zone_map[myPlayer.location][SOLVED] == False:
			solving()
			myPlayer.inventory.append('climbing gear')
	if myPlayer.location == '':
		pass

	prompt()
###### game functionality #####
def start_game():
	main_game_loop()
def main_game_loop():
	while myPlayer.game_over is False:
		prompt()



	##### map #####
	'''#player starts at d2
	 A1  A2  A3...
	_________________
	|   |   |   |   | A4
	_________________
	|   |   |   |   | B4
	_________________
	|   |   |   |   | C4
	_________________
	|   |   |   |   | D4
	_________________

	'''
ZONE_NAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVING = 'solving'
SOLVED_EXAMINATION = 'solved examination'
UNSOLVED_EXAMINATION = 'unsolved examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT  = 'left', 'west'
RIGHT =  'right', 'east'

zone_map = {

'a0': {ZONE_NAME: 'none', 
					  DESCRIPTION: 'description',
				      EXAMINATION: 'examine',
				      SOLVED: False,
				      UP: 'a0',
				      DOWN: 'b0',
				      LEFT: 'a0',
				      RIGHT: 'a1'},


'a3': {ZONE_NAME: 'Top of the Island', 
					  DESCRIPTION: 'description',
				      EXAMINATION: 'examine',
				      SOLVED: False,
				      SOLVED_EXAMINATION: '',
				      UNSOLVED_EXAMINATION: '',
				      UP: 'a3',
				      DOWN: 'b3',
				      LEFT: 'a2',
				      RIGHT: 'a4'},

'a4': {ZONE_NAME: 'Buggy Swamp', 
					  DESCRIPTION: 'You step into a swamp and the sounds of buzzing.',
				      EXAMINATION: 'There are cliffs blocking the North and West. There is a new growth forest in the South. It looks like there is a man-made structure to the East.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'The insects are kept away by the fragrant grass in your inventory. You should have no problem getting to the cabin in the East.',
				      UNSOLVED_EXAMINATION: 'The biting and stinging insects here make the swamp impassible.',
				      SOLVING: 'The insects come just close enough to smell the fragrant grass in your inventory, but no closer. They are repelled by the smell.',
				      UP: 'a4',
				      DOWN: 'b4',
				      LEFT: 'a4',
				      RIGHT: 'a4'},

'a5': {ZONE_NAME: 'Cabin', 
					  DESCRIPTION: 'You come upon a wooden, man-made structure here.',
				      EXAMINATION: 'You peer inside. It has clearly been uninhabited for a long time. You are in a dead-end, and only West, the direction you came from, is open.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is a rotted sleeping pad on the ground, and a crude wooden table',
				      UNSOLVED_EXAMINATION: 'There is a rotted sleeping pad on the ground, and a crude wooden table with a journal on top.',
				      SOLVING: 'The journal is old and mostly illegible. One of the few legible parts teaches how to make fish traps. You put the trap guide in your inventory.',
				      UP: 'a5',
				      DOWN: 'a5',
				      LEFT: 'a4',
				      RIGHT: 'a5'},


'b1': {ZONE_NAME: 'Rocky Pass', 
					  DESCRIPTION: 'This pass provides a way to the top of the higher parts of the island.',
				      EXAMINATION: 'You see rocks and dust. There is nothing of interest here.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is a ridge to the East and a dead tiger to the south. The West is a sheer drop, and the North an unscalable cliff face.',
				      UNSOLVED_EXAMINATION: 'There is a ridge to the East and a dead tiger to the south.',
				      UP: 'b1',
				      DOWN: 'c1',
				      LEFT: 'b1',
				      RIGHT: 'b2'},

'b2': {ZONE_NAME: 'Ridge', 
					  DESCRIPTION: 'This ridge provides a view of the southern part of the island',
				      EXAMINATION: 'You see no way up the Northern cliff face. There is a pass to the West and more ridge to the East.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is a vine attached to the scraggly tree, allowing you to decend the cliff to the south.',
				      UNSOLVED_EXAMINATION: 'There is a tree here that looks just strong enough to support your weight. Maybe you could decend the southern cliff if you had a rope.',
				      SOLVING: 'You tie the vine to the tree. You can now scale down the cliff face to the South.',
				      UP: 'b2',
				      DOWN: 'b2',
				      LEFT: 'b1',
				      RIGHT: 'b3'},

'b3': {ZONE_NAME: 'Smooth Pass', 
					  DESCRIPTION: 'The path is smooth and treacherous.',
				      EXAMINATION: 'A new-growth forest is visible under a treacherous drop to the East. The path continues to the West and the South.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'The rock wall to the North is scalable with your climbing gear.',
				      UNSOLVED_EXAMINATION: 'The rock wall to the North looks like it might be scalable, but only if you had some climbing gear.',
				      SOLVING: 'You set up your climbing gear. The northern wall should be climbable.',
				      UP: 'b3',
				      DOWN: 'c3',
				      LEFT: 'b2',
				      RIGHT: 'b3'},

'b4': {ZONE_NAME: 'New-Growth Forest', 
					  DESCRIPTION: 'You come upon a new-growth forest.',
				      EXAMINATION: 'This forest could only be a few years old that the most. There is a swamp to the north, impassible jungle to the East, a scree slope to the South, and an unscalable rock wall to the West.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'You wonder who cut down the old growth forest.',
				      UNSOLVED_EXAMINATION: 'I wonder who cut down the old growth forest..',
				      SOLVING: 'You find a rusty, but usable axe in a stump. You take it.',
				      UP: 'a4',
				      DOWN: 'c4',
				      LEFT: 'b4',
				      RIGHT: 'b4'},


'c1': {ZONE_NAME: 'Tiger Territory', 
					  DESCRIPTION: 'You walk into a clearing. There is a huge tiger eying you hungrily.',
				      EXAMINATION: 'examine',
				      SOLVED: False,
				      UNSOLVED_EXAMINATION: 'The tiger lunges at you and only barely misses.',
				      SOLVED_EXAMINATION: 'There is a dead tiger here. There is a jungle to the south, and a passage to a high ridge to the north',
				      SOLVING: 'You thrust with you spear and make a tiger shish-kebab. This tiger wont be bothering you anymore.',
				      UP: 'c1',
				      DOWN: 'd1',
				      LEFT: 'c1',
				      RIGHT: 'c1'},
'c2': {ZONE_NAME: 'Crash Site', 
					  DESCRIPTION: 'There is a helicopter crash here.',
				      EXAMINATION: 'You are stuck between impassible cliffs on all four sides. Only the vine you used to decend the northern wall allows you any way out.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'What happened? How did this get here?.',
				      UNSOLVED_EXAMINATION: 'What happened? How did this get here?.',
				      SOLVING: 'You find some climbing gear among the wreckage. This should help you climb upwards.',
				      UP: 'b2',
				      DOWN: 'c2',
				      LEFT: 'c2',
				      RIGHT: 'c2'},

'c3': {ZONE_NAME: 'Rocky Slope', 
					  DESCRIPTION: 'The rocky pass desends onto a plateu.',
				      EXAMINATION: 'The pass continues to the North, there is a plateu to the East, there is a swamp at the bottom of a sheer drop to the South, and a bed of jagged rocks at the bottom of a similar drop to the West. ',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is nothing interesting here.',
				      UNSOLVED_EXAMINATION: 'There is nothing interesting here.',
				      UP: 'b3',
				      DOWN: 'c3',
				      LEFT: 'c3',
				      RIGHT: 'c4'},

'c4': {ZONE_NAME: 'plateu', 
					  DESCRIPTION: 'The path ends in a wide, flat plateu.',
				      EXAMINATION: 'There is a new growth forest in the north, impassible crags in the East, a waterfall at the bottom of a steep drop to the South, and a high pass to the West.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is nothing interesting here.',
				      UNSOLVED_EXAMINATION: 'There is nothing interesting here.',
				      UP: 'b4',
				      DOWN: 'c4',
				      LEFT: 'c3',
				      RIGHT: 'c4'},



'd0': {ZONE_NAME: 'Bamboo Grove', 
					  DESCRIPTION: 'You enter a bamboo grove.',
				      EXAMINATION: 'The bamboo to the North, South, and West is far too thick to pass through. Only the East is open.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'The wind rustles the bamboo growing here.',
				      UNSOLVED_EXAMINATION: 'These bamboo shafts could be useful for a variety of applications.',
				      UP: 'd0',
				      DOWN: 'd0',
				      LEFT: 'd0',
				      RIGHT: 'd1'},

'd1': {ZONE_NAME: 'Deep Jungle', 
					  DESCRIPTION: 'You enter a deep jungle.',
				      EXAMINATION: 'The East and West are impassible. There is more junlge to the South. There is an onimous-looking clearing to the North. You get the distinct feeling that you shouldn\'t go there unprepared.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'You already have some so you leave it alone.',
				      UNSOLVED_EXAMINATION: 'There is some stikcy sap coming from a tree here.',
				      SOLVING: 'It looks useful so you collect some. Sap added to inventory.',
				      UP: 'c1',
				      DOWN: 'e1',
				      LEFT: 'd0',
				      RIGHT: 'd1'},

'd2': {ZONE_NAME: 'Dark Cave', 
					  DESCRIPTION: 'Your torch cuts through the dark, illuminating a small sphere of space.',
				      EXAMINATION: 'You shine your torch on the walls.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: '',
				      UNSOLVED_EXAMINATION: '',
				      UP: 'd2',
				      DOWN: 'e2',
				      LEFT: 'd2',
				      RIGHT: 'd2'},

'd3': {ZONE_NAME: 'Swamp', 
					  DESCRIPTION: 'You enter a swamp.',
				      EXAMINATION: 'There are unscalable cliffs to the North and West, a waterfall empties into a wide pool in the East, and the crocodiles are back South.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: '',
				      UNSOLVED_EXAMINATION: '',
				      UP: 'd3',
				      DOWN: 'e3',
				      LEFT: 'd3',
				      RIGHT: 'd4'},

'd4': {ZONE_NAME: 'Waterfall', 
					  DESCRIPTION: 'You come upon a waterfall and a wide pool.',
				      EXAMINATION: 'This is a dead end. Only the way you came, the West, is open.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There are small fish in this pool, but they are of no interest to you.',
				      UNSOLVED_EXAMINATION: 'You see some long, strong vines. They could maybe be used to decend from high places.',
				      SOLVING: 'You cut one down and add it to your inventory.',
				      UP: 'd4',
				      DOWN: 'd4',
				      LEFT: 'd3',
				      RIGHT: 'd4'},

'e1': {ZONE_NAME: 'Thick Jungle', 
					  DESCRIPTION: 'You enter a thick jungle.',
				      EXAMINATION: 'There is more jungle to the north, impassible rocks to the East, a beach to the south, and impassible jungle to the West.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is a lot of thick brush clogging the way, but it is navigatable with you machetee.',
				      UNSOLVED_EXAMINATION: 'There is a lot of thick brush clogging the way, but it is navigatable with you machetee.',
				      UP: 'd1',
				      DOWN: 'f1',
				      LEFT: 'e1',
				      RIGHT: 'e1'},

'e2': {ZONE_NAME: 'Cave Entrance', 
					  DESCRIPTION: 'You enter the cave.',
				      EXAMINATION: 'The sun gives enough light to see only the very frontmost part of the cave.\n The cave is narrow, and the walls close in from the East and West. The exit is to the South.',
				      SOLVED: False,
				      SOLVING: 'You light your torch to get a better view. The northern part of the cave is no accesible to you.',
				      SOLVED_EXAMINATION: 'The back of the cave is dark, but should be navigatable with your torch.',
				      UNSOLVED_EXAMINATION: 'You cannot continue North, deeper into the cave unless you have a light source.  ',
				      UP: 'e2',
				      DOWN: 'f2',
				      LEFT: 'e2',
				      RIGHT: 'e2'},

'e3': {ZONE_NAME: 'Crocodile Terrirory', 
					  DESCRIPTION: 'The stream widens and slows down here. It is crossable to the North and unnavigatably fast in the East and West. There is a friends stram bank in the South.',
				      EXAMINATION: 'This muddy, shallow water is home to a bunch of crocodiles.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'The crocodiles are elsewhere for now. It should be safe to cross.',
				      UNSOLVED_EXAMINATION: '',
				      SOLVING: 'You toss the fish downstream and the crocodiles go after it.',
				      UP: 'd3',
				      DOWN: 'f3',
				      LEFT: 'e2',
				      RIGHT: 'e4'},



'f0': {ZONE_NAME: 'Coconut Beach', 
					  DESCRIPTION: 'You are on a beach with a single coconut tree.',
				      EXAMINATION: 'There are impassible cliffs to the North and West. There is another beach to the East, and the Ocean stretches to the Southern horizon.',
				      SOLVING: 'solving',
				      SOLVED_EXAMINATION:'There are no coconuts on the tree and the ones on the ground are all rotten.',
				      UNSOLVED_EXAMINATION: 'There is a stringy coconut husk on the ground. It looks like it could be made into cord.\n Coconut husk added to inventory.',
				      SOLVED: False,
				      UP: 'f0',
				      DOWN: 'f0',
				      LEFT: 'f0',
				      RIGHT: 'f1'},

'f1': {ZONE_NAME: 'Sandy Beach', 
					  DESCRIPTION: 'You find yourself on a sandy beach.',
				      EXAMINATION: 'There is a thick jungle to the North, other beaches in the East and West, and an ocean to the South.',
				      SOLVING: 'You hack through the brush with your machetee.',
				      UNSOLVED_EXAMINATION: 'The North is blocked by thick brush.',
				      SOLVED_EXAMINATION: 'There is a path through the brush in the North',
				      SOLVED: False,
				      UP: 'f1',
				      DOWN: 'f1',
				      LEFT: 'f0',
				      RIGHT: 'f2'},

'f2': {ZONE_NAME: 'Stream Bank', 
					  DESCRIPTION: 'You come to a stream bank.',
				      EXAMINATION: 'There is a cave to the North, an ocean to the South, and another beach to the East. ',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There is a tree trunk spanning the stream, providing a way across.',
				      UNSOLVED_EXAMINATION: 'There is a tall, but thin tree here. The stream flows far too quickly to even consider trying to swim across, but you could maybe use this tree trunk to cross if you had something to chop it down with.',
				      SOLVING: 'You take a few swings at the tree. It\'s difficult with your rusty axe, but doable. After many more swings and cursing, the tree falls, forming a bridge over the stream.',
				      UP: 'e2',
				      DOWN: 'f2',
				      LEFT: 'f1',
				      RIGHT: 'f2'},

'f3': {ZONE_NAME: 'Opposite Stream Bank', 
					  DESCRIPTION: 'You are on the opposite side of the stream.',
				      EXAMINATION: 'There is a citrus-like fragrance here. It is coming from the grass growing next to the stream. There is more stream bank in the North, cliffs block the East, the ocean blocks off the South, and the bridge spans the stream to the West.',
				      SOLVED: False,
				      SOLVED_EXAMINATION: 'There are no more fish around here.',
				      UNSOLVED_EXAMINATION: 'There are fish in the water. You wonder how to catch them.',
				      SOLVING: 'Following the instructions in your trap guide, you make a trap and a fish swims right in. You put the fish in your inventory.',
				      UP: 'e3',
				      DOWN: 'f3',
				      LEFT: 'f2',
				      RIGHT: 'f3'},



				      }

def setup_game():
	print(' Welcome to Island Escape '.center(60, '='))
	
	text = textwrap.wrap('\nCongradulations, you have survived a catostrophic place crash/ shipwreck/ alien abduction/ whatever. Unfortunatly you are stuck on this island and need to explore it to find a way off.\n', width = 60)
	for t in text:
		print(t)
	print('\n'+ 'How To Play:'.center(60,'-'))
	text = textwrap.wrap('Island Escape is a text-based adventure game where you move your character North, South, East, and West aroudn the island, searching for items and tools that will help you progress.\n', width = 60)
	for t in text:
		print (t)
	input('\n' + '> Press Enter to Continue.')
	print('You open your eyes... ')
	main_game_loop()
setup_game()
