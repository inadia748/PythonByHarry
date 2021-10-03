#2. Write a class calculator capable of finding square, cube and squareroot of a number.  Add a static method to greet the user with 'hello'



class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f"The value of {self.number} square is {self.number ** 2} ")
    def cube(self):
         print(f"The value of {self.number} cube is {self.number ** 3} ")
    def squareroot(self):
         print(f"The value of {self.number} squareroot is {self.number ** 0.5} ")

    @staticmethod
    def greet():
        print('Hello, Welcome to Calcutor')


a = Calculator(3)
a.square()
a.cube()
a.squareroot()
a.greet()