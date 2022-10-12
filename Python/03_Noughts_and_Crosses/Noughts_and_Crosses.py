#________________________PRELIMENARIES____________________________
# This Python program was written by Odd Harald Sandtveit in 2022.

import datetime


#__________________________FUNCTIONS______________________________


def welcome_message(game_version):
    welcome=''
    hour=datetime.datetime.now().hour
    if hour>=18:
        welcome='Good evening!'
    elif hour>=12:
        welcome='Good afternoon!'
    elif hour>=6:
        welcome='Good morning!'
    elif hour>=0:
        welcome='Good night!'
    
    print(welcome)
    print('')
    print(f'Welcome to Noughts and Crosses by Odd Harald Sandtveit, version {game_version}.')
    print(('I realise, naturally, that Noughts and Crosses is not exactly a novel idea for a game. '
          'The game, often referred to as Tic-Tac-Toe by Americans, dates back to ancient Egypt. '
          'An early implementation of the game was made in 1950 in Canada by Josef Kates in order to '
          'showcase the capabilities of the newly developed additron tube. '
          'Another early implementation was made in 1952 for the Cambridge University EDSAC. '
          'Many times, when Noughts and Crosses has been programmed, it has been done specifically as a proof-of-concept. '
          'In a sense, a more advanced version of the classic "Hello, World!" statement. '
          'This is exactly the spirit in which this version has also been developed'))
    print('')
    print(('The game is played by two human players, One playing as "X", and one playing as "O". '
          '"X" always goes first, and the players then alternate turns. '
          'The objective, for both players, is to get three of their own symbols in a row. '
          'The first player to do this, wins the game. If neither player manages this, the game is a draw.'))
    print('')
    print('The game is played on a board that looks like this:')
    print('')
    print(' 1 | 2 | 3 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 7 | 8 | 9 ')
    print('')
    print('Please alternate taking turns. '
          'Take your turn by inputting the slot-number you wish to cross/circle, and then pressing the "Enter" button')
    print('Good luck!')

def quit_or_start_game():
    print(('Do you want to start the game, or do you want to terminate the program? '
    'Enter "t" to terminate. Enter anything else to start.'))
    return input()

def show_board(board_input):
    print('')
    print('')
    print(f' {board_input[1]} | {board_input[2]} | {board_input[3]} ')
    print('---+---+---')
    print(f' {board_input[4]} | {board_input[5]} | {board_input[6]} ')
    print('---+---+---')
    print(f' {board_input[7]} | {board_input[8]} | {board_input[9]} ')

def take_input(game_board,turn_number):
    while True:
        if turn_number%2==1:
            
            print('It is the turn of "X". Please select a square to fill.')
            selected_square=input()
            if selected_square.isdigit():
                selected_square=int(selected_square)
                if selected_square<10 and selected_square>0:
                    if game_board[selected_square]==' ':
                        game_board[selected_square]='X'
                        break
            print('Invalid input.Try again.')
    
        if turn_number%2==0:
            
            print('It is the turn of "O". Please select a square to fill.')
            selected_square=input()
            if selected_square.isdigit():
                selected_square=int(selected_square)
                if selected_square<10 and selected_square>0:
                    if game_board[selected_square]==' ':
                        game_board[selected_square]='O'
                        break
            print('Invalid input.Try again.')
            
    return game_board

def win_check(game_board,win_tuplets):
    for a in win_tuplets:
        if game_board[a[0]]=='X' and game_board[a[1]]=='X' and game_board[a[2]]=='X':
            return 1
    for b in win_tuplets:
        if game_board[b[0]]=='O' and game_board[b[1]]=='O' and game_board[b[2]]=='O':
            return 2
    if ' ' not in game_board:
        return 3
    return 0
    
def ask_play_again():
    print(('Do you want to restart the game, or do you want to terminate the program '
           'and end the session? '
    'Enter "t" to terminate. Enter anything else to restart.'))
    return input()
    
    

    
#____________________________LOGIC________________________________

def n_and_c():
    game_version=1.0    #   <------UPDATE FOR NEW VERSIONS-------
    win_tuplets=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    game_on=True
    welcome_message(game_version)
    if quit_or_start_game()=='t':
        game_on=False
    
    
        
    while game_on==True:
        game_board=['Placeholder',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        turn_number=0
        
        while True:
            turn_number+=1
            show_board(game_board)
            game_board=take_input(game_board,turn_number) #The function also sets the new game board.
            win_check_=win_check(game_board,win_tuplets)  #returns 0 for no win, 1 for x, 2 for o and 3 for draw.
            if win_check_==1:
                print('Congratulations, player "X", you have won the game!')
                break
            if win_check_==2:
                print('Congratulations, player "O", you have won the game!')
                break
            if win_check_==3:
                print('Neither player has won the game. The game is a draw.')
                break
            
        if ask_play_again() == 't':
            break
          
    print('')
    print('Noughts and Crosses has been terminated.')

#____________________________Execution________________________________

n_and_c()