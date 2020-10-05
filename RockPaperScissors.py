##Github test

from random import randint

def cpu_logic():
    cpu_choice = randint(1,3) #CPU random picks int and assigns to R,P,S

    if cpu_choice == 1:
        return 'Rock'
    elif cpu_choice == 2:
        return 'Paper'
    else:
        return 'Scissors'


def user_logic():   
    
    while True:
        user_input = input("Choose Rock, Paper or Scissors (R,P,S):")
        user_input = user_input.upper()

        if user_input == 'ROCK':        #check for word or char
            user_input = 'R'
        if user_input == 'PAPER':
            user_input = 'P'
        if user_input == 'SCISSORS':
            user_input = 'S'



        if user_input == 'P':
            return 'P'
        elif user_input == 'R':
            return 'R'
        elif user_input == 'S':
            return 'S'
        else:
            print('Enter valid input')
            continue
    

def game_logic(cpu, user):

    #game logic R > S, R < P,   S > P, S < R,   P > R, P < S
    if cpu == 'Rock' and user == 'S':
        print('CPU wins! (CPU picks Rock)')
    elif cpu == 'Rock' and user == 'P':
        print('YOU win! (CPU picks Rock)')
    elif cpu == 'Scissors' and user == 'P':
        print('CPU wins! (CPU picks Scissors)')
    elif cpu == 'Scissors' and user == 'R':
        print('YOU win! (CPU picks Scissors)')
    elif cpu == 'Paper' and user == 'R':
        print('CPU wins! (CPU picks Paper)')
    elif cpu == 'Paper' and user == 'S':
        print('YOU win! (CPU picks Paper)')
    elif cpu and user == 'P' or 'R' or 'S':
        print(f'Draw! (CPU picks {cpu})')
    else:
        print('Logic Error!')

    #replay game on 'Y'
    play_again = input('Play again? (Y or N): ')
    play_again = play_again.upper()
    if play_again == 'Y':
        game_logic(cpu_logic(),user_logic())
    else:
        exit


game_logic(cpu_logic(),user_logic())


