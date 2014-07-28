#Elaine Mao
#ekm2133
#AI Project 3

#Import necessary modules
from copy import deepcopy
import time

#Global Variables

#Initialize gameboard variable to the starting state
gameboard = [["x", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "o"]]

#Initializes computer and opponent
computer = ""
opponent = ""

#Initializes turn
turn = ""

#Initializes time limit variable
time_limit = 0

#Game-Playing Functions

#Asks the player for a time limit for the game
def set_time_limit ():
    global time_limit
    answer = input ("What is the time limit for this round? Please give your answer in seconds. \n")
    time_limit = int (answer)

#Asks the player if the computer will be x or o
def players ():
    answer = input ("Should the computer be x or o?\n")
    global computer
    global opponent
    global turn
    if answer == "x":
        computer = "x"
        opponent = "o"
        turn = computer
    else:
        computer = "o"
        opponent = "x"
        turn = opponent

#Displays the current state of gameboard; is called after each move
def display ():
    for i in range (0,8):
        print (gameboard [i])

#Get value of a tile given the position
def get_value (x, y, board):
    return (board [x - 1] [y - 1])

#Gets (only the first) index where a particular value is found (will only be used to get 'x' and 'o' indexes, so this is fine)
def get_index (value, board):
    for i in range (1,9):
        for j in range (1,9):
            if get_value (i, j, board) == value:
                return (i,j)

#Main isolation game function
def isolation ():
    set_time_limit ()               #Asks the player for a time limit for the computer's turn
    players ()                      #Asks the player whether the computer will be 'x' or 'o'
    while not game_over (gameboard):                    #While the gameboard does not satisfy the game_over conditions
        if turn == computer:                            #If it is the computer's turn
            print ("\nThe computer moves to:")
            computer_move = best_move (computer)            #Call best_move to find the computer's best move
            print (computer_move)
            move_to (computer, computer_move, gameboard)    #Move computer player to that location
            display ()
            print ("\n")
        else:                                                                       #If it is the opponent's turn
            x = 0                                                                   #Initialize x and y 
            y = 0
            while (x, y) not in legal_moves (opponent, gameboard):                  #As long as (x,y) is not in the opponent's list of legal moves
                x = input ("Enter the row the opponent will move to: \n")           #Continue asking for the desired row and column to move to
                y = input ("Enter the column the opponent will move to: \n")
                if x not in "12345678" or y not in "12345678":                      #If the user's input is not a number within the range 1-8, set x and y to 0 ( (0,0) will not be in the list of legal moves)
                    x = 0
                    y = 0
                else:
                    x = int (x)                                                     #Convert the user's input to an integer
                    y = int (y)
                if (x, y) not in legal_moves (opponent, gameboard):                 #If the move is illegal, gives the user an error message
                    print ("That is not a valid move. Please enter another.")
            print ("\nYou have moved to:")
            print ((x, y))
            move_to (opponent, (x, y), gameboard)           #Move opponent to specified location
            display ()

#Determines if a specific tile is empty
def is_empty (x, y, board):
    if get_value (x, y, board) == "-":
        return True
    else:
        return False

#Moves a player to a location on a board
def move_to (self, move, board):
    global gameboard
    global turn
    if self == computer:                                    #If move_to is called for the computer player
        computer_position = get_index (computer, board)     #Find the computer player's current position
        (board [computer_position [0] - 1] [computer_position [1] - 1]) = "*"       #Set that position to "*"
        (board [move [0] - 1] [move [1] - 1]) = computer                            #Move computer player to new position, change turn
        turn = opponent
    else:                                                   #If move_to is called for the opponent
        opponent_position = get_index (opponent, board)     #Find the opponent's current position
        (board [opponent_position [0] - 1] [opponent_position [1] - 1]) = "*"       #Set that position to "*"
        (board [move [0] - 1] [move [1] - 1]) = opponent                            #Move opponent to new position, change turn
        turn = computer

#Determines if a given move is legal
def is_legal (self, x, y, board):
    position = get_index (self, board)      #Gets position of player
    if not is_empty (x,y, board):           #Checks to see if goal tile is empty   
        return False
    else:                                   #Otherwise, checks to see if the move is legal based on remaining criteria specified in clear_path
        return clear_path (position, x, y, board)                  

#Accessory function for determining if diagonal moves are legal
def clear_path (self, x, y, board):
    start_row = (self [0])
    start_column = (self [1])
    goal_row = x
    goal_column = y
    if abs (start_row - goal_row) <= 1 and abs (start_column - goal_column) <= 1:       #Base case
        return True
    elif start_row == goal_row and start_column < goal_column:                          #Checks moves horizontal right
        temp = (start_row, start_column + 1)
    elif start_row == goal_row and start_column > goal_column:                          #Checks moves horizontal left
        temp = (start_row, start_column - 1)
    elif start_row > goal_row and start_column == goal_column:                          #Checks moves vertical up
        temp = (start_row - 1, start_column)
    elif start_row < goal_row and start_column == goal_column:                          #Checks moves vertical down
        temp = (start_row + 1, start_column)
    elif (abs(x - (self [0]))) == (abs(y - (self [1]))) and start_row > goal_row and start_column > goal_column:        #Checks moves diagonal up and left
        temp = (start_row - 1, start_column - 1)
    elif (abs(x - (self [0]))) == (abs(y - (self [1]))) and start_row > goal_row and start_column < goal_column:        #Checks moves diagonal up and right
        temp = (start_row - 1, start_column + 1)
    elif (abs(x - (self [0]))) == (abs(y - (self [1]))) and start_row < goal_row and start_column > goal_column:        #Checks moves diagonal down and left
        temp = (start_row + 1, start_column - 1)
    elif (abs(x - (self [0]))) == (abs(y - (self [1]))) and start_row < goal_row and start_column < goal_column:        #Checks moves diagonal down and right
        temp = (start_row + 1, start_column + 1)
    else:
        return False
    if not is_empty (temp [0], temp[1], board):             #Checks to see if the next tile is empty; if not, returns false
        return False
    else:                                                   #Otherwise, check the next tile
        return clear_path (temp, x, y, board)

