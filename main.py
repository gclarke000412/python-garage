class ParkingGarage:
    def __init__(self, capacity):
        self.tickets = list(range(1, capacity + 1))
        self.parkingSpaces = list(range(1, capacity + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket_number] = {"paid": False, "parking_space": parking_space}
            print(f"Ticket #{ticket_number} issued. Please park in space #{parking_space}.")
        else:
            print("Sorry, the garage is full.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket and not self.currentTicket[ticket_number]["paid"]:
            amount_paid = input("Enter the amount you want to pay: ")
            if amount_paid:
                self.currentTicket[ticket_number]["paid"] = True
                print(f"Ticket #{ticket_number} has been paid. You have 15 minutes to leave.")
            else:
                print("Payment not received.")
        else:
            print("Invalid ticket number or ticket is already paid.")

    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]["paid"]:
                parking_space = self.currentTicket[ticket_number]["parking_space"]
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(parking_space)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                print("Ticket has not been paid. Please pay before leaving.")
        else:
            print("Invalid ticket number.")

# Example parameters
garage = ParkingGarage(10)  #parking garage with 10 parking spaces

garage.takeTicket()
garage.payForParking()
garage.leaveGarage()
