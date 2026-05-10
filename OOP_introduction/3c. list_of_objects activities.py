# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age=0, vaccination=True, address='unknown', ccard='unknown', owner='unknown', acc_balance=0):
        self.name = name
        self.category = category
        self.age = age
        self.vaccination = vaccination
        self.ccard = ccard
        self.address = address
        self.owner = owner
        self.acc_balance = acc_balance
    
    def __str__(self):
        payment_status = 'Unregistered'
        if len(self.ccard) == 19:
            payment_status = 'Unregistered'
        
        my_status = 'Name: ' + self.name + '\n Category: ' + self.category + '\n Age: ' + str(self.age) + '\n Vaccination: ' + str(self.vaccination) + '\n Payment Status: ' + payment_status
        return my_status

p1 = Pet('Jack Gullo', 'Dog')
p2 = Pet('Hack Bullo', 'Ostrich', 4)
p3 = Pet('Tack Tullo', 'Thingy', 12)
p4 = Pet('Dack Gunlow', 'Starfish')

pets = [p1, p2, p3, p4]

for pet in pets:
    print(pet)
    print('')

#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list


