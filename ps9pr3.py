#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """
    The function will perform all of the steps involved in processing a single move by the specified player on the specified board.
    """
    print(str(player) + "'s turn")
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print()
    print(board)
    if board.is_win_for(player.checker):
        print(str(player) + " wins in " + str(player.num_moves) + " moves.")
        print("Congratulations")
        return True
    else:
        if board.is_full():
            print("It's a tie!")
            return True
        else:
            return False

class RandomPlayer(Player):
    """
    an unintelligent computer player that chooses at random from the available columns
    """
    def __init__(self, checker):
        super().__init__(checker)

    def next_move(self, board):
        self.num_moves += 1
        collist = [eachcol for eachcol in range(board.width) if board.can_add_to(eachcol)]
        return random.choice(collist)






