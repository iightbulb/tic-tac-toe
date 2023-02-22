import random
import numpy as np


# create board
def create_board():
    board = np.array([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
    return board


def is_win(board, current_player):
    win = False
    # for horizontal row
    for row in board:
        if (row == current_player).all():
            print(f'\n{current_player} wins!')
            print_board()
            win = True

    # verticals
    for row in board.T:
        if (row == current_player).all():
            print(f'\n{current_player} wins!')
            print_board()
            win = True

    # diagonals

    if board[0, 0] == board[1, 1] == board[2, 2] or board[0, 2] == board[1, 1] == board[2, 0] == current_player:
        print(f'\n{current_player} wins!')
        print_board()
        win = True

    return win


def print_board():
    for i in game_board:
        print('\n')
        for j in i:
            print(f'{j} ', end=' ')
    print('\n')


def change_player(current_player):
    return 'X' if current_player == '0' else '0'


def place_piece(current_player, locx, locy, board):
    board[locx, locy] = current_player


# assign starting player
player = 'X' if random.randint(0, 1) == 1 else '0'

# create game board
game_board = create_board()

# loop that breaks only if a player has won
game_running = True
while game_running:
    turns = 0
    # print current board
    print_board()

    # player input - location of x or o
    while True:
        player_input = input(f"{player}, please choose where you want to place your piece: eg. '3 1' for the bottom-left, or '1 3 for the top right. ")
        loc_x = int(player_input[0]) - 1
        loc_y = int(player_input[2]) - 1
        if game_board[loc_x, loc_y] == 'X' or game_board[loc_x, loc_y] == '0':
            print("You can't put a piece there")
        else:
            break

    # put piece onto board and change player
    place_piece(player, loc_x, loc_y, game_board)

    # check if win
    winner = is_win(game_board, player)
    if winner:
        game_running = False

    # ensure player on new iteration of while loop is the other player
    new_player = change_player(player)
    player = new_player
    turns += 1
    if turns == 9:
        print('Game over, nobody won')
        game_running = False


