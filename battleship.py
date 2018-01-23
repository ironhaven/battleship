#!/usr/bin/python3
##This is a battleship game where you gotta sink that battleship!
from random import randint

board_height = 6
board_width = 6
board = []

##Creates a list of list to create a 2-D game board "gb"
def create_board():
    gb = []
    if gb == []:
      for i in range(board_height):
        row = []
        for i in range(board_width):
            row.append('O')
        gb.append(row)
      return gb
    else:
        board = []
        for i in range(board_height):
            row = []
            for i in range(board_width):
                row.append('O')
            board.append(row)
        return gb
##This will display the entire board with row and column numbers
def print_board():
##Print top row with only columns numbers
    print(' ', end='')
    row = 0
    for i in range(board_width):
        print(str(i), end=' ')
    print('')
##Print rows with row number
    for i in board:
        print(str(row)+' '.join(i))
        row += 1
##Spawn single boat on board
def spawn_boat():
    x = randint(0,board_width)
    y = randint(0,board_height)
##If the boat in not in the 'O'cean try again
    while board[x][y] != 'O':
        x = randint(0,board_width)
        y = randint(0,board_height)
    else:
        board[x][y] = 'B'
board = create_board()
print('Board Hight: '+str(len(board))+' Board Width: '+str(len(board[0])))
spawn_boat()
print_board()
