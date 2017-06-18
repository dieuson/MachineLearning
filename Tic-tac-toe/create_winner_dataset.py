# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-12 22:43:38
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-13 22:02:58
import random
import json

def check_line_state(line, nb_column):
	nb_line_right = 0
	prev_piece = -1
	for piece in line:
		if (prev_piece < 0):
			prev_piece = piece
		if (piece != 0 and prev_piece == piece):
			nb_line_right += 1
		else:
			nb_line_right = 0
	if (nb_line_right == nb_column):
		return (True)
	return (False)

def check_column_state(grid, i, nb_column):

	column = []
	for x in xrange(0, nb_column):
		column.append(grid[x][i])
	if (check_line_state(column, nb_column)):
		return (True)

def check_winner(grid, nb_column=3):
	x1 = nb_column - 1
	diagonal = []
	diagonal1 = []
	for i in xrange(0, nb_column):
		line = grid[i]
		if (check_line_state(line, nb_column)):
			return (True)
		if (check_column_state(grid, i, nb_column)):
			return (True)
		diagonal.append(grid[i][i])
		diagonal1.append(grid[x1][i])
		x1 -= 1
	if (check_line_state(diagonal, nb_column) or check_line_state(diagonal, nb_column)):
		return (True)
	return (False)

def check_equal(grid, piece, nb_column=3):
	free_places = 0
	for i in xrange(0, nb_column):
		line = grid[i]
		for e in xrange(0, nb_column):
			if (line[e] == piece):
				free_places += 1
	if (free_places > 0):
		return (False)
	return (True)

def can_put_a_piece(grid, x, y):
	x -= 1
	y -= 1
	max_x = len(grid)
	max_y = len(grid[0])
	if (x > max_x or y > max_y or x < 0 or y < 0):
		return (False)
	if (grid[x][y] == 0):
		return (True)
	return (False)

def put_a_piece(grid, x, y, piece):
	x -=1
	y -=1
	grid[x][y] = piece
	return (grid)

def print_grid(grid):
	for x in grid:
		print(x)
	print("\n")

class Piece:
	dot = 0
	X = 1
	O = 2



def play_tic_tac_toe():
	grid = [[0,0,0],
			[0,0,0],
			[0,0,0],]

	nb_column = len(grid[0])

	piece = Piece()
	player = random.randint(1,2)
	winner = None
	iteration = 0
	en_jeu = True

	while en_jeu:
		x = random.randint(1,3)
		y = random.randint(1,3)

		if (check_winner(grid, nb_column) == True):
			winner = player
			en_jeu = False
		elif (check_equal(grid, piece.dot, nb_column) == True):
			winner = None
			en_jeu = False
		else:
			if (can_put_a_piece(grid, x, y)):
				if (player == piece.X):
					player = piece.O
				else:
					player = piece.X
				grid = put_a_piece(grid, x, y, player)
				print_grid(grid)
		iteration += 1

	if (winner):
		print("The winner is: %s" % ("X" if player == piece.X else "O"))
#		winner = ('X' if player == piece.X else 'O')
		winner = player
	else:
		print("Equality")
#		winner = 'E'
		winner = 0
	hash_array = {"grid": grid, "winner": winner}
	return (hash_array)

def create_dataset():
	nb_loop = 0
	filename = "./dataset_winner_x.json"
	data = []
	target = []
	Allarray = []
	array = []
	while nb_loop < 1000:
		array = play_tic_tac_toe()
		if (array["winner"] == 1):
			test = array["grid"][0] + array["grid"][1] + array["grid"][2]
			print(test)
			data.append(test)
			target.append(array["winner"])
			nb_loop += 1
	Allarray = {"data": data, "target": target}
	with open(filename,"w") as f:
	    json.dump(Allarray, f)
#	print (Allarray)

create_dataset()