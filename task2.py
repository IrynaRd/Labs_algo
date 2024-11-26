class Passenger:
    def __init__(self):
        self.passengers = []

    def enter(self, item):
        self.passengers.append(item)
        print(f"Зайшов {item}")

    def go_out(self):
        went_out = self.passengers.pop(0)
        print(f"Вийшов {went_out}")
        return went_out
    
    def display_passengersNumber(self):
        pass_number = len(self.passengers)
        print(f"Пасажири в автобусі: {pass_number}")

passenger = Passenger()
passenger.enter("Pavlo")
passenger.enter("Dmytro")
passenger.enter("Petro")

passenger.display_passengersNumber()
passenger.go_out()
passenger.display_passengersNumber()
    
