import checkersBoard as ckbd
import re

#need a check space func
#check if move is legal
#can have the move func test all 4 possible but have a condition to check if king and if red or black +1/-1, +1/-1

charLookUp = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def userInput():
    print "Please enter in a coordinate you would like to move to:"
    userString = raw_input(">  ")
    return userString

def checkInput():
    str = userInput().upper()
    matches = re.search(r'([a-hA-H])([1-8])\sTO\s([a-hA-H])([1-8])', str)
    if matches:   
        return [match for match in matches.groups()]        
    else:
        print "Erroneous input, please try again"
        return checkInput()

def assignValues():
    """col and row swapped need to switch then assign"""
    #use a while loop?
    while bad_Input = True:
        userInputVals = checkInput()
        bad_Input = checkValidMove(userInputVals)
        
    userMoveCoords[0] = int(userInputVals[1]) - 1
    userMoveCoords[1] = charLookUp[userInputVals[0]]
    userMoveCoords[2] = int(userInputVals[3]) - 1
    userMoveCoords[3] = charLookUp[userInputVals[2]]
    return userMoveCoords

# needs a func tocheck if inp is valid beforehand


"""
def checkIfLegal():
    coordCheck = assignValues()
    if gameBoard[coordCheck[0]][coordCheck[1]].isAlive() == True
"""

def checkValidMove(userInputVals):
    """"""
    #need to check if there is a peice selected on the sq  feedbk" err inp sel sq with piece
    #need to check if there is a piece that has moves avail (weights) select greatest? feedbk" follow rules, if move avail must take
    #need to force user (have the abv func return a list, need to pick from the list) to move it to the right spot
    #NEED A GEERERIC func to return the type of a 1/1 sq so that can use to either move or get type to eat
    #if cant eat then need to check if spce is free, then call move
    #need to check if king then recursively do the above
    if 



def move(currentState, fromX, fromY, toX, toY):
    """Moves a peice from one square to another"""
    currentState[fromX][fromY], currentState[toX][toY] = currentState[toX][toY], currentState[fromX][fromY]
    return currentState



#### user input





#### computer moves
