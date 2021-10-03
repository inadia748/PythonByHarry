import random

def game():
    pass


'''
randNo = random.randint(1,2)
print(randHo)
'''

# Snake Water Gun or Rock Paper Scissor
def gameWin(comp, you):
    # If two values are equal
    if comp == you:
        return None

    #check for all possibilites when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    #check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    
    #check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


            
comp = ('Computer Turn: Snake(1) water(2) or gun(3)?')
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input('Your Turn: Snake(s) water(w) or gun(g)?')

print(f"Computer chose {comp}")
print(f"you choose {you}")

a = gameWin(comp, you)

if a == None:
    print('The game is a tie')
elif a:
    print('You win!')
else:
    print('You lose!')