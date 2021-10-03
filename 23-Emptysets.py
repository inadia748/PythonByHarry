#Important: This syntax will create an empty dictionary.

a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(8)
b.add(88)
b.add(4)
b.add(8) #Adding a value repeatedly does not change a set
b.add(8)
b.add((0, 32, 50)) #(0,32, 50) is a tuple

#b.add({4:5}) #cannot add list or dictionary to sets. {4:5} is a dictionary
print(b)

print(len(b)) # prints the length of the set 'b'
print(b)

#Removal of an Item
b.remove(4) #removes 5 from set
#b.remove(15) # throws an error while trying to remove 15(which is not present in the set).

print(b)


b.add(13)
print(b)

print(b.pop()) #removes random element from the set and returns the element that is removed.
print(b)