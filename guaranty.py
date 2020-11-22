from games import *


# To Determine if X gets a guaranteed win, loss or draw
def guaranteed(game, state):
    gm = TicTacToe()  # create a new ttt object as to not edit the other
    gm.initial = state

    while not gm.terminal_test(gm.initial):
        m = minmax_decision(gm.initial, gm)
        gm.initial = gm.result(gm.initial, m)

    if gm.initial.utility == 1:
        # g_x_wins += 1
        return 1
    elif gm.initial.utility == -1:
        # g_x_loses -= 1
        return -1
    else:
        # g_x_draws += 1
        return 0