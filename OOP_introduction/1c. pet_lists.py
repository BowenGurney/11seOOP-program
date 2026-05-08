import random
loop = True

#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets

pet_name = ['Dork',  'Ponyo', 'Princess Mononoke', 'Prince Ashitaka', 'Hootie']
species = ['Chihuahua', 'Pomeranian', 'Yorkshire Terrier', 'Maltese', 'Papillon', 'Shih Tzu', 'Pug', 'Cat']
age = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 34, 120]
vaccination_status = [False, True, False, True]

#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''

for i in range(1):
    
  pet_name = random.choice(pet_name)
  species = random.choice(species)
  age = random.choice(age)
  vaccination_status = random.choice(vaccination_status)

  print(f'Pet name: {pet_name}') 
  print(f'Species: {species}')
  print(f'Age: {age}')
  print(f'Vaccination Status: {vaccination_status}')

if vaccination_status == False:
    while loop == True:
      confirmation = input('Do you wish to vaccinate your pet? ')
      if ('Y') in confirmation or ('y') in confirmation:
        loop = False
        print('Your pet has been booked to be vaccinated.')
      elif ('N') in confirmation or ('n') in confirmation:
        loop = False
        print('Thank you for your time.')
      else:
        print('Yes or no, please.')

#3. Demonstrate what happens when an item is deleted

  #ACTIVITIES:
# In each activity test out that the printing of data is still valid

#1. Add a new animal named Hootie, its a blowfish, it is 34 years

#2. Vaccinate an unvaccinated animal (create vaccination)

#3. Remove an animal and make sure that all the printing is correct
# added hootie then removed her as a blowfish
# cause i dont want any blowfishes in MY petstore
# she's a cat now