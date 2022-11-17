"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count_x = 0
    count_y = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                count_x += 1
            if board[row][col] == O:
                count_y += 1
    if count_x > count_y:
        return 0
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                action_set.add((row, col))
    return action_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a Valid Exception")

    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checktherow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkthecol(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkfirstplay(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def checksecondplay(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checktherow(board, X) or checkthecol(board, X) or checkfirstplay(board, X) or checksecondplay(board, X):
        return X
    if checktherow(board, O) or checkthecol(board, O) or checkfirstplay(board, O) or checksecondplay(board, O):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxvalue(board):
    v = - math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v

def minvalue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([minvalue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == 0:
        plays = []
        for action in actions(board):
            plays.append([maxvalue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]