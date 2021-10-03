#1. Write a program to find greatest of four numbers entered by the user.

num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
num3 = int(input('Enter number3: '))
num4 = int(input('Enter number4: '))


if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + ' is greatest')
else:
    print(str(f2) + ' is greatest')








#2. Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33%, in each subject to pass. Assume 3 subjects and take marks as an input from the user.

    sub1 = int(input('Enter first subject marks: '))
    sub2 = int(input('Enter second subject marks: '))
    sub3 = int(input('Enter third subject marks: '))

    if(sub1 < 33 or sub2 < 33 or sub3 < 33):
        print('You failed')
    
    if( (sub1+sub2+sub3)/3 < 40):
        print('You failed because your average is less than 40%')
    else:
        print('You passed the test')






#3. A spam comment is defined as a text containing following keywords:  "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

text = input('Enter the text')
if('Make a lot of money' in text):
    spam = True
elif('buy now' in text):
    spam = True
elif('subscribe this' in text):
    spam = True
else:
    spam = False

if(spam):
    print('This text is spam')
else:
    print('This text is not spam')


#4. Write a program to find whether a give username contains less than 10 characters.

username = input('Enter username: ')
print(len(username))
if(len(username) < 10):
    print('It is less than 10 characters')
else:
    print('It is more than 10 characters')



#5. Write a program which finds out whether a given name is present in a list.

    names = ['Jamie', 'Sarah', 'Nadia']
    name = input('Enter the name to check')

    if name in names:
        print('The name you entered is present in the list')
    else:
        print('The name you entered is not present in the list')


#6.  Write a program to calculate the grade of a student from his marks from the following scheme:
        '''
        90 - 100 -> Excellent
        80 - 90  -> A
        70 - 89  -> B
        60 - 70  -> C
        50 - 60  -> D
        0 - 40    -> F
        '''

marks = int(input('Enter your marks out of 100: '))

if marks > 90:
    grade = 'Excellent'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
else:
    grade = 'F'

print('Your grade is '+ grade)





    


