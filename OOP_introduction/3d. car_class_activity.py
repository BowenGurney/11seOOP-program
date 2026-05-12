    # Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,price=None,sale=False):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = sale

    def __str__(self):
        possible_cars = 'Brand: ' + self.make + '\n Model: ' + self.model + '\n Year: ' + str(self.year) + '\n Price: ' + str(self.price) + '\n Sale: ' + str(self.for_sale)
        return possible_cars

c1 = Car('Mazda','6',2005)
c2 = Car('Kia', '3', 2009,'$1249.99',True)
c3 = Car('Ferrari','1',2011,'$600,000.00')
c4 = Car('Lamborgini', '23',2004,'$900,000',True)

cars = [c1, c2, c3, c4]

for car in cars:
    print(car)

#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop