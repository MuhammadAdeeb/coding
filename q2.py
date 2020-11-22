# TODO import the necessary classes and methods
import sys
from games import *
from guaranty import guaranteed

if __name__ == '__main__':

	term_state = 0  	# Total terminal states
	non_term_state = 1  # Total Non-terminal states
	x_wins = 0  		# Terminals states where x wins
	x_loses = 0  		# Terminals states where x loses
	x_draws = 0  		# Terminals states where x draws
	g_x_wins = 0  		# Non-terminal states where x wins (Guaranteed)
	g_x_loses = 0  		# Non-terminal states where x loses (Guaranteed)
	g_x_draws = 0  		# Non-terminal states where x draws (Guaranteed)

	def minmax(state, game):  # modified minmax algorithm from the Aima code

		player = game.to_move(state)  # Player who's turn it is to move

		def max_value(state):
			# calling all the global vars:
			global term_state
			global non_term_state
			global x_wins
			global x_loses
			global x_draws
			global g_x_wins
			global g_x_loses
			global g_x_draws

			if game.terminal_test(state):
				term_state += 1  # Above if statement means it's a term state, hence increment term_state cntr
				if game.utility(state, 'X') == 1:  # if utility == 1; x wins
					x_wins += 1
				elif game.utility(state, 'X') == -1:  # if utility == -1; x loses
					x_loses += 1
				elif game.utility(state, 'X') == 0:  # if utility == 0; x draws
					x_draws += 1
				return game.utility(state, player)  # return utility of the player at this state
			else:
				non_term_state += 1  # B/c not term, increment non_term_state cntr

				a = guaranteed(game, state)  # To check what's guaranteed at this non-term state

				if a == 1:  # to increment Guaranteed X win
					g_x_wins += 1
				elif a == -1:  # to increment Guaranteed X loss
					g_x_loses += 1
				else:  # to increment Guaranteed X draw
					g_x_draws += 1

			v = -np.inf
			for a in game.actions(state):
				v = max(v, min_value(game.result(state, a)))
			return v

		def min_value(state):
			# calling all the global vars:
			global term_state
			global non_term_state
			global x_wins
			global x_loses
			global x_draws
			global g_x_wins
			global g_x_loses
			global g_x_draws

			if game.terminal_test(state):
				term_state += 1  # Above if statement means it's a term state, hence increment term_state cntr
				if game.utility(state, 'X') == 1:  # if utility == 1; x wins
					x_wins += 1
				elif game.utility(state, 'X') == -1:  # if utility == -1; x loses
					x_loses += 1
				elif game.utility(state, 'X') == 0:  # if utility == 0; x draws
					x_draws += 1
				return game.utility(state, player)  # return utility of the player at this state
			else:
				non_term_state += 1  # B/c not term, increment non_term_state cntr

				a = guaranteed(game, state)  # To check what's guaranteed at this non-term state

				if a == 1:  # to increment Guaranteed X win
					g_x_wins += 1
				elif a == -1:  # to increment Guaranteed X loss
					g_x_loses += 1
				else:  # to increment Guaranteed X draw
					g_x_draws += 1

			v = np.inf
			for a in game.actions(state):
				v = min(v, max_value(game.result(state, a)))
			return v

		return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))


	# input_file = sys.argv[1]
	input_file = "Test.txt"
	read_file = open(input_file, 'r')  # open file
	read_file = read_file.readlines()  # Read the file lines and save as list

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
	moves = []  # list for all the empty slots, moves, available passed in GameState(namedtuple)

	# uses above list of list to put info of location of X's and O's in a dict
	for i in range(3):
		for j in range(3):
			if lines_lst[i][j] != '-':
				board_dict[(i, j)] = lines_lst[i][j]  # Ex: (1, 1): 'X'
				if lines_lst[i][j] == 'X':
					x_count += 1
				else:
					o_count += 1
			else:
				moves.append((i, j))  # where ever there's a '-' a move is available
	# print(board_dict)
	term = 0

	# to_move in GameState, determined by num of X and O's in input:
	if x_count <= o_count:
		tm = 'X'
	else:
		tm = 'O'

	game_obj = TicTacToe()  # ttt object
	game_obj.initial = GameState(tm, 0, board_dict, moves)  # Initialize the object's state

	n = guaranteed(game_obj, game_obj.initial)  # check the guaranteed win, draw, or loss in the entered state
												# and increment accordingly:
	if n == 1:
		g_x_wins += 1
	elif n == -1:
		g_x_loses += 1
	else:
		g_x_draws += 1

	m = minmax(game_obj.initial, game_obj)
	'''
	For debugging:
	
	print("G_wins: ", g_x_wins)
	print("G_losses: ", g_x_loses)
	print("G_draws: ", g_x_draws)

	
	print("Term States: ", term_state)
	print("Non-Term States: ", non_term_state)
	print("X_wins: ", x_wins)
	print("X_draws: ", x_draws)
	print("X_loses: ", x_loses)
	print("G_wins: ", g_x_wins)
	print("G_losses: ", g_x_loses)
	print("G_draws: ", g_x_draws)
	'''

	# TODO implement
	# Starting from this state, populate the full game tree.
	# The leaf nodes are the terminal states.
	# The terminal state is terminal if a player wins or there are no empty squares.
	# If a player wins, the state is considered terminal, even if there are still empty squares.
	# Answer the following questions for this game tree.
	print('How many terminal states are there?')
	print(term_state)
	print('In how many of those terminal states does X win?')
	print(x_wins)
	print('In how many of those terminal states does X lose?')
	print(x_loses)
	print('In how many of those terminal states does X draw?')
	print(x_draws)
	print('How many non-terminal states are there?')
	print(non_term_state)
	print('In how many of those non-terminal states does X have a guranteed win?')
	print(g_x_wins)
	print('In how many of those non-terminal states does X have a guranteed loss?')
	print(g_x_loses)
	print('In how many of those non-terminal states does X have a guranteed draw?')
	print(g_x_draws)
