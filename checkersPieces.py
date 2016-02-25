class Piece(object):
    def __init__(self):
        self.isAlive = True
        self.isKing = False
        #self.coordX = None
        #self.coordY = None
        
    def isDead(self):
        self.isAlive = False
        
    def isKing(self):
        self.isKing = True

class RedPiece(Piece):
    
    def dispColor(self):
        if self.isKing == True:
            color = "KR"
        else:
            color = " R"
        return color

class BlkPiece(Piece):
    
    def dispColor(self):
        if self.isKing == True:
            color = "KB"
        else:
            color = " B"
        return color

    
    
