#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    def __init__(self, checker):
        assert (checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """
        returns a string representing a Player object
        """
        return "Player " + self.checker

    def opponent_checker(self):
        """
        returns a one-character string representing the checker of the Player object’s opponent
        """
        if self.checker == "X":
            return "O"
        return "X"

    def next_move(self, board):
        """
        returns the column where the player wants to make the next move
        """
        self.num_moves += 1
        while True:
            col = int(input("Enter a column:"))
            if col in range(board.width) and board.can_add_to(col):
                return col
            print("Try again!")

