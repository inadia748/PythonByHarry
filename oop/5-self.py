# class Employee:
#     company = "Google"
#     def getSalary(self):
#         print('Salary is 100k')

# nadia = Employee()
# #nadia.getSalary()
# Employee.getSalary(nadia)




class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee woring in {self.company} is {self.salary}")

nadia = Employee()
nadia.salary = 100000
nadia.getSalary()

