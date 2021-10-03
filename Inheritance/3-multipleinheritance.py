class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiver"
    level = 2

    def upgradeLevel(self):
        self.level = self.level + 1

# class Programmer(Employee,Freelancer):
#     name = "Nadia"

class Programmer(Freelancer, Employee):
    name = "Nadia"


p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)