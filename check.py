import string
from checkersPieces import RedPiece, BlkPiece
from gameMechanics import assignValues


class Board(object):
    def __init__(self):
	    self.cur_state = [[None for i in xrange(8)] for j in xrange(8)]
	    self.place_pieces()
        self.is_red_turn = True

    def place_pieces(self):
        """Places pieces on a game board at the starting positions"""
        initial_board = self.cur_state

        initial_board[0][1] = RedPiece()
        initial_board[0][3] = RedPiece()
        initial_board[0][5] = RedPiece()
        initial_board[0][7] = RedPiece()
        initial_board[1][0] = RedPiece()
        initial_board[1][2] = RedPiece()
        initial_board[1][4] = RedPiece()
        initial_board[1][6] = RedPiece()
        initial_board[2][1] = RedPiece()
        initial_board[2][3] = RedPiece()
        initial_board[2][5] = RedPiece()
        initial_board[2][7] = RedPiece()
        initial_board[5][0] = BlkPiece()
        initial_board[5][2] = BlkPiece()
        initial_board[5][4] = BlkPiece()
        initial_board[5][6] = BlkPiece()
        initial_board[6][1] = BlkPiece()
        initial_board[6][3] = BlkPiece()
        initial_board[6][5] = BlkPiece()
        initial_board[6][7] = BlkPiece()
        initial_board[7][0] = BlkPiece()
        initial_board[7][2] = BlkPiece()
        initial_board[7][4] = BlkPiece()
        initial_board[7][6] = BlkPiece()

        self.cur_state = initial_board

    @property
    def display(self):
        board = self.cur_state

        print "  " + "   ".join(string.ascii_lowercase[0: len(board)])
        print "  " + "   ".join(["*"] * len(board))

        for row_number, row in enumerate(board):
            row_to_print = [piece.disp_color() if piece else '  ' for piece in row]
            row_to_print.append('  ' + str(row_number))

            print "  ".join(row_to_print)

"""
def main():
    test = Board()
    test.display
    coords = assignValues()
    print "you entered" , coords
main()
"""
