class Employee:
    company = 'Google'
    salary = 100

nadia = Employee()
sarah = Employee()

#Creating instance attribute salary for both the object.
nadia.salary = 200
sarah.salary = 500
print(nadia.company)
print(sarah.company)

Employee.company = 'Youtube'
print(nadia.company)
print(sarah.company)


print(nadia.salary)
print(sarah.salary)

#it throws an error as address is not present in the instance class.
#print(nadia.address)