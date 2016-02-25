import checkersBoard as ckbd
import gameMechanics as gmec

#need a move() function
#use a dict for player input, 1. split the string then use A:0, B:1 etc

#this gets an initially filled board run at beg once
#currentState is the board that will be playyed on
currentState = ckbd.gameBoard

#these two need to be called together
#each turn currentState needs to be updated
#put in a while loop have the counter end when the # of dead pieces = for any one color
#the deadRead deadBlack counters can work to display the score also
ckbd.displayBoard(ckbd.returnBoard(currentState))


#can ask if you want to go first or the comp
#have it switch just like in lpthw
'''
currentState = gmec.move(currentState, 2, 1, 3, 2)

ckbd.displayBoard(ckbd.returnBoard(currentState))
'''
coords = gmec.assignValues()

currentState = gmec.move(currentState, coords[0], coords[1], coords[2], coords[3])

ckbd.displayBoard(ckbd.returnBoard(currentState))
