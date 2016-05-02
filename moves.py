"""
valid_spaces = {
    "01":[], "03":[], "05":[], "07":[],
    "10":[], "12":[], "14":[], "16":[],
    "21":[], "23":[], "25":[], "27":[],
    "30":[], "32":[], "34":[], "36":[],
    "41":[], "43":[], "45":[], "47":[],
    "50":[], "52":[], "54":[], "56":[],
    "61":[], "63":[], "65":[], "67":[],
    "70":[], "72":[], "74":[], "76":[],
    }
    #commented out for testing
"""
valid_spaces = {
    "01":[], "03":[]
    }
cur_state = [[None for i in xrange(8)] for j in xrange(8)]

def place_pieces(cur_state):
    """Places pieces on a game board at the starting positions"""
    initial_board = cur_state

    initial_board[0][3] = " R"
    initial_board[1][2] = " B"
    initial_board[1][4] = " B"
    initial_board[3][4] = " B"
    initial_board[3][6] = " B"
    initial_board[5][2] = " B"

    cur_state = initial_board

    """
    initial_board[0][1] = "R"
    initial_board[0][3] = "R"
    initial_board[0][5] = "R"
    initial_board[0][7] = "R"
    initial_board[1][0] = "R"
    initial_board[1][2] = "R"
    initial_board[1][4] = "R"
    initial_board[1][6] = "R"
    initial_board[2][1] = "R"
    initial_board[3][2] = "B"  #######
    initial_board[2][5] = "R"
    initial_board[2][7] = "R"
    initial_board[5][0] = "B"
    initial_board[5][2] = "B"
    initial_board[5][4] = "B"
    initial_board[5][6] = "B"
    initial_board[6][1] = "B"
    initial_board[6][3] = "B"
    initial_board[6][5] = "B"
    initial_board[6][7] = "B"
    initial_board[7][0] = "B"
    initial_board[7][2] = "B"
    initial_board[7][4] = "B"
    initial_board[7][6] = "B"
    """

place_pieces(cur_state)

def possible_moves(cur_state, i, j, valid_spaces, hist_str, move_str):

    """
    have all the is red turn stuff out of the moves functs
    make a func and call it

    have a master counter 0, 1, 2... in the Board class
    even #s represent the first half of the turn, odd is second
    have the is_red_turn func just mod2 the counter to determine red/black turn
    """
    is_red_turn = True

    #if self.is_red_turn == True:  uncomment when adding back to Board class
    if is_red_turn == True:
        enemy_1 = " B"
        enemy_2 = "KB"
        self_1 = " R"
        self_2 = "KR"
    else:
        enemy_1 = " R"
        enemy_2 = "KR"
        self_1 = " B"
        self_2 = "KB"


    '''
    have logic (if else) control
    if red or is_king do func1 func2
    else if ....
    '''

    new_i = i
    new_j = j

#make 4 funcs  need to call at the same time/ i/j will change, before call of func can check is king?
    try:
        move_p1_p1(cur_state, new_i, new_j, valid_spaces, hist_str, move_str, enemy_1, enemy_2)
        move_p1_m1(cur_state, new_i, new_j, valid_spaces, hist_str, move_str, enemy_1, enemy_2)
    except IndexError:
        pass

def move_p1_p1(cur_state, new_i, new_j, valid_spaces, hist_str, move_str, enemy_1, enemy_2):
    if cur_state[new_i+1][new_j+1] == enemy_1 or cur_state[new_i+1][new_j+1] == enemy_2:
        try:
            if cur_state[new_i+2][new_j+2] == None:
                new_i += 2
                new_j += 2
                if (new_i < 8) and (new_j < 8):
                    move_str += (str(new_i) + str(new_j))
                    valid_spaces[hist_str].append(move_str)
                    i = new_i
                    j = new_j
                    possible_moves(cur_state, i, j, valid_spaces, hist_str, move_str)
        except IndexError:
            pass

def move_p1_m1(cur_state, new_i, new_j, valid_spaces, hist_str, move_str, enemy_1, enemy_2):
    if cur_state[new_i+1][new_j-1] == enemy_1 or cur_state[new_i+1][new_j-1] == enemy_2:
        try:
            if cur_state[new_i+2][new_j-2] == None:
                new_i += 2
                new_j -= 2
                if (new_i < 8) and (new_j > -1):
                    move_str += (str(new_i) + str(new_j))
                    valid_spaces[hist_str].append(move_str)
                    i = new_i
                    j = new_j
                    possible_moves(cur_state, i, j, valid_spaces, hist_str, move_str)
        except IndexError:
            pass


def iterate_board(cur_state, valid_spaces):
        # have this function be called twice per turn (1 red 1 black)
        # have the enemy state keep changing in the board class
        # maybe pass in a tuple? a 2 member list? etc..
    for i in xrange(8):
        for j in xrange(8):
            #append the lower func?
            hist_str = (str(i) + str(j))
            if hist_str in valid_spaces and cur_state[i][j] == " R":
                move_str = hist_str  #is passing this in nessecary
                possible_moves(cur_state, i, j, valid_spaces, hist_str, move_str)

iterate_board(cur_state, valid_spaces)
print valid_spaces
