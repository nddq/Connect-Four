# 
# ps9pr1.py - Problem Set 9, Problem 1
#
# A Connect Four Board class
#

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[" "] * self.width for row in range(self.height)]

    def __repr__(self):
        """
        return a single string that represents the entire board
        """
        s = ""
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' * (self.width*2 + 1) + "\n"
        for eachcolumn in range(self.width):
            s += " "+str(eachcolumn%10)
        return s

    def add_checker(self, checker, col):
        """
        add checker to board
        """
        assert (checker == 'X' or checker == 'O')
        assert (0 <= col < self.width)

        row = 0
        if self.slots[row][col] != " ":
            return
        else:
            while self.slots[row][col] == " " and (row + 1) <= (self.height - 1):
                if self.slots[row+1][col] != " ":
                    self.slots[row][col] = checker
                    return
                else:
                    row += 1
            self.slots[row][col] = checker

    def reset(self):
        """
        reset the Board object on which it is called by setting all slots to contain a space character
        """
        self.slots = [[" "] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """
        returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False.
        """
        if 0 <= col < self.width:
            if self.slots[0][col] != " ":
                return False
            else:
                return True
        else:
            return False

    def is_full(self):
        """
        returns True if the called Board object is completely full of checkers, and returns False otherwise.
        """
        col = 0
        while col < self.width:
            if self.can_add_to(col) == True:
                return False
            else:
                col += 1
        return True

    def remove_checker(self, col):
        """
        removes the top checker from column col of the called Board object. If the column is empty, then the method should do nothing.
        """
        assert (0 <= col < self.width)
        row = 0
        while row < self.height:
            if self.slots[row][col] != " ":
                self.slots[row][col] = " "
                return
            else:
                row += 1

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                        self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                        self.slots[row][col + 3] == checker:
                    return True

        return False

    def is_vertical_win(self, checker):
        """
        Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                        self.slots[row+1][col] == checker and \
                        self.slots[row+2][col] == checker and \
                        self.slots[row+3][col] == checker:
                    return True

        return False

    def is_down_diagonal_win(self, checker):
        """
        Checks for a diagonals that go down from left to right win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                        self.slots[row+1][col+1] == checker and \
                        self.slots[row+2][col+2] == checker and \
                        self.slots[row+3][col+3] == checker:
                    return True

        return False

    def is_up_diagonal_win(self, checker):
        """
        Checks for a diagonals that go up from left to right win for the specified checker.
        """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                        self.slots[row-1][col+1] == checker and \
                        self.slots[row-2][col+2] == checker and \
                        self.slots[row-3][col+3] == checker:
                    return True

        return False

    def is_win_for(self, checker):
        """
        returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return False
        """

        assert (checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker) == True or \
           self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
                    return True

        return False

