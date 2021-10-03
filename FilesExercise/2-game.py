#2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'history.txt' which is either blank or contains the previous Hi-score. You need to write a program to update Hi-score whenever game() breaks the Hi-score.


def game():
    return 693

score = game()
with open('hiscore.txt') as f:
    hiscoreStr = int(f.read())

if hiscoreStr == '':
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))

elif int(hiscoreStr) < score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))

