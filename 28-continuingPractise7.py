#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their name. Assume that the names are unique.

favlang = {}

a = input('Enter your language Sarah: ')
b = input('Enter your language Oishi: ')
c = input('Enter your language Nadia: ')
d = input('Enter your language Jamie: ')

favlang['Sarah'] = a
favlang['Oishi'] = b
favlang['Nadia'] = c
favlang['Jamie'] = d

print(favlang)


#7. If the names of two friends are same; What will happen to the program of 6? Answer: If the keys are same, the latest value to the key will be inserted. 


#8. If languages of two friends are same, What will happen to the program of 6? Answer: Nothing will happen, but the keys must be unique.

#9. Can you change the values inside a list which is contained in set s.  s = {8, 7, 12, 'Harry', [1, 2]}.  Answer: No, you cannot store a list in a set.

#hashable means it is unlikely to change.

#list is unhashable meaning it can be modified.
