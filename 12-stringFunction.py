story = "Once there was a girl named Nadia, who learns tutorials from Youtube there"

print(story[0:5])


#String Functions

print(len(story)) #68
print(story.endswith('girl'))
print(story.endswith('ube'))
print(story.count('N'))
print(story.count('a'))
print(story.count('who'))
print(story.count('was'))

print(story.capitalize())


print(story.find("Nadia")) #28
print(story.find('nadia')) #-1
print(story.find('there')) #5

print(story.replace('Nadia', 'Syeda Nadia Islam'))