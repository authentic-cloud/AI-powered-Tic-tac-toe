 import math
from copy import deepcopy

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
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        count = count + row.count(X) - row.count(O)
    return X if count == 0 else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = deepcopy(board)    
    if board[i][j] == EMPTY:
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("Cell is not empty")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Transpose the board
    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
    # Find diagonals of the board
    diagonals = [[row[i] for i, row in enumerate(board)], [row[len(row) - 1 - i] for i, row in enumerate(board)]]
    # Create a list of all possible rows
    rows = board + transposed_board + diagonals
    # Return the winner of the game, if there is one
    for row in rows:
        if row.count(row[0]) == len(row):
            return row[0]
    # Return None if there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for row in board:
            for cell in row:
                if cell == EMPTY:
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


def minimax_value(state):
    """
    Returns utility value if an optimal action is played for the current player on the board.
    """   
    if terminal(state):
        return utility(state)
    if player(state) == X:
        func = max
        v = - math.inf
    else:
        func = min
        v = math.inf
    for action in actions(state):
        v = func(v, minimax_value(result(state, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """    
    for action in actions(board):
        if minimax_value(board) == minimax_value(result(board, action)):
            return action
