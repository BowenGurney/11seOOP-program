# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age, vaccination, ccard, address, owner="unknown", acc_balance=0):
        self.name = name
        self.category = category
        self.age = age
        self.vaccination = vaccination
        self.ccard = ccard
        self.address = address
        self.owner = owner
        self.acc_balance = acc_balance

p1 = Pet('Bonnie', 'Dog', 8, True, '0238 8735 9283 2938', '17 Park Drive, The Tung', acc_balance=111.11)
print(p1.name)
print(p1.category)
print(p1.age)
print(p1.vaccination)
print(p1.ccard)
print(p1.address)
print(p1.owner)
print(p1.acc_balance)

p2 = Pet('Foxy', 'Dog', 1, True, '9872 9824 6579 0120', '16 Park Drive, The Tung', 'Hack Bullo',)
print(p2.name)
print(p2.category)
print(p2.age)
print(p2.vaccination)
print(p2.ccard)
print(p2.address)
print(p2.owner)
print(p2.acc_balance)

#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)