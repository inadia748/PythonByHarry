for i in range(10):
    print(i)

for i in range(5):
    print(i)
else:
    print('This is inside else of for')


for i in range(10):
    print(i)
    if i == 5:
        break





for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('This is inside else of for')

#here, 'This is inside else of for' will not be printed because the for loop is terminated using the'break'. The for loop is not exhausted.