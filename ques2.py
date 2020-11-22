# TODO import the necessary classes and methods
import sys
from games import *

if __name__ == '__main__':

    term_state = 0
    non_term_state = -1
    x_wins = 0
    x_loses = 0
    x_draws = 0

    def minmax(state, game):
        """Given a state in a game, calculate the best move by searching
        forward all the way to the terminal states. [Figure 5.3]"""
        player = game.to_move(state)

        def max_value(state):
            if game.terminal_test(state):
                term_state += 1
                if game.utility(state, player) == 1:
                    x_wins += 1
                elif game.utility(state, player) == -1:
                    x_loses += 1
                else:
                    x_draws += 1
                return game.utility(state, player)
            else:
                non_term_state += 1
            v = -np.inf
            for a in game.actions(state):
                v = max(v, min_value(game.result(state, a)))
            return v

        def min_value(state):
            if game.terminal_test(state):
                term_state += 1
                if game.utility(state, player) == 1:
                    x_wins += 1
                elif game.utility(state, player) == -1:
                    x_loses += 1
                else:
                    x_draws += 1
                return game.utility(state, player)
            else:
                non_term_state += 1
            v = np.inf
            for a in game.actions(state):
                v = min(v, max_value(game.result(state, a)))
            return v

        # Body of minmax_decision:
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
    moves = []
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

    # to_move in GameState, determined by num of X and O's in input
    if x_count <= o_count:
        tm = 'X'
    else:
        tm = 'O'

    game_obj = TicTacToe()
    game_obj.initial = GameState(tm, 0, board_dict, moves)

    m = minmax(game_obj.initial, game_obj)
    print("Term States: ", term_state)
    print("Non-Term States: ", non_term_state)
    print("X_wins: ", x_wins)
    print("X_draws: ", x_draws)
    print("X_loses: ", x_loses)

    # For debugging:
    ''' 
    print(board_dict)
    print(tm)
    print(moves)

    # TODO implement

    # Starting from this state, populate the full game tree.
    # The leaf nodes are the terminal states.
    # The terminal state is terminal if a player wins or there are no empty squares.
    # If a player wins, the state is considered terminal, even if there are still empty squares.
    # Answer the following questions for this game tree.
    print('How many terminal states are there?')
    # TODO print the answer
    print('In how many of those terminal states does X win?')
    # TODO print the answer
    print('In how many of those terminal states does X lose?')
    # TODO print the answer
    print('In how many of those terminal states does X draw?')
    # TODO print the answer
    print('How many non-terminal states are there?')
    # TODO print the answer
    print('In how many of those non-terminal states does X have a guranteed win?')
    # TODO print the answer
    print('In how many of those non-terminal states does X have a guranteed loss?')
    # TODO print the answer
    print('In how many of those non-terminal states does X have a guranteed draw?')
    # TODO print the answer
    '''
