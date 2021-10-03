class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in  {self.company} is {self.salary} \n {signature}")

    @staticmethod
    def greet():
        print('Hava a good day!')

    @staticmethod
    def time():
        print('The time is 9AM in the morning')

nadia = Employee()
nadia.salary = 10000
nadia.getSalary('Thanks!')
nadia.greet()
nadia.time()