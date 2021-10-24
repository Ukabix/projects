# globals
import random

# Step 1: Write a function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.

def display_board(board):
    print("\n"*50)
    horizontal = ('   |   |   ')
    vertical = ('---+---+---')
    line789 = (' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    line456 = (' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    line123 = (' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print(horizontal)
    print(line789)
    print(horizontal)
    print(vertical)
    print(horizontal)
    print(line456)
    print(horizontal)
    print(vertical)
    print(horizontal)
    print(line123)
    print(horizontal)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.

def player_input_marker():
    marker1 = ''
    marker2 = ''
    while marker1 not in ['X','O']:
        marker1 = input('Player 1, please select X or O.')
        if marker1 not in ['X','O']:
            print("Wrong selection! Please choose X or O.")
        elif marker1 == 'X':
            print('Player 1, you have chosen X.')
        else:
            print('Player 1, you have chosen O.')    
    if marker1 == 'X':
        marker2 = 'O'
        print("Player 2, you are O.")
    else:
        marker2 = 'X'
        print("Player 2, you are X.")
    return (marker1, marker2)

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
# and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

# Step 4: Write a function that takes in a board and a mark (X or O) 
# and then checks to see if that mark has won.

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

# Step 5: Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.


def choose_first():
    if random.randint(1,2) == 1:
        return "Player 1"
    else:
        return "Player 2"

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. 
# True if full, False otherwise.

def full_board_check(board):
    if ' ' not in board:
        return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position. 
# If it is, then return the position for later use.
 
def position_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1,2,3,4,5,6,7,8,9) '))
        
    return position

# Step 9: Write a function that asks the player if they want to play again
# and returns a boolean True if they do want to play again.

def replay():
    choice = "wrong"
    while choice not in ['Y','N']:
        choice = input("Play Again? Y or N: ")
        if choice not in ['Y','N']:
            print("Sorry, invalid choice, choose Y or N")
    if choice == "Y":
        return True
    else:
        return False
    return int(choice)

# Step 10: Here comes the hard part! 
# Use while loops and the functions you've made to run the game!


while True:
    # Set the game up here
    print("\n"*50)
    print("Welcome to TicTacToe.")
    gameBoard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker1, marker2 = player_input_marker()
    turn = choose_first()
    print(turn + ' will start.')

    game_start = input("Are you ready? Y/N")
    if game_start == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 1:
        # Player 1 Turn
            display_board(gameBoard)
            print("Player 1 turn.")
            position = position_choice(gameBoard)
            place_marker(gameBoard, marker1, position)
        if win_check(gameBoard,marker1) == True:
            display_board(gameBoard)
            print("Congratulations! Player 1 wins!")
            game_on = False
        else:
            if full_board_check(gameBoard) == True:
                print("This game is a draw.")
                game_on = False
                break
            else:
                turn = 2
        if turn == 2:
        # Player 2 Turn
            display_board(gameBoard)
            print("Player 2 turn.")
            position = position_choice(gameBoard)
            place_marker(gameBoard, marker2, position)
        if win_check(gameBoard,marker2) == True:
            display_board(gameBoard)
            print("Congratulations! Player 2 wins!")
            game_on = False
        else:
            if full_board_check(gameBoard) == True:
                print("This game is a draw.")
                game_on = False
                break
            else:
                turn = 1
    if not replay():
        break