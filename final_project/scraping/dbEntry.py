class DBEntry:
    def __init__(self, price, ticketType, age, discount, date, departure, destination, duration, startTime, arrivalTime, changes, tariffClass):
        self.price = price
        self.ticketType = ticketType
        self.age = age 
        self.discount = discount 
        self.date = date
        self.departure = departure
        self.destination = destination
        self.duration = duration
        self.startTime = startTime
        self.arrivalTime = arrivalTime
        self.changes = changes
        self.tariffClass = tariffClass
    def __str__(self):
        return f'{self.price},{self.ticketType},{self.age},{self.discount},{self.date},{self.departure},{self.destination},{self.duration},{self.startTime},{self.arrivalTime},{self.changes},{self.tariffClass}'
    def toList(self):
        return [self.price, self.ticketType, self.age, self.discount, self.date, self.departure, self.destination, self.duration, self.startTime, self.arrivalTime, self.changes, self.tariffClass]
