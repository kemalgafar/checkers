from check import Board
import re

char_look_up = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def user_input():
    print "Please enter in a coordinate you would like to move to:"
    user_string = raw_input(">  ")
    return user_string

def check_input():
    str = user_input().upper()
    matches = re.search(r'([a-hA-H])([1-8])\sTO\s([a-hA-H])([1-8])', str)
    if matches:
        return [match for match in matches.groups()]
    else:
        print "Erroneous input, please try again"
        return check_input()

def assign_values():
    """col and row swapped need to switch then assign"""
    while bad_input = True:

        user_input_vals = check_input()

        user_move_coords = []
        user_move_coords[0] = int(user_input_vals[1]) - 1
        user_move_coords[1] = char_look_up[user_input_vals[0]]
        user_move_coords[2] = int(user_input_vals[3]) - 1
        user_move_coords[3] = char_look_up[user_input_vals[2]]
        # if the first two inputs aka the space 'from' isnt located within the possible moves dict, then prompt again and throw a error



        #bad_input = checkValidMove(user_move_coords)
        
    return user_move_coords


def move(current_state, fromX, fromY, toX, toY):
    """Moves a peice from one square to another"""
    current_state[fromX][fromY], current_state[toX][toY] = current_state[toX][toY], current_state[fromX][fromY]
    return current_state
