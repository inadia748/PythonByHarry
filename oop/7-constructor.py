class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        print('Employee is created')
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f'The name of the employee is {self.name}')
        print(f'The salary of the employee is {self.salary}')
        print(f'The subunit of the employee is {self.subunit}')

    def getSalary(self, signature):
        print(f"Salary for this employee working in  {self.company} is {self.salary} \n {signature}")

    @staticmethod
    def greet():
        print('Hava a good day!')

    @staticmethod
    def time():
        print('The time is 9AM in the morning')



nadia = Employee('Nadia', 4000, 'Youtube')
#nadia = Employee() ---> This throws an error (missing 3 required positional arguments.)
nadia.getDetails()