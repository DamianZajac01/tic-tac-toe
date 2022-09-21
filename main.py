def display_board(game_board):
    for key in game_board.keys():
        if key == 3 or key == 6 or key == 9:
            print(f'{game_board[key]}', end=' ')
        else:
            print(f'{game_board[key]}', end=' | ')
        if key == 3 or key == 6:
            print('\n----------')
    print('\n')


def check_position(position):
    if board[position] != players[0] and board[position] != players[1]:
        return True
    return False


def player_move():
    global should_play
    display_board(board)
    if check_for_empty_field():
        num_of_field = int(input("Your move: "))
        try:
            if check_position(num_of_field):
                board[num_of_field] = players[0]
                if check_for_win():
                    display_board(board)
                    print('You won!')
                    should_play = False
            else:
                print('Position is already taken!')
                player_move()
        except KeyError:
            print('Wrong position!')
            player_move()
    else:
        if check_for_draw():
            print('Draw!')
            should_play = False


def computer_move():
    global should_play
    best_score = -1000
    best_move = 0

    if check_for_empty_field():
        display_board(board)
        for key in board.keys():
            if board[key] == ' ':
                board[key] = players[1]
                score = minimax(board, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
                    best_move = key

        board[best_move] = players[1]
        print(f'Computer move: {best_move}')

        if check_for_win():
            display_board(board)
            print('Computer has won!')
            should_play = False
    else:
        if check_for_draw():
            display_board(board)
            print('Draw!')
            should_play = False


def minimax(game_board, maximizing):
    if check_who_won(players[1]):
        return 1
    elif check_who_won(players[0]):
        return -1
    elif check_for_draw():
        return 0

    if maximizing:
        best_score = -1000
        for key in game_board.keys():
            if game_board[key] == ' ':
                game_board[key] = players[1]
                score = minimax(game_board, False)
                game_board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 1000
        for key in game_board.keys():
            if game_board[key] == ' ':
                game_board[key] = players[0]
                score = minimax(game_board, True)
                game_board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def check_for_win():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True

    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True

    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True

    else:
        return False


def check_who_won(symbol):
    if board[1] == board[2] and board[1] == board[3] and board[1] == symbol:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == symbol:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == symbol:
        return True

    elif board[1] == board[4] and board[1] == board[7] and board[1] == symbol:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == symbol:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == symbol:
        return True

    elif board[1] == board[5] and board[1] == board[9] and board[1] == symbol:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == symbol:
        return True

    else:
        return False


def check_for_draw():
    if not check_for_win() and not check_for_empty_field():
        return True
    return False


def check_for_empty_field():
    for key in board.keys():
        if board[key] == ' ':
            return True
    return False


should_play = True
players = ['O', 'X']
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' ',
}

while should_play:
    player_move()
    computer_move()
