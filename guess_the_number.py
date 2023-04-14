import random 

def main():
    play_game()
    while True:
        game_reload = input('Play again? Y or N: ')
        if((game_reload == 'Y') or (game_reload == 'y')):
            play_game()
        else:
            print('Thanks to play my game!')
            break
    
""" Generate a random number """
def generate_number():

    random_number = int((random.random() * 100))
    return random_number

""" Play the game """
def play_game():
    # initial values
    score = 50
    attempts = 5

    print('-------- Guess the number --------')
    number = generate_number()
    while(attempts > 0):
        number_of_user = input('Choose a number: ')
        if(number_of_user == number):
            print(f'Congrats! You win. Your score: {score} and the number was : {number}')
        else:
            if(int(number_of_user) > number):
                print('Choose a smaller number!')
            else:
                print('Choose a larger number!')
            score-=10
        attempts -= 1

    print(f'Sorry! You lose. Your score: {score} and the number was : {number}\n')


main()

