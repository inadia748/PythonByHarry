

class RailwayForm:
    formType = 'RailwayForm'
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


nadiasApplication = RailwayForm()
nadiasApplication.name = 'Nadia'
nadiasApplication.train = 'Mulan Express'

nadiasApplication.printData()


print(nadiasApplication)
print(nadiasApplication.formType)
