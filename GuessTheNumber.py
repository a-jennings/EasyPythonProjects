from random import randint

def correct_num():
    return randint(1, 100)


def game(number):

    
    attempts = 10
    while True:
        
        if attempts == 0:
            print('You Lose!')
            play_again()
        user_input = input('Please select a number between 1 and 100: ')
        try:
            int(user_input)
        except:
            print('Enter valid number')
            continue
        if int(user_input) < 1 or int(user_input) > 100:
            print('Enter valid number')
            continue
            
        
        if int(user_input) == number:
            print(f'YOU WIN! The correct number was {user_input}!')
            (play_again())
        else:
            tloth = ''      #too low or too high
            if int(user_input) > number:
                tloth = 'Too high'
                attempts -= 1
            elif int(user_input) < number:
                tloth = 'Too low'
                attempts -= 1

            print(f'You guessed wrong! ({tloth}), you have {attempts} attempts remaining')
            continue
 

def play_again():
    user_input = input('Do you want to play again? (Y or N): ')
    user_input = user_input.upper()
    if user_input == 'Y' or user_input == 'YES':
        game(correct_num())
    else:
        exit()


game(correct_num())
