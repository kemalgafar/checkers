import string
import checkersPieces as ckp
from gameMechanics import assignValues


class Board(object):
    def __init__(self):
	    self.cur_state = [[None for i in range(8)] for j in range(8)]
	    self.placePieces()
    
    def placePieces(self):
        """Places pieces in on a game board at the starting positions"""
        initialBoard = self.cur_state
           
        initialBoard[0][1] = ckp.RedPiece()
        initialBoard[0][3] = ckp.RedPiece()
        initialBoard[0][5] = ckp.RedPiece()
        initialBoard[0][7] = ckp.RedPiece()
        initialBoard[1][0] = ckp.RedPiece()
        initialBoard[1][2] = ckp.RedPiece()
        initialBoard[1][4] = ckp.RedPiece()
        initialBoard[1][6] = ckp.RedPiece()
        initialBoard[2][1] = ckp.RedPiece()
        initialBoard[2][3] = ckp.RedPiece()
        initialBoard[2][5] = ckp.RedPiece()
        initialBoard[2][7] = ckp.RedPiece()
        initialBoard[5][0] = ckp.BlkPiece()
        initialBoard[5][2] = ckp.BlkPiece()
        initialBoard[5][4] = ckp.BlkPiece()
        initialBoard[5][6] = ckp.BlkPiece()
        initialBoard[6][1] = ckp.BlkPiece()
        initialBoard[6][3] = ckp.BlkPiece()
        initialBoard[6][5] = ckp.BlkPiece()
        initialBoard[6][7] = ckp.BlkPiece()
        initialBoard[7][0] = ckp.BlkPiece()
        initialBoard[7][2] = ckp.BlkPiece()
        initialBoard[7][4] = ckp.BlkPiece()
        initialBoard[7][6] = ckp.BlkPiece()
        
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
            
def main():
    test = Board()
    test.display
    coords = assignValues()
    print "you entered" , coords
main()
