#10. Write a program to wipe out the contents of a file using python.


filename = 'sample1.txt'

with open(filename, 'w') as f:
    f.write('')