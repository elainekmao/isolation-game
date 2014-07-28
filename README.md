isolation-game
==============

Isolation game with alpha-beta search (Artificial Intelligence, Spring 2013)

I implemented this project in Python 3.1 using the Python GUI. All of the code is in a single file, "ekm2133.py." To run the code, just select "Run Module." Once the code has been loaded, type the following to start the game:

>>> isolation ()

This will ask a series of questions to determine the time limit for each game, as well as the turn order (which player gets to be x and which player gets to be o). Each turn, the function will ask for the opponent to input their desired move, and it wlil then check if the move is legal. 

The evaluation function I chose first checks to see if the move will result in a winning state for either player or a draw. If it results in the opponent winning, the evaluation function assigns it a utility of -infinity. If it results in the computer winning, the evaluation function assigns it a utility of infinity. If the move results in a draw, the evaluation function assigns it a utility of -3, so that best_move will only choose a move that results in a draw if all other options are terrible.

Otherwise, if the move results in the computer having more move options than the opponent, the function returns (# moves the computer has)/(# moves the opponent has) + (# moves the opponent had before - # moves the opponent will have after this move). The function therefore returns the highest utility value for a move that restricts the opponent's moves and keeps the computer's moves open. I originally had a subtraction function instead of division, but this often caused the computer to pass up opportunities to restrict the opponent's movement simply to open up more move opportunities for itself. I changed it to division because this takes into account the fact that as (#moves the opponent has) grows very small in proportion to (#moves the computer has), the move is actually better for the computer. Also, if a move greatly restricts the move options of the opponent from what they were before, it is a better move. 

If the computer has fewer move options than the opponent, the function returns - (# moves the opponent has)/(# moves the computer has) - (# moves the opponent had before + # moves the opponent has after this move). The logic for this is similar. If a move causes the computer to have greatly proportionally fewer moves than the opponent, it is a bad move. 

This evaluation function allows for very quick execution since it just takes into account the move lists for the computer and the opponent at each state that it evaluates as well as the original state. I went through several versions of this evaluation function and I tested it each time to see if I could find a better-looking move than the one the computer chose, and then I modified the evaluation function accordingly. 

The "ekm2133.py" file first imports the necessary modules to run the game. The game uses "deepcopy" many times to create copies of the gameboard for alpha-beta search so as to avoid making changes to the gameboard itself until the best move is found. Then several global variables are initialized. The "turn" variable keeps track of whether it is time for 'x' or 'o' to go. 

is_legal and clear_path are functions used by the legal_moves function, which takes a position and a gameboard and returns a list of legal moves. 

game_over checks to see if either or both players have run out of moves, in which case the game is over, and the function returns the winner. In the case of a tie, both players have "won." next_turn and new_state are only used by the alpha_beta function. 

I based my alpha-beta search function on the one from the book, and it calls the evaluation function I described earlier. The max_value and min_value functions include checks to see if the depth limit has been reached, or if the function has nearly run out of time. I chose to leave 2 seconds leeway just to be safe. 
