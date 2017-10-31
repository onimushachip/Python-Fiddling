
from mancala import *

class PlayerOne(mancala_player):
    # This should return the utility of the given boardstate.
    # It can access (but not modify) the to_move and _board fields.
    def calculate_utility(self, boardstate):
        return simple_utility(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        # This should return a tuple of (cutoffDepth, cutoffTest, evalFn)
        # where any (or all) of the values can be None, in which case the
        # default values are used:
        #        cutoffDepth default is 4
        #        cutoffTest default is None, which just uses cutoffDepth to
        #            determine whether to cutoff search
        #        evalFn default is None, which uses your boardstate_utility_fn
        #            to evaluate the utility of board states.
        return (4, None, None)

class PlayerTwo(mancala_player):
    def claculate_utility(self, boardstate):
        return test_utility(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)

def simple_utility(boardstate):
    # return (boardstate.PlayerPieceCount(boardstate.to_move)
    #         - boardstate.PlayerPieceCount(opponent(boardstate.to_move)))
    # return 0
    if boardstate.to_move == P0:
        return boardstate._board[P0Mancala] - boardstate._board[P1Mancala]
    else:
        return boardstate._board[P1Mancala] - boardstate._board[P0Mancala]

def test_utility(boardstate):
    # a = boardstate._board[P1Mancala]
    # print(a)
    mancalaOne = boardstate._board[P0Mancala] - boardstate._board[P1Mancala]
    mancalaTwo = boardstate._board[P1Mancala] - boardstate._board[P0Mancala]
    if (boardstate.to_move == P0):
        for pos in range(P0Start, P0Mancala+1):
            if boardstate._board[pos] == 0:
                mancalaOne -= 10
        return mancalaOne
    else:
        for pos in range(P1Start, P1Mancala+1):
            if boardstate._board[pos] == 0:
                mancalaTwo += 1
        return mancalaTwo
    # return 0
# After "running" this module, to play a game type:
play_mancala(None, 600, PlayerOne("Bot"), PlayerTwo("Lam"))

# The above plays your player against itself, using the names
# Fred and Bob.  You could try having two different classes that
# use different strategies and play them against each other.



