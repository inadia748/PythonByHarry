#1. Write a program to print multiplication table of a given number using for loop.

num = int(input('Enter the number: '))

for i in range(1,11):
    print(str(i) + '*' + str(num) + ' = ' + str(i*num))
    #or
    #print(f"{num} X {i} = {num * i}")



#2. Write a program to greet all person names stored in a list l1 and which starts with S. l1 = ['Harry', 'sohan', 'Sarah', 'Rahul']

l1 = ['Harry', 'Sohan', 'Sarah', 'Rahul']

for name in l1:
    if name.startswith('S'):
        print('Hello' + name)


#3. Attempt problem1 using while loop

        i = 1

        while(i <= 10):
            print(f"{num} * {i} = {num * i}")
            i = i + 1


#4. Write a program to check whether a number is prime or not

num1 = int(input('Enter the number: '))
prime = True
for i in range(2, num1):
    if(num1%i == 0):
        prime = False
        break
        
if prime:
    print('This number is prime')
else:
    print('The number is not prime')



#5. Write a program to find the sum of first n natural numbers using while loop.

    sum = 0
    num2 = int(input('Enter the number: '))
    for i in range(1, num2 + 1):
        sum+=i
    print('Sum of first', num2, 'terms is ', sum)

    #or
    # num2 = int(input('Enter the number: '))
        #sum = 0, i = 1
        #while (i <= num2):
            #sum+=1
            #i = i + 1
        #print('Sum of first', num2, 'terms is ', sum)






#6. Write a program to calculate the factorial of a given number using for loop.

num3 = int(input('Enter the number you want factorial of  '))
factorial = 1

for i in range(1, num3+1):
    factorial = factorial * i
print(f"The factorial of {num3} is {factorial}")




#7. Program to print a following pattern.

num4 = int(input('Enter the number of patterns you want: '))

for i in range(num4):
    print('*' * (i+1))



#8. Program for another pattern

k = 3
for i in range(3):
    for j1 in range(k-1-i):
        print( " " * (k-1-i), end='')
        print('*' * (2*i+1), end='')
        print(" " * (k - 1 -1))
    


#8. Write multiplication table in reverse order.
    num5 = int(input('Enter the number: '))

for i in range(num5, 0, -1):
    print(str(i) + '*' + str(num5) + ' = ' + str(i*num5))



