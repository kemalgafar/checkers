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
    matches = re.search(r'([A-H])([1-8])\sTO\s([A-H])([1-8])', str)
    if matches:   
        return [match for match in matches.groups()]        
    else:
        print "Erroneous input, please try again"
        return checkInput()

def assignValues():
    """col and row swapped need to switch then assign"""
    #Theres a bug here where if the user puts in a wrong string first
    #then 2nd go around a good one, theres a 
    userMoveCoords = [0, 0, 0, 0]
    userInputVals = checkInput()
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




def move(currentState, fromX, fromY, toX, toY):
    """Moves a peice from one square to another"""
    currentState[fromX][fromY], currentState[toX][toY] = currentState[toX][toY], currentState[fromX][fromY]
    return currentState


#### user input





#### computer moves