#Creates a list of legal moves given a position and a board
def legal_moves (self, board):                      
    moves = []
    for i in range (1,9):
        for j in range (1,9):
            temp = (i,j)
            if is_legal (self, i, j, board):                #If a position (i,j) is legal, append it to moves
                moves.append (temp)
    return moves

#Determines if the game is over
def game_over (gameboard):
    computer_moves = legal_moves (computer, gameboard)              #List of computer's move options
    opponent_moves = legal_moves (opponent, gameboard)              #List of opponent's move options
    if len (computer_moves) == 0 and len (opponent_moves) != 0:     #If the computer has no more moves, but the opponent does, the opponent wins
        print ("The opponent has won.")
        return opponent
    elif len (computer_moves) != 0 and len (opponent_moves) == 0:   #If the opponent has no more moves, but the computer does, the computer wins
        print ("The computer has won.")
        return computer
    elif len (computer_moves) == 0 and len (opponent_moves) ==  0:  #If both players are out of moves, it is a tie
        print ("The game is a tie.")
        return computer, opponent
    else:                                                           #Otherwise, the game is not over yet
        return False 

#Accessory function for alpha_beta to switch turns without affecting the global turn variable
def next_turn (current_turn):
    if current_turn == computer:
       return opponent
    else:
       return computer                            

#Accessory function for alpha_beta to create new boards according to specified moves without modifying the global gameboard    
def new_state (self, move, board):
    new_board = deepcopy (board)
    move_to (self, move, new_board)
    return new_board

#Determines what the best move will be for a given position
def best_move (position):
    return (alpha_beta (get_index (computer, gameboard), gameboard, turn, 3))   #Calls alpha_beta with depth 3

#Alpha-beta search algorithm 
def alpha_beta (position, board, current_turn, depth):  
    start_time = deepcopy (time.time ())                                        #Records the time the function was first called
    possible_moves = legal_moves (current_turn, board)                          #List of legal moves for the given position

    def max_value (position, board, current_turn, alpha, beta, depth):
        if depth == 0 or time.time() - start_time >= time_limit - 2:            #Checks to see if the depth limit has been reached or if time is almost out
            return evaluate (position, board)                                   
        v = float ("-inf")
        for a in legal_moves (current_turn, board):
            v = max (v, min_value (a, new_state (current_turn, a, board), next_turn (current_turn), alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max (alpha, v)
        return v

    def min_value (position, board, current_turn, alpha, beta, depth):
        if depth == 0 or time.time() - start_time >= time_limit - 2:            #Checks to see if the depth limit has been reached or if time is almost out
            return evaluate (position, board)
        v = float ("inf")
        for a in legal_moves (current_turn, board):
            v = min (v, max_value (a, new_state (current_turn, a, board), next_turn (current_turn), alpha, beta, depth - 1))
            if v <= alpha:
                return v
            beta = min (beta, v)
        return v
    return max (possible_moves, key = lambda a: min_value (a, new_state (current_turn, a, board), next_turn (turn), float ("-inf"), float ("inf"), depth))

#Evaluation function used by alpha-beta search to determine the "goodness" of a particular state
def evaluate (self, board):                                                     
    previous_computer_moves = legal_moves (computer, gameboard)         #Gets the list of moves for the computer at its current global position
    previous_opponent_moves = legal_moves (opponent, gameboard)         #Gets the list of moves for the opponent at its current global position
    computer_moves = legal_moves (computer, board)                      #Gets the list of moves for the computer at its test position in alpha-beta search
    opponent_moves = legal_moves (opponent, board)                      #Gets the list of moves for the opponent at its test position in alpha-beta search
    if len (computer_moves) == 0 and len (opponent_moves) != 0:         #If this move results in the opponent winning the game, return utility -infinity
        return float ('-inf')
    elif len (computer_moves) != 0 and len (opponent_moves) == 0:       #If this move results in the computer winning the game, return utility infinity
        return float ('inf')
    elif len (computer_moves) == 0 and len (opponent_moves) == 0:       #If this move results in a draw, return utility -10
        return -10
    elif len (computer_moves) >= len (opponent_moves):                  #More explanation for this part is available in the README
        return (len (computer_moves) / len (opponent_moves))**2 + len (previous_opponent_moves) - len(opponent_moves)
    elif len (computer_moves) < len (opponent_moves):
        return - (len (opponent_moves)/ len(computer_moves))**2 + len (previous_opponent_moves) - len (opponent_moves)
