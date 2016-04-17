class Piece(object):
    def __init__(self):
        self.is_king = False

    def is_king(self):
        self.is_king = True

class RedPiece(Piece):

    def disp_color(self):
        if self.is_king == True:
            color = "KR"
        else:
            color = " R"
        return color

class BlkPiece(Piece):

    def disp_color(self):
        if self.is_king == True:
            color = "KB"
        else:
            color = " B"
        return color
