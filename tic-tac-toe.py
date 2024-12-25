Tic-Tac-Toe is a simple yet classic two-player game that involves strategy, planning, and quick thinking.
It is played on a 3x3 grid where players take turns marking the spaces with their respective symbols, typically "X" and "O". 
The objective of the game is to be the first player to get three of their symbols in a row, either horizontally, vertically, or diagonally.
Gameplay:
The game is played on a 3x3 grid.
Players alternate turns, placing their symbol (X or O) in an empty cell.
The goal is to align three of their symbols consecutively in a row, column, or diagonal.


from IPython.display import clear_output 

def display_board(board):
    clear_output()
    print(' |   |')
    print(board[9]+'|'+board[8]+'|'+board[7])
    print(' |   |')
    print('-----------')
    print(' |   |')
    print(board[6]+'|'+board[5]+'|'+board[4])
    print(' |   |')
    print('-----------')
    print(' |   |')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' |   |')
    print('-----------')


def player_input():
    choose=''
    while not(choose == 'X' or choose == 'Y'):
        choose=input('choose value X or O:\n').upper()
    if choose == 'X':
        return ('X','O')
    else:
        return ('O','X')
    


def player_marker(board,marker,position):
    board[position]=marker


def win_check(board,mark):
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[3] == board[6] == board[9] == mark) or (board[5] == board[2] == board[8] == mark) or (board[1] == board[4] == board[7] == mark) or (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark)  

import random
def choose_first():
    if random.randint == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space(board,position):
    return board[position] == ' '

def full_board(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    pos=0
    while pos not in range(1,10) or not space(board,pos):
        pos = int(input("choose a pos in range(1-9):"))
    return pos

def replay():
    ch=input("play another game Yes or No:\n")
    return ch == 'Yes'

print('Welcome to Tic-Tac-Toe')
while True:
    board=[' ']*10
    player1,player2=player_input()
    turn=choose_first()
    print(turn+'will go first')
    print('y or n')
    play_game = input("ready to play the game? y or n:\n")
    if play_game == 'y':
        game_on= True
    else:
        game_on = False
    
    while game_on:
        if turn == 'player1':
            display_board(board)
            position=player_choice(board)
            player_marker(board,player1,position)
            
            if win_check(board,player1):
                display_board(board)
                print('WIN THE GAME')
                game_on=False
            else:
                if full_board(board):
                    display_board(board)
                    print('board is full')
                    break
                else:
                    turn = 'player2'
        else:
            display_board(board)
            position = player_choice(board)
            
            player_marker(board,player2,position)
            
            if win_check(board,player2):
                display_board(board)
                print('WIN THE GAME')
                game_on=False
            else:
                if full_board(board):
                    display_board(board)
                    print('board is full')
                    break
                else:
                    turn = 'player1'
    if not replay():
        break
            
                    
    
