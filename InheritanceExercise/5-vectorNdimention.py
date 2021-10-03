#5. write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot product of them.

class Vector:
    def __init__(self, vec):
        self.vec = vec 
    
    def __str__(self):
        str = ''
        index = 0
        for i in range(len(self.vec)):
            str += f"{i}a{index} +"
            index +=1
        return str[:-1]

    def __add__(self):
        pass



v1 = Vector([1, 4, 7])
print(v1)
