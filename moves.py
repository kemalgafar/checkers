
opponent = {" R":"B", "KR":"B", " B":"R", "KB":"R"}

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

######
"""
is_red_turn = True

def playTurn():
    possible_capture = False

    space_color = Board.cur_state[x_coord][y_coord].dispColor()

    possible_capture = verify_captures(Board.cur_state, x_coord, y_coord)

def verify_captures(Board.cur_state, x_coord, y_coord):
"""
# test matrix


#print possible_moves

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

def possible_moves(cur_state, i, j, valid_spaces):
    hist_key = str(i) + str(j)
    #NEED TO ACCOUNT FOR INDEX OUT OF RANGE
    # take out the (i <...) (j<...)
    # handle the exception, maybe just Break from that iteration?
    # need to get a recursive function to TREE through the spaces
    # instead MAKE i AND j A FUNCTION OF BOARD LENGTH ?????????
    if (i < 7) and (j < 7) and cur_state[i+1][j+1] == "B":  #MESSY NEED TO FIX
        if (i < 6) and (j < 6) and cur_state[i+2][j+2] == None:
            valid_spaces[hist_key].append(str(i+2) + str(j+2))
    print hist_key  # leave in  shows how many times the nested for loops iterated
    # why is it 77?

# I DONT LIKE THE IDEA OF calling a function 64 times thru 2 nested loops
# maybe just get the possible moves func to iterate itself, no need to nest functions

def iterate_board(cur_state, valid_spaces):
    for i in xrange(8):
        for j in xrange(8):
            #append the lower func?
            possible_moves(cur_state, i, j, valid_spaces)

iterate_board(cur_state, valid_spaces)
print valid_spaces
'''
def possibleCapure(cur_state):

    for


'''
