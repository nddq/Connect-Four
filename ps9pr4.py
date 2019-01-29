#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *
class AIPlayer(Player):
    """
    a more “intelligent” computer player
    """
    def __init__(self, checker, tiebreak, lookahead):
        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        return "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"

    def max_score_column(self, scores):
        """
        takes a list scores containing a score for each column of the board, and that returns the
        index of the column with the maximum score. If one or more columns are tied for the maximum
        score, the method should apply the called AIPlayer‘s tiebreaking strategy to break the tie
        """
        max_score = 0
        cols = []
        for i in range(len(scores)):
            if scores[i] > max_score:
                max_score = scores[i]
                cols = [i]
            elif scores[i] == max_score:
                cols += [i]
        if self.tiebreak == "LEFT":
            return cols[0]
        elif self.tiebreak == "RIGHT":
            return cols[-1]
        else:
            return random.choice(cols)


    def scores_for(self, board):
        """
        takes a Board object board and determines the called AIPlayer‘s scores for the columns in board.
        """
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                temp_p = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                temp_scores = temp_p.scores_for(board)
                if max(temp_scores) == 50:
                    scores[col] = 50
                elif max(temp_scores) == 100:
                    scores[col] = 0
                elif max(temp_scores) == 0:
                    scores[col] = 100
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        self.num_moves += 1
        pos_move = self.scores_for(board)
        return self.max_score_column(pos_move)

connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))