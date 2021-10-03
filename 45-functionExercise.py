#1. Write a program using function to find the greatest of three numbers.

def maximum(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3

m = maximum(3, 989, 234)
print('The value of maximum is '+ str(m))






#2. Write a program using function to convert celcius to fahrenheit

def farh(cel):
    return (cel * (9/5)) + 35

c = 45
f = farh(c)
print('Fahrenheit Temperature is '+ str(f))






#3. How do you prevent a python print() function to print a new line in the end.
print('Hello')
print('How')
print('are')
print('you? ')

print('Hello, ', end=" ")
print('How', end=" ")
print('are', end=" ")
print('you? ', end=" ")
print('\n')




#4.Write a recursive to print first n natural numbers.
def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

num = 3

if num < 0:
    print('Enter positive number')
else:
    print('The sum is, ', recur_sum(num))



#5. Write a python program to convert inches to cm.

def cm(v):
    return (v * 2.54)

v = 45
q = cm(v)
print('Inches to centimer is '+ str(q))






#6. print the pattersn

    # m = 6
    # for i in range(m):
    #     print("*" * (m-i))




#7. Write a function to remove a given word from a string and strip  it at the same time.

'''
this = '    Hello, I am Nadia     '
print(this)
print(this.strip())

'''

def remove_and_split(string, word):
    newStr = string.replace(word, '')
    return newStr.strip()


this = '   Hello, Nadia is good  '
q = remove_and_split(this, 'Nadia')
print(q)





#8. Write a function to print multiplication table of a give number.

def mult(number):
    for i in range(1, 11):
        print(f"{number} X {i} = {number*i}")

mult(9)

