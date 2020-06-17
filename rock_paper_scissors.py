# program to guess a random number

# import libraries
import random, sys, os

# game variables
wins = 0
losses = 0
ties = 0

# legend
print('r is for rock, p is for paper, s is for scissors, q is for quit')

# main game loop
while True:
    print('')
    print(f'WINS {wins}')
    print(f'LOSSES {losses}')
    print(f'TIES {ties}')

    print('type "r" or "p" or "s" or "q"')
    userChoice = input()
    if userChoice == 'q':
        quit()


    # player input options
    elif userChoice == 'r':
        print('ROCK VERSUS...')
    elif userChoice == 'p':
        print('PAPER VERSUS...')
    elif userChoice == 's':
        print('SCISSORS VERSUS...')
    
    # computer choice
    compChoice = random.randint(1, 3)

    if compChoice == 1:
        print('ROCK!')
    elif compChoice == 2:
        print('PAPER!')
    elif compChoice == 3:
        print('SCISSORS')

    # war time
    if userChoice == 'r' and compChoice == 1:
        print('TIE!')
        ties = ties + 1
    elif userChoice == 'p' and compChoice == 2:
        print('TIE!')
        ties = ties + 1
    elif userChoice == 's' and compChoice == 3:
        print('TIE!')
        ties = ties + 1
    
    elif userChoice == 'r' and compChoice == 3:
        print('YOU WIN!')
        wins = wins + 1
    elif userChoice == 'p' and compChoice == 1:
        print('YOU WIN!')
        wins = wins + 1
    elif userChoice == 's' and compChoice == 2:
        print('YOU WIN!')
        wins = wins + 1
    
    elif userChoice == 'r' and compChoice == 2:
        print('YOU LOSE')
        losses = losses + 1
    elif userChoice == 'p' and compChoice == 3:
        print('YOU LOSE')
        losses = losses + 1
    elif userChoice == 's' and compChoice == 1:
        print('YOU LOSE')
        losses = losses + 1

    os.system('clear')