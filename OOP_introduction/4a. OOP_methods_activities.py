# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    while_number = 0
    def __init__(self, name, category, age=0, vaccination=True, ccard='unknown', acc_balance=0, acc_bill=0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccination
        self.account_balance = acc_balance
        self.account_bill = acc_bill

    def __str__(self):
      human_age = self.pet_to_human_years()
      my_status = 'Name: ' + self.name + '\n Category: ' + self.category + '\n Age: ' + str(self.age) + '\n Vaccination: ' + str(self.vaccinated) + '\n Human age: ' + str(human_age)
      return my_status
    
    def have_birthday(self):
        self.age += 1

    def clear_balance(self):
        pet.account_bill = 0
        print(f"\n Payment received! {pet.name}'s balance is cleared.")

    def vaccination_process(self):
        while_number = 0
        if pet.vaccinated == False:
            while while_number == 0:
                confirmation = input(f'Do you wish to vaccinate {pet.name}? ')
                if ('Y') in confirmation or ('y') in confirmation:
                    while_number = 1
                    account_bill = account_bill + 12.99
                    payment_process = input('Do you wish to pay now or later?')
                    if ('Y') in payment_process or ('y') in payment_process:
                        pet.account_balance = pet.account_balance - 12.99
                        print(f'Current Balance: {pet.account_balance}')
                        pet.clear_balance(self)
                    if ('N') in payment_process or ('n') in payment_process:
                        print(f'Current bill is 12.99.')
                elif ('N') in confirmation or ('n') in confirmation:
                    while_number = 1
                    print('Thank you for your time.')
                else:
                    print('Yes or no, please.')
    
    def pet_to_human_years(self):
        if pet.category == 'Dog':
            human_age = pet.age * 7 
        elif pet.category == 'Cat':
            human_age = pet.age * 6
        else:
            human_age = None
        return human_age

p1 = Pet('Jack', 'Dog', 2, True, acc_balance=100)
p2 = Pet('Back', 'Cat', 5, False, acc_balance=1000)
p3 = Pet('Dack', 'Dogfish', 4, False, acc_balance=600)

Pets = [p1, p2, p3]

for pet in Pets:
    while_number = 0
    print(pet)
    pet.vaccination_process()
    pet.pet_to_human_years()

    
#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comepleted each activity correctly.