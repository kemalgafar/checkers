class Piece(object):
    def __init__(self):
        self.isAlive = True
        self.isKing = False
        #self.coordX = None
        #self.coordY = None
    
    # do these 2 need to be funcs? can just be variables to be overwritten    
    def isDead(self):
        self.isAlive = False
        
    def isKing(self):
        self.isKing = True

class RedPiece(Piece):
    
    def dispColor(self):
        if self.isKing == True:  #isking && isalive
            color = "KR"
        else:    #else if if alive
            color = " R"
        return color
    #else turn to None?
class BlkPiece(Piece):
    
    def dispColor(self):
        if self.isKing == True:
            color = "KB"
        else:
            color = " B"
        return color

    
    
