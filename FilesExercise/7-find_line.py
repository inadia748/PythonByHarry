#7. Write a program to find out the line number where 'python' is present from Question 6.

content = True
i = 1

with open('log.txt') as f:
    while content:

        content = f.readline()  

        if 'python' in content.lower():
            print(content)
            print(f'Yes, python is present on line {i}')
            
        i+=1