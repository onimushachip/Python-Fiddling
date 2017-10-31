from mancala import *

class PlayerTwo(mancala_player):
    def claculate_utility(self, boardstate):
        return test_utility(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)

def test_utility(boardstate):
    # a = boardstate._board[P1Mancala]
    # print(a)
    mancalaOne = boardstate._board[P0Mancala] - boardstate._board[P1Mancala]
    mancalaTwo = boardstate._board[P1Mancala] - boardstate._board[P0Mancala]
    if (boardstate.to_move == P0):
        for pos in range(P0Start, P0Mancala+1):
            if boardstate._board[pos] == 0:
                mancalaOne -= 1
        return mancalaOne
    else:
        for pos in range(P1Start, P1Mancala+1):
            if boardstate._board[pos] == 0:
                mancalaTwo += 1
        return mancalaTwo
    # return 0