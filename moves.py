
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

cur_state = [[None for i in xrange(8)] for j in xrange(8)]


def place_pieces(cur_state):
    """Places pieces on a game board at the starting positions"""
    initial_board = cur_state

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

    cur_state = initial_board

place_pieces(cur_state)


print cur_state

def possible_moves(cur_state, i, j, valid_spaces, hist_str):
    # need to get a recursive function to TREE through the spaces
    # only use first 2 chars from hist string that way u can keep adding onto the string
    is_red_turn = True

    #if self.is_red_turn == True:  uncomment when adding back to Board class
    if is_red_turn == True:
        enemy_1 = " B"
        enemy_2 = "KB"
    else:
        enemy_1 = " R"
        enemy_2 = "KR"

    try:
        if cur_state[i+1][j+1] == enemy_1 or enemy_2:
            try:
                if cur_state[i+2][j+2] == None:
                    valid_spaces[hist_str].append(str(i+2) + str(j+2))
                    i += 2
                    j += 2
                    possible_moves(cur_state, i, j, valid_spaces, hist_str) #need to return?
            except IndexError:
                pass
    except IndexError:
        pass


def iterate_board(cur_state, valid_spaces):
        # have this function be called twice per turn (1 red 1 black)
        # have the enemy state keep changing in the board class
    for i in xrange(8):
        for j in xrange(8):
            #append the lower func?
            hist_str = (str(i) + str(j))
            if hist_str in valid_spaces:
                possible_moves(cur_state, i, j, valid_spaces, hist_str)

iterate_board(cur_state, valid_spaces)
print valid_spaces
