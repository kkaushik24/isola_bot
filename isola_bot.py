import random
N = 7
BLOCKED = -1
OPEN_AREA = 0 
board = []


def read_board():
    for i in range(N):
        row = map(int, raw_input().split())
        board.append(row)


def get_player_position():
    for i in range(N):
        for j in range(N):
            if board[i][j] == player_id:
                return i, j


def move_left(x, y):
    possible = False
    if y-1 >= 0 and board[x][y-1] == OPEN_AREA:
        possible = True
    return possible, x, y-1


def move_right(x, y):
    possible = False
    if y+1 < N and board[x][y+1] == OPEN_AREA:
        possible = True
    return possible, x, y+1

def move_top(x,y):
	possible = False
	if x-1  >= 0 and board[x-1][y] == OPEN_AREA:
		possible =True
	return possible,x-1,y

def move_bottom(x,y):
	possible = False
	if x+1  < N and board[x+1][y] == OPEN_AREA:
		possible =True
	return possible,x+1,y


def move_top_left(x,y):
	possible = False
	if x-1 >=0 and y-1 >=0 and board[x-1][y-1] == OPEN_AREA:
		possible = True
	return possible,x-1,y-1


def move_top_right(x,y):
	possible = False
	if x-1 >= 0 and y+1 < N and board[x-1][y+1] == OPEN_AREA:
		possible = True
	return possible,x-1,y+1


def move_bottom_left(x,y):
	possible = False
	if x+1 <N and y-1 >=0 and board[x+1][y-1] == OPEN_AREA:
		possible = True
	return possible,x+1,y-1


def move_bottom_right(x,y):
	possible = False
	if x+1 <N and y+1 <N and board[x+1][y+1] == OPEN_AREA:
		possible = True
	return possible,x+1,y+1

move_funcs=[move_top, move_top_left, move_top_right,
			move_bottom, move_bottom_left, move_bottom_right,
			move_left, move_right]
opponent_move_funcs = [move_bottom, move_bottom_left, move_bottom_right,
			move_top, move_top_left, move_top_right,
			move_left, move_right]

def get_opponent_id():
    if player_id == 1:
        return 2
    if player_id == 2:
        return 1


def get_opponent_position():
    for i in range(N):
        for j in range(N):
            if board[i][j] == get_opponent_id():
                return i, j


def available_neighbor_moves_index(x, y):
    available_moves = []
    for k, func in enumerate(move_funcs):
        possible, move_x, move_y = func(x, y)
        if possible:
            available_moves.append(k)
    return available_moves

def prioritize_player_move(available_moves, x, y):
	priority_list = []
	for index in available_moves:
		possible, move_x, move_y = move_funcs[index](x,y)
		if possible:
			possible_moves_count = len(available_neighbor_moves_index(move_x, move_y))
			priority_list.append((index, possible_moves_count))
	priority_list.sort(key = lambda x:x[1],reverse = True)
	moves =[value[0] for value in priority_list if priority_list[0][0] ==value[0] ]
        random.shuffle(moves)
	return moves[0]


def available_cross_area():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i,j

def player_cross():
    player_x, player_y = get_opponent_position()
    available_moves = available_neighbor_moves_index(player_x, player_y)
    if available_moves:
        if len(available_moves)<4: 
            player_prioritized_move = prioritize_player_move(available_moves,player_x, player_y)
            possible, cross_x, cross_y = move_funcs[player_prioritized_move](player_x, player_y)
            board[cross_x][cross_y] = -1
            return cross_x, cross_y
        else:
            for func in opponent_move_funcs:
               possible,move_x,move_y = func(player_x, player_y)
               if possible:
                   return move_x,move_y

            
    else:
        cross_x,cross_y = available_cross_area()
        board[cross_x][cross_y] = -1
        return cross_x, cross_y

def player_move():
    player_x, player_y = get_player_position()

    available_moves = available_neighbor_moves_index(player_x, player_y)
		
    if len(available_moves)<4:
        move_index = random.randint(0, len(available_moves)-1)
        player_prioritized_move = prioritize_player_move(available_moves,player_x, player_y)
        possible, move_x, move_y = move_funcs[player_prioritized_move](player_x, player_y)
        board[move_x][move_y] = player_id
        board[player_x][player_y] = 0
        return move_x, move_y
    else:
    	random.shuffle(move_funcs)
    	for func in move_funcs:
            possible,move_x,move_y = func(player_x, player_y)
    	    if possible and move_x!=0 and move_x!=N-1 and move_y!=0 and move_y!=N-1:
                return move_x,move_y
        for func in move_funcs:
            possible,move_x,move_y = func(player_x, player_y)
            if possible:
                return move_x,move_y




read_board()
player_id = input()

cross_x, cross_y = player_cross()
player_x, player_y = player_move()


print str(player_x)+" "+str(player_y)
print str(cross_x)+" "+str(cross_y)

