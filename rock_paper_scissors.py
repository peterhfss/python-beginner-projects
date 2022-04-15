import random

def game():

    print("------- Rock, Paper, Scissors -------\n")

    user = input('         What`s your choice?'
    "\n'r' for rock | 'p' for papper | 's' for scissors : \n")

    
    computer= random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return 'You won!'
        
    return 'You lost!' 

print(game())

# function return true if user wins
def is_win(player, opponent):
        # r > s | s > p | p > r
            if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
                return True

while True:
    game_reload = input("Play again? | 'y' for yes or  'n' for no : ")
    if(game_reload == 'y'):
        game()
    else:
        break 