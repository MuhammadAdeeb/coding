# TODO import the necessary classes and methods
from games import *
import sys

if __name__ == '__main__':
	
	input_file = sys.argv[1]
	# input_file = "Test.txt"
	read_file = open(input_file, 'r')  # open file
	read_file = read_file.readlines()  # read lines of the file and save that listin read_file

	lines_lst = []
	board_dict = {}  # dict for 'board' in GamesState namedtuple

	i = 0  # to put items in line_list
	# Creates a list of a list of the strings with board info
	for x in read_file:
		lines_lst.append(None)
		lines_lst[i] = [x[0], x[2], x[4]]
		i += 1

	x_count = 0  # x_cnt and o_cnt used to determine whose turn it is
	o_count = 0
	moves = []
	# uses above list of list to put info of location of X's and O's in a dict
	for i in range(3):
		for j in range(3):
			if lines_lst[i][j] != '-':
				board_dict[(i, j)] = lines_lst[i][j]  # Ex: {(1, 1): 'X'}
				# Increment x and o count for to_move part of the GameState
				if lines_lst[i][j] == 'X':
					x_count += 1
				else:
					o_count += 1
			else:
				moves.append((i, j))  # whereever there's a '-' a move is available
	# print(board_dict)
	term = 0

	# to_move in GameState, determined by num of X and O's in input
	if x_count <= o_count:
		tm = 'X'
	else:
		tm = 'O'

	# For debugging:
	'''
	print(board_dict)
	print(tm)
	print(moves)
	'''

	# Answer to Part a:
	print('Whose turn is it in this state?')
	print(tm)

	game_obj = TicTacToe()
	game_obj.initial = GameState(tm, 0, board_dict, moves)

	while not game_obj.terminal_test(game_obj.initial):
		# m = alpha_beta_search(game_obj.initial, game_obj)
		m = minmax_decision(game_obj.initial, game_obj)
		# print(game_obj.initial.to_move, ": ", m)
		game_obj.initial = game_obj.result(game_obj.initial, m)
		# game_obj.display(game_obj.initial)
		# print()

	# Answer to Part b:
	print(
		'If both X and O play optimally from this state, does X have a guaranteed win, guaranteed loss, or guaranteed draw')
	if game_obj.utility(game_obj.initial, 'X') == 1:
		print("Guaranteed Win")
	elif game_obj.utility(game_obj.initial, 'X') == 0:
		print("Guaranteed Draw")
	else:
		print("Guaranteed Loss")
