#3. Create a class with a class a attribute a; Create an object from it and set a directly using object.a = 0. Does this change the class attribute.

class Sample:
    a = "Nadia"

obj = Sample()
obj.a = 'John'
print(Sample.a)
print(obj.a)