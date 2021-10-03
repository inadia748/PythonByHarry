
class Person:

    def __init__(self):
        print('Initializng Person... \n')

    country = "Bangladesh"
    def takeBreak(self):
        print('I am breathing...')

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print('Initializing Employee...\n')

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print('I am an Employee so I am breathing')

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print('Initializing Programmer...\n')

    def getSalary(self):
        print('No salary to Programmer')

    def takeBreak(self):
        super().takeBreak()
        print('I am  a programmer so I am breathing....+++')



# p = Person()
# p.takeBreak()

# e = Employee()
# e.takeBreak()

# pr = Programmer()
# pr.takeBreak()

#e = Employee()

pr = Programmer()




