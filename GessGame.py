# Author: Nick Osborne
# Date: 5/26/2020
# Description: Gess game

class Gess:
    def __init__(self):
        """" initializes game: sets status, whose turn it is, and starting
        positions"""
        self.__dict__ = {
            "X": "WHITE",
            "O": "BLACK",
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "11": 11,
            "12": 12,
            "13": 13,
            "14": 14,
            "15": 15,
            "16": 16,
            "17": 17,
            "18": 18,
            "19": 19
        }
        self._status = 'UNFINISHED'
        self._turn = "X"
        self._board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ",  " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "X", " ", "X", " ", "X", "X", "X", "X",
                        "X", "X", "X", "X", " ", "X", " ", "X", " ", " "],
                       [" ", "X", "X", "X", " ", "X", " ", "X", "X", "X",
                        "X", " ", "X", " ", "X", " ", "X", "X", "X", " "],
                       [" ", " ", "X", " ", "X", " ", "X", "X", "X", "X",
                        "X", "X", "X", "X", " ", "X", " ", "X", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "X", " ", " ", "X", " ", " ", "X", " ",
                        " ", "X", " ", " ", "X", " ", " ", "X", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "O", " ", " ", "O", " ", " ", "O", " ",
                        " ", "O", " ", " ", "O", " ", " ", "O", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "O", " ", "O", " ", "O", "O", "O", "O",
                        "O", "O", "O", "O", " ", "O", " ", "O", " ", " "],
                       [" ", "O", "O", "O", " ", "O", " ", "O", "O", "O",
                        "O", " ", "O", " ", "O", " ", "O", "O", "O", " "],
                       [" ", " ", "O", " ", "O", " ", "O", "O", "O", "O",
                        "O", "O", "O", "O", " ", "O", " ", "O", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]


    def display(self):
        """func for printing board to screen"""
        for i in range(0, 20):
            for y in range(0, 20):
                if y ==19:
                    print(self._board[i][y])
                else:
                    print(" " + self._board[i][y] + " " + "|", end="")

    def get_game_state(self):
        """returns the current status of the game"""
        return self._status

    def set_game_state(self, state):
        """changes the current state of the game, options include UNFINISHED,
        BLACK_WON, WHITE_WON"""
        self._status = state

    def resign_game(self, player):
        """allows a player to resign, calls set_game_state()"""
        pass

    def make_move(self, old_pos, new_pos):
        """ takes 2 coordinates as input and will make the move if it is
        legal, calls  get_coordinates legal_move()"""
        coordinates = self.get_coordinates(old_pos,new_pos)
        # if coordinate was invalid return False
        if not coordinates:
            return False
        print(coordinates)
        piece = self.get_piece(coordinates[0], coordinates[1])
        print(piece)
        # if piece is invalid return false
        if not self.validate_piece(piece):
            return False


    def legal_move(self):
        """ checks if proposed move is legal: coordinates inbounds, doesn't
        break any rules, returns True/False"""

        # calculate possible moves from current piece
        # if NW contains char,
        pass
    def get_coordinates(self, old, new):
        """takes 2 input strings as coordinates and converts them to list
        indices for the board, returns a list of integers as x and y
        coordinates;
        returns False if invalid input"""

        x1 = ""
        x2 = ""
        y1 = ""
        y2 = ""

        try:
            x1 = self.__dict__[old[0].lower()]
            y1 = 20 - int(old[1:])
            x2 = self.__dict__[new[0].lower()]
            y2 = 20 - int(new[1:])

        # if  a letter not in [a-t] or a special character is entered return
        # False
        except KeyError or ValueError:
            print("invalid coordinates")
            return False

        # if coordinates are not withing the 18x18 grid return False
        if y1 not in range(1,19) or y2 not in range(1,19) or x1 not in range(
                1,19) or x2 not in range(1,19):
            print("invalid coordinates")
            return False
        return [x1,y1,x2,y2]

    def get_piece(self, x, y):
        """accepts a list with an x and y coordinate, returns a list  of the
        surrounding piece values"""
        piece = []

        piece.append(self._board[y-1][x-1])     # NW
        piece.append(self._board[y-1][x])       # N
        piece.append(self._board[y-1][x+1])     # NE
        piece.append(self._board[y][x-1])       # W
        piece.append(self._board[y][x])         # C
        piece.append(self._board[y][x+1])       # E
        piece.append(self._board[y+1][x-1])     # SW
        piece.append(self._board[y+1][x])       # S
        piece.append(self._board[y+1][x+1])     # SE

        return piece

    @staticmethod
    def validate_piece(piece):
        """validates selected piece (list of strings).
                False Conditions:
                    all blanks
                    different characters (Xs and Os)
                    single char in center
        """
        x_count = 0
        o_count = 0
        blank_count = 0
        for char in piece:
            if char == 'X':
                x_count += 1
            if char == 'O':
                o_count += 1
            if char == ' ':
                blank_count += 1

        if x_count > 0 and o_count > 0:
            print("piece contains multiple players' pieces")
            return False
        if x_count == 0 and o_count == 0:
            print("blank piece")
            return False
        if piece[4] != ' ' and blank_count == 8:
            print("single center piece")
            return False
        return True

g = Gess()
g.display()

g.make_move("i7", "g8")
