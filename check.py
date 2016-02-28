import string
from checkersPieces import RedPiece, BlkPiece
from gameMechanics import assignValues


class Board(object):
    def __init__(self):
	    self.cur_state = [[None for i in xrange(8)] for j in xrange(8)]
	    self.placePieces()
    
    def placePieces(self):
        """Places pieces on a game board at the starting positions"""
        initialBoard = self.cur_state
           
        initialBoard[0][1] = RedPiece()
        initialBoard[0][3] = RedPiece()
        initialBoard[0][5] = RedPiece()
        initialBoard[0][7] = RedPiece()
        initialBoard[1][0] = RedPiece()
        initialBoard[1][2] = RedPiece()
        initialBoard[1][4] = RedPiece()
        initialBoard[1][6] = RedPiece()
        initialBoard[2][1] = RedPiece()
        initialBoard[2][3] = RedPiece()
        initialBoard[2][5] = RedPiece()
        initialBoard[2][7] = RedPiece()
        initialBoard[5][0] = BlkPiece()
        initialBoard[5][2] = BlkPiece()
        initialBoard[5][4] = BlkPiece()
        initialBoard[5][6] = BlkPiece()
        initialBoard[6][1] = BlkPiece()
        initialBoard[6][3] = BlkPiece()
        initialBoard[6][5] = BlkPiece()
        initialBoard[6][7] = BlkPiece()
        initialBoard[7][0] = BlkPiece()
        initialBoard[7][2] = BlkPiece()
        initialBoard[7][4] = BlkPiece()
        initialBoard[7][6] = BlkPiece()
        
        self.cur_state = initialBoard
    
    @property
    def display(self):
        board = self.cur_state

        print "  " + "   ".join(string.ascii_lowercase[0: len(board)])
        print "  " + "   ".join(["*"] * len(board))

        for row_number, row in enumerate(board):
            row_to_print = [piece.dispColor() if piece else '  ' for piece in row]
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

