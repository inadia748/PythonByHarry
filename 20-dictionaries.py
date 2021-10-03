myDict = {
    'Fast': "In a Quick Manner",
    'Nadia': 'It is a name of a girl',
    'marks': [1, 5, 10],
    
    'anotherDict': {
        'Sarah': 'Graphic Designer',
        'marks': [89, 92, 100],
    }
}

print(myDict['Fast'])
print(myDict['marks'])
myDict['marks'] = [38, 40, 83] #it is mutable.
print(myDict['anotherDict'])
print(myDict)