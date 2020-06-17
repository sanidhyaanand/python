# program to guess a random number

# import random
import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
       break 

if guess == secretNumber:
    print(f'Nice! You guessed the number in {guessesTaken + 1} guesses!')
else:
    print(f'Better luck next time, number I was thinking of was {secretNumber} :(')