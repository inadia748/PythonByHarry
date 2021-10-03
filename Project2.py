# The Perfect Guess.

#We are going to write a program that generates a random number and asks the user to guess it. If the player 's guess is higher than the actual number, the program displays "Lower number please". You get the idea right.


import random 

randNumber = random.randint(1,100)

print(randNumber)

guesses = 0

userGuess = None

while(userGuess != randNumber):
    userGuess = int(input('Enter your guess'))
    guesses += 1
    if(userGuess == randNumber):
        print('You guessed it right!')
    else:
        if(userGuess > randNumber):
           print('You guessed it wrong! Enter a lower number')
        else:
            print('You guessed it wrong. Enter a higher number')

print(f"You guessed the number in {guesses} guesses")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print('You have broken the hiscore')
    with open('hiscore.txt', 'w') as f:
      f.write(str(guesses))
        
