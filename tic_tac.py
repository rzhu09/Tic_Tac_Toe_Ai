import numpy as np
import random
import pygame
import sys
import math
import collections

color_black = (0,0,0)
color_white = (255,255,255)
gui_height = 500
gui_width = 500
gui_margin = 1

player = 1
player_ai = 2

row = 3
column = 3

def create_board_3_x_3():
    new_board = np.zeros((row, column))
    return new_board

def print_curr_board(curr_board):
    print(curr_board)

def row_col(move): # don't really need this tbh, numpy has function to return I think
    if move == 0:
        return 0, 0
    elif move == 1:
        return 0, 1
    elif move == 2:
        return 0, 2
    elif move == 3:
        return 1, 0
    elif move == 4:
        return 1, 1
    elif move == 5:
        return 1, 2
    elif move == 6:
        return 2, 0
    elif move == 7:
        return 2, 1
    elif move == 8:
        return 2, 2

def update_board(board,row,col, player_move):
    board[row][col] = player_move

def check_winner(board, pla):
    # horizontals
    for i in range(row):
        for j in range(column):
            if j != 1 and j != 2 and board[i][j] == pla and board[i][j+1] == pla and board[i][j+2] == pla:
                return True

    # verticals
    for i in range(row):
        for j in range(column):
            if i != 1 and i != 2 and board[i][j] == pla and board[i+1][j] == pla and board[i+2][j] == pla:
                return True

    # down diagonal (upper left  -> bottom right_)
    for i in range(row-2):
        for j in range(column-2):
            if board[i][j] == pla and board[i+1][j+1] == pla and board[i+2][j+2] == pla:
                return True

    # up diagonal (bottom left -> upper right
    for i in range(row - 2):
        for j in range(column -2):
            if board[i][j+2] == pla and board[i+1][j+1] == pla and board[i+2][j] == pla:
                return True

def ai_best_move(board, play):

    #first we need the list of avaliable moves
    avaliable_locations = []
    for i in range(9):
        tr, tc = row_col(i)
        if board[tr][tc] == 0:
            avaliable_locations.append(i)

    initial_score = 0
    move_to_pick = random.choice(avaliable_locations) #temp place holder for now

    for i in avaliable_locations:
        tr, tc = row_col(i)
        temp_board = board.copy()
        temp_board[tr][tc] = play
        score = rate_move(temp_board, play)
        if score > initial_score:
            initial_score = score
            move_to_pick = i

    return move_to_pick

def rate_move(board, play):
    score = 0

    if check_winner(board, play):
        return 10000

    # horizontals
    for i in range(row):
        for j in range(column):
            if j != 1 and j != 2 and board[i][j] == play and board[i][j+1] == play or j != 1 and j != 2 and board[i][j+1] == play and board[i][j+2] == play:
                score += 20
            if j != 1 and j != 2 and board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == play or board[i][j] == play and j != 1 and j != 2 and board[i][j + 1] == player and board[i][j + 2] == player:
                score += 25


    # verticals
    for i in range(row):
        for j in range(column):
            if i != 1 and i != 2 and board[i][j] == play and board[i+1][j] == play or i != 1 and i != 2 and board[i+1][j] == play and board[i+2][j] == play:
                score += 20
            if i != 1 and i != 2 and board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == play or i != 1 and i != 2 and board[i][j] == play and board[i + 1][j] == player and board[i + 2][j] == player:
                score += 25


    # down diagonal (upper left  -> bottom right_)
    for i in range(row-2):
        for j in range(column-2):
            if board[i][j] == play and board[i+1][j+1] == play or board[i+1][j+1] == play and board[i+2][j+2] == play:
                score += 20
            if board[i][j] == play and board[i + 1][j + 1] == player and player and board[i + 2][j + 2] == player or board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == play:
                score += 25

    # up diagonal (bottom left -> upper right
    for i in range(row - 2):
        for j in range(column -2):
            if board[i][j+2] == play and board[i+1][j+1] == play or board[i+1][j+1] == play and board[i+2][j] == play:
                score += 20
            if board[i][j + 2] == player and board[i + 1][j + 1] == player and board[i + 2][j] == play or board[i][j + 2] == play and board[i + 1][j + 1] == player and board[i + 2][j] == player:
                score += 25

    return score


#def draw_gui_board(curr_board):

 #   pygame.draw.rect(gui, color_black, (10, 156, 480, 15), 0)
 #   pygame.draw.rect(gui, color_black, (10, 322, 480, 15), 0)
 #   pygame.draw.rect(gui, color_black, (156, 10, 15, 480), 0)
 #   pygame.draw.rect(gui, color_black, (322, 10, 15, 480), 0)
 #   pygame.display.update()

# pygame.init()
# size = (gui_height, gui_width)
# gui = pygame.display.set_mode(size)
# gui.fill(color_white)


working_board = create_board_3_x_3()

print("These are the moves to pick from")
moves = np.arange(9).reshape((3,3))
print(moves)

print("This is the current game board")
print_curr_board(working_board)

gg = False

who_starts = random.randint(player, player_ai)
moves = 0
print("Player {who} starts first".format(who = who_starts))

while not gg:
    if who_starts == player:
        move = input("Enter your move : ")
        temp_row, temp_col = row_col(int(move))
        if working_board[temp_row][temp_col] == 0:
            update_board(working_board, temp_row, temp_col, player)
            moves += 1
            print_curr_board(working_board)
            #check to see if there is a winner if so, end the game and announce it
            if check_winner(working_board, player):
                print("Player {player} won !".format(player = player))
                gg = True
            elif moves >= 9:
                print("TIE !")
                gg = True
            who_starts += 1
            who_starts = who_starts % 2

    else: # player_ai turn
        print("Ai's turn:")
        move = ai_best_move(working_board, player_ai)
        temp_row, temp_col = row_col(int(move))
        if working_board[temp_row][temp_col] == 0:
            update_board(working_board, temp_row, temp_col, player_ai)
            moves += 1
            print_curr_board(working_board)
            #check to see if there is a winner if so, end the game and announce it
            if check_winner(working_board, player_ai):
                print("Player {player} won !".format(player = player_ai))
                gg = True

            elif moves >= 9:
                print("TIE !")
            who_starts += 1
            who_starts = who_starts % 2

        # Improving the Ai
        # need to create a array/list of valid next moves
        # stimulate those moves with a copy of the board
        # choose the best move to make based on a given score for each move
        # execute that move
        # implement better algorithms





