name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95
paid = False
while_number = 1

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  global paid, account_balance
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      print('Valid Credit Card.')
      account_balance = 129.95
      account_balance = account_balance - 39
      print(f'Account Balance: {account_balance}')
      paid = True
      return True
  print('Invalid Credit Card.')
  return False

def vaccination_process():
  global while_number
  if paid == True:
    print("Your dog will be vaccinated shortly.")
    while_number = 0
  if paid == False:
    print("You have not paid yet. Please pay if you wish to continue.")
    confirmation_p = input('Do you wish to continue? ')
    if 'n' in confirmation_p or 'n' in confirmation_p:
      while_number = 0
  
help()
increase_age()

print(f'Your dog is {age}.')
confirmation_v = input('Do you wish to vaccinate your dog? ')
if 'Y' in confirmation_v or 'y' in confirmation_v:
  while while_number == 1:
    input_ccard = input('Card Number: ')[:19]
    verify_credit_card(input_ccard)
    vaccination_process()
elif 'N' in confirmation_v or 'n' in confirmation_v:
  print('ok dork')


# ACTIVITIES:
# There are many ways to complete these. How will you go about the job?
#1. Verify this number 1234 4334 1001 0000
#2. Ask the user for a credit card number and let them know if it is valid
#3. If the credit card is valid then reduce balance by $39
#4. Write and test a function to vaccinate Bonnie 
