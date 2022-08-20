import random


def display_board(board):
    #Displays tic tac toe board with current user inputs

    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('\n\n')

def player_input():
    #Assigns each player either X or O as their marker for the entirety of the game

    p1marker = ''
    p2marker = ''
    while p1marker != 'X' and p1marker != 'O':
        p1marker = input('Player 1 - Choose your marker: X or O\n').capitalize()
    if p1marker == 'X':
        p2marker = 'O'
    else:
        p2marker= 'X'
    return (p1marker,p2marker)

def place_marker(board, marker, position):
    #Places users marker in specified location on tic tac toe board

    board[int(position)-1] = marker

def win_check(board, mark):
    #Takes in a board and a mark and checks to see if a user with that mark has won

    if board[0] == mark and board [1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board [4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board [7] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board [4] == mark and board[8] == mark:
        return True
    elif board[2] == mark and board [4] == mark and board[6] == mark:
        return True
    elif board[0] == mark and board [3] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board [4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board [5] == mark and board[8] == mark:
        return True
    else:
        return False

def choose_first():
    #Chooses which user goes first

    first = random.randint(1,2)
    if first == 1:
        return 'X'
    else:
        return 'O'

def space_check(board, position):
    #Checks if a certain position on the board is free

    return board[position] == ' '

def full_board_check(board):
    #Checks if there are any spots on board that is empty

    for pos in board:
        if pos == ' ':
            return False
    return True

def player_choice(board):
    #Takes players next position between 1-9 and checks if there is space

    userchoice = 0
    end = False
    while end == False:
        userchoice = input('Choose your next position: (1-9)\n')
        if userchoice.isdigit() == False:
            print('Please enter a number.')
        elif int(userchoice) not in range(1,10):
            print('Choose a number between 1-9')
        elif space_check(board, int(userchoice)-1) == False:
            print(f'Position {int(userchoice)} is already taken. Please choose another position.')
        else:
            end = True
            return int(userchoice)

def replay():
    #Returns true if user wants to play the game again and false if not

    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to play again? (Y or N):\n').upper()
        # if answer!= 'Y' or answer!= 'N':
        #     print('Please enter either Y or N')
    if answer == 'Y':
        return True
    else:
        return False
        


print('Welcome to tic-tac-toe!')

playagain = True
while playagain == True:
    gameboard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1 = ''
    player2 = ''
    winner = False
    fullboard = False
    
    print('\n'*50)
    player1, player2 = player_input()
    print(f'Player 1: You are {player1}!')
    print(f'Player 2: You are {player2}!\n')
    currentmarker = choose_first()
    if player1 == currentmarker:
        print("Player 1 goes first!")
    else:
        print("Player 2 goes first!")
    print('\n')
    display_board(gameboard)
    print('\n')
    while winner == False:

        userchoice = player_choice(gameboard)
        print('\n')
        place_marker(gameboard, currentmarker, userchoice)
        display_board(gameboard)
        if currentmarker == 'X':
            currentmarker = 'O'
        else:
            currentmarker = 'X'
        fullboard = full_board_check(gameboard)
        winner = win_check(gameboard, 'X')
        if winner == False:
            winner = win_check(gameboard, 'O')
        


    if win_check(gameboard, 'X'):
        if player1 == 'X':
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif win_check(gameboard, 'O'):
        if player1 == 'O':
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    else:
        print("It's a tie!")
    playagain = replay()

print('Thanks for playing!')
    


