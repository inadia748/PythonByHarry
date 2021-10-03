greeting= "Good Morning, "
name = 'Harry'
#print(type(name))


#Concatinating 2 strings
# print(greeting + name)
# c = greeting + name
# print(c)


print(name[0])
print(name[1])
print(name[2])
print(name[4])
#print(name[5]) #string index out of range. It is an error. It will go from index 0 to 4.


#String does not allow item assignment
    #name[3] = 'd', It is not allowed item assignment. ---> Does not work


#Harry
# 0 to 3, it will exclude 3rd index
print(name[0:3])  #Har

#1 to 4, it will exclude 4th index
print(name[1:4]) #arr

print(name[:4]) #Harr, it is same as 0 to 4, it will exclude 4th index.
print(name[0:])  #Harry
print(name[1:]) #arry

#negative indices.
c = name[-4:-1] # is same as name[1:4]
print(c)


#Slicing with skip value

name1 = 'HarryIsGood'
d = name1[0::2]
print(d) #Hrysod
d = name1[0::3]
print(d) #Hrso