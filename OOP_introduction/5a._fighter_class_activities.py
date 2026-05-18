#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    ## Creating the fighter object with name, health, weapon, and shield
    def __init__(self,name,starting_health,weapon,shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
    
    ## Creating the random possible attacks, Character Report
    def report(self):
        print(self.name + ':' + '\n Health:', str(self.health) + '\n Defense: ' + str(self.shield))

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print(' Attack power:', attack_power)
        return attack_power
    
Hero = Fighter('Jack',100,50,20)
Troll = Fighter('Bum',100,20,10)

while Hero.health > 0 and Troll.health > 0:
    Hero.report()
    Troll.report()
    print('You attack the Troll!')
    Troll.health -= Hero.random_attack()
    Troll.report()
    print('He attacks back!')
    Hero.health -= Troll.random_attack()
    Hero.report()
    print(' ')

if Hero.health < 0:
    print('You lose!')

elif Troll.health < 0:
    print('You win!')