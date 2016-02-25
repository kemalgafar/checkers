import checkersPieces as ckp

def newGameBoard():
    """Initializes a blank game board"""
    newBoard = [[ None for i in range(8)] for j in range(8)]
    return newBoard

def placePieces():
    """Places pieces in on a game board at the starting positions"""
    initialBoard = newGameBoard()
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
    return initialBoard

gameBoard = placePieces()

def returnBoard(gameBoard):
    """
    Creates an array with 64 positions that sequentially takes note
    if a space is 'empty' (None) or has a piece on it
    """
    piecesSequential = []
    ctrRow = 0
    for row in gameBoard:
        ctrCol = 0
        for val in row:
            if val != None:
                piecesSequential.append(gameBoard[ctrRow][ctrCol].dispColor())
                ctrCol += 1
            else:
                piecesSequential.append(None)
                ctrCol += 1
        ctrRow += 1
    return piecesSequential


def replaceNone(listOfVals):
    #'  ' if x == None else x for x in currentBoard
    for ind, val in enumerate(listOfVals):
        if val == None:
            listOfVals[ind] = "  "
    return listOfVals


def displayBoard(currentBoard):
    """Draws the current gameBord"""
    #use enummerate to draw the 8 rows plus get the lines for
    #each row of the 2x2 array and then refference the %s wit enum
    cb = replaceNone(currentBoard)
    
    print "  A    B    C    D    E    F    G    H      "
    print " ____ ____ ____ ____ ____ ____ ____ ____    "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  1" % (cb[0], cb[1], cb[2], cb[3], cb[4], cb[5], cb[6], cb[7])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  2" % (cb[8], cb[9], cb[10], cb[11], cb[12], cb[13], cb[14], cb[15])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  3" % (cb[16], cb[17], cb[18], cb[19], cb[20], cb[21], cb[22], cb[23])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  4" % (cb[24], cb[25], cb[26], cb[27], cb[28], cb[29], cb[30], cb[31])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  5" % (cb[32], cb[33], cb[34], cb[35], cb[36], cb[37], cb[38], cb[39])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  6" % (cb[40], cb[41], cb[42], cb[43], cb[44], cb[45], cb[46], cb[47])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  7" % (cb[48], cb[49], cb[50], cb[51], cb[52], cb[53], cb[54], cb[55])
    print "|____|____|____|____|____|____|____|____|   "
    print "|    |    |    |    |    |    |    |    |   "
    print "| %s | %s | %s | %s | %s | %s | %s | %s |  8" % (cb[56], cb[57], cb[58], cb[59], cb[60], cb[61], cb[62], cb[63])
    print "|____|____|____|____|____|____|____|____|   "



