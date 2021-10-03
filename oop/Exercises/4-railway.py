#4. Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information of train running on Railways.

class  Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print('********')
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print('*********')

    def fareInfo(self):
        print(f"The price of the ticket is: {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print('Your ticket has been booked! Your seat number is ', self.seats)
            self.seats = self.seats - 1
        else:
            print('Sorry this train is full, Please book after sometime!')

    
        
    

intercity = Train('Intercity Express', 100, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
    