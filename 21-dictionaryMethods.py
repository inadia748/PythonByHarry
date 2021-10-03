myDict = {
    'Fast': "In a Quick Manner",
    'Nadia': 'It is a name of a girl',
    'marks': [1, 5, 10],
    
    'anotherDict': {
        'Sarah': 'Graphic Designer',
        'marks': [89, 92, 100],
    },

    1: 3.9
}

print(myDict.keys())  #Print the keys of the dictionary.
print(myDict.values()) #Print the values of the dictionary.
print(myDict.items()) #Print the (key, value) for all contents of the dictionary.

print(myDict)


updateDict = {
    'John': 'Youtuber',
    'Number': [33, 394, 83, 22],
    'Nadia': 'A Learner'
}

myDict.update(updateDict) #Updates the dictionary by adding  key-value pairs from UpdateDict and also updates 'key' if necessary

print(myDict)


# The difference between .get and [] syntax in Dictionaries:

print(myDict['Nadia']) #will throw you an error if the the key is not present. 

#example: print(myDict['Nadia2']), will throw you an error as 'throws an error as harry2 is not present in the dictionary.


print(myDict.get('Nadia'))  # Prints value associated with with key 'Nadia'
#example: print(myDict.get('Nadia2')), will you none.


