# 1. Write a program to store seven fruits in a list entered by the user.

f1 = input('Enter fruit number1:  ')
f2 = input('Enter fruit number2:  ')
f3 = input('Enter fruit number3:  ')
f4 = input('Enter fruit number4:  ')
f5 = input('Enter fruit number5:  ')
f6 = input('Enter fruit number6:  ')
f7 = input('Enter fruit number7:  ')

myFruitList = [f1, f2, f3, f4, f5, f6, f7]

print(myFruitList)



#2. Write a program to accept marks of 6 students and display them in sorted manner.

s1 = int(input('Enter the marks of Student1: '))
s2 = int(input('Enter the marks of Student2: '))
s3 = int(input('Enter the marks of Student3: '))
s4 = int(input('Enter the marks of Student4: '))
s5 = int(input('Enter the marks of Student5: '))
s6 =  int(input('Enter the marks of Student6: '))

marks = [s1, s2, s3, s4, s5, s6]
marks.sort()
print(marks)


#3. Check that a tuple cannot be changed in python

a = (2, 4, 5, 3, 2)
a[0] = 45


#4. Write a program to find the sum of list of 4 numbers

x = [2, 4, 56, 7]
print(x[0] + x[1] + x[2] + x[3])
print(sum(x)) # Will give you the sum of items in any list


#5. Write a program to count the number of zeros in the following tuple.
y = (7, 0, 8, 0, 0, 9)
print(y.count(0))
