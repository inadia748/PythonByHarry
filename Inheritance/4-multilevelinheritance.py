class Person:
    country = "Bangladesh"
    def takeBreak(self):
        print('I am breathing...')

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print('I am an Employee so I am breathing')

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print('No salary to Programmer')



p = Person()
e = Employee()
pr = Programmer()


p.takeBreak()
e.takeBreak()
pr.takeBreak()

#print(p.company) #throws an error

print(e.company)
print(pr.company)

print(pr.country)