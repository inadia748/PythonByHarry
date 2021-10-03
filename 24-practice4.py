#1. Write a program to create a dictionary of Hindi words with values as their english translation.Provide user with an option to look it up.

myDict = {
    'Pankha': 'Fan',
    'Dabba': 'Box',
    'Vastu': 'Item',
}

print('Options are ', myDict.keys())
a = input('Enter the hindi word\n')

#This may throw you an error, if the key is not present in the dictionary.
print('The meaning of your word is:', myDict[a])
#or
#Below line will not throw you and error if the key is not present in the dictionary.
print('The meaning of your word is: ', myDict.get(a))





