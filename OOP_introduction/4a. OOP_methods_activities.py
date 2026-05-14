# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

vaccination = True
while_number = 0

class Pet:
    def __init__(self, name, category, age=0, vaccinated=True):
        global vaccination
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = vaccinated
        self.account_balance = 0

    def __str__(self):
      my_status = 'Name: ' + self.name + '\n Category: ' + self.category + '\n Age: ' + str(self.age) + '\n Vaccination: ' + str(self.vaccinated)
      return my_status
    
    def have_birthday(self):
        self.age += 1

p1 = Pet('Jack', 'Dog', 2, True)
p2 = Pet('Back', 'Bog Turtle', 5, False)
p3 = Pet('Dack', 'Dogfish', 4, False)

Pets = [p1, p2, p3]

for pet in Pets:
    while_number = 0
    print(pet)
    if pet.vaccinated == False:
        while while_number == 0:
            confirmation = input(f'Do you wish to vaccinate {pet.name}? ')
            if ('Y') in confirmation or ('y') in confirmation:
                while_number = 1
                print('Your pet has been booked to be vaccinated.')
            elif ('N') in confirmation or ('n') in confirmation:
                while_number = 1
                print('Thank you for your time.')
            else:
                print('Yes or no, please.')

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.