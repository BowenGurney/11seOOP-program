# Learning intentions:
# - Create some default attributes of the class
# - Create the special print method that prints the status of the object

class Pet:
    def __init__(self, name, category, age, vaccination, address='unknown', ccard='unknown', owner='unknown', acc_balance=0):
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

p1 = Pet('Bonnie', 'Dog', vaccination=True, age=1, ccard='0411 8555 6077 4200')
print(p1)

#ACTIVITIES:
#1. Add a default new credit card value  of unknown

#2. In the __str__ method, let the user know if the pet has registered payment details  

#3. Add the vaccinated status  and include it in the special __str__ function