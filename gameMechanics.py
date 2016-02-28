from check import Board
import re

#need a check space func
#check if move is legal
#can have the move func test all 4 possible but have a condition to check if king and if red or black +1/-1, +1/-1

charLookUp = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def userInput():
    print "Please enter in a coordinate you would like to move to:"
    user_string = raw_input(">  ")
    return user_string

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
    while bad_input = True:
    
        user_input_vals = checkInput()
        
        user_move_coords = []
        user_move_coords[0] = int(user_input_vals[1]) - 1
        user_move_coords[1] = charLookUp[user_input_vals[0]]
        user_move_coords[2] = int(user_input_vals[3]) - 1
        user_move_coords[3] = charLookUp[user_input_vals[2]]
        
        bad_input = checkValidMove(user_move_coords)
        
    return user_move_coords

# needs a func tocheck if inp is valid beforehand


"""
def checkIfLegal():
    coordCheck = assignValues()
    if gameBoard[coordCheck[0]][coordCheck[1]].isAlive() == True
"""

    #need to check if there is a peice selected on the sq  feedbk" err inp sel sq with piece
    #need to check if there is a piece that has moves avail (weights) select greatest? feedbk" follow rules, if move avail must take
    #need to force user (have the abv func return a list, need to pick from the list) to move it to the right spot
    #NEED A GEERERIC func to return the type of a 1/1 sq so that can use to either move or get type to eat
    #if cant eat then need to check if spce is free, then call move
    #need to check if king then recursively do the above
    # need a func that destroys a eaten piece


def checkValidMove(user_move_coords): #has to return a bool
    """"""
    # need a func to return the # of pieces tat have possible moves
    # append all alive pieces to an array, make the array 2D? if 0 moves then array is empty
    # if 1 move then [1][append1, append2...] , [2]
    tst_arr = user_move_coords #only to save space/improve readabilty 
    if tst_arr[0], tst_arr[1] == tst_arr[2], tst_arr[3]:
        print "test case 1"
    elif Board.cur_state[tst_arr[0]][tst_arr[1]] == None:
        print "tst case 2"
    elif
    



def move(currentState, fromX, fromY, toX, toY):
    """Moves a peice from one square to another"""
    currentState[fromX][fromY], currentState[toX][toY] = currentState[toX][toY], currentState[fromX][fromY]
    return currentState



#### user input





#### computer moves
