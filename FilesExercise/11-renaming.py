#11. Write a program to rename a file to 'renamed_by_python'.txt

#how to delete a file using os module in python

import os

oldname = "dummyfile.txt" #create a 'dummyfile.txt' to see the effect
newname = 'renamed_by_python.txt'

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)


