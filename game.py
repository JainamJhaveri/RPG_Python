import sys
import os
import random
clear = lambda : os.system('clear') #on Linux System

class Player:
    maxhealth = 100
    def __init__(self, name):
        self.name = name
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.potions = 0

class Goblin:
    maxhealth = 50
    def __init__(self, name):
        self.name = name
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10
GoblinIG = Goblin('Goblin')

class Zombie:
    maxhealth = 70
    def __init__(self, name):
        self.name = name
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15
ZombieIG = Zombie('Zombie')

def store():
    pass

def prefight():
    enemynum = random.randint(1,2)
    global enemy
    if(enemynum == 1):
        enemy = GoblinIG
    else:
        enemy = ZombieIG
    fight()


def dead():
    # clear()
    print("You have died")
    pass

def win():
    PlayerIG.gold += enemy.goldgain
    enemy.health = enemy.health = enemy.maxhealth
    print("You have defeated the %s" %enemy.name)
    print("You found %i gold"%enemy.goldgain)
    input('')
    start1()

def attack():
    # clear()
    PAttack = random.randint(PlayerIG.attack/2, PlayerIG.attack)
    EAttack = random.randint( int(enemy.attack/2), enemy.attack)
    if(PAttack == PlayerIG.attack/2):
        print("You miss !")
    else:
        enemy.health -= PAttack
        print("You did %i damage" %PAttack)
    input(' ')
    # clear()
    if(EAttack == EAttack/2):
        print("Enemy missed")
    else:
        PlayerIG.health -= EAttack
        print("The enemy did %i damage" %EAttack)
    input(' ')
    if(PlayerIG.health <= 0):
        dead()
    else:
        fight()

def drinkpotion():
    pass
    # clear()
    if(PlayerIG.potions == 0):
        print("You don't have any potions")
    else:
        PlayerIG.health += 50
        if(PlayerIG.health > PlayerIG.maxhealth):
            PlayerIG.health = PlayerIG.maxhealth
        print("You drank a potion")
    input('')
    fight()

def run():
    # clear()
    runnum = random.randint(1,3)
    if(runnum == 1):
        print("You have successfully ran away")
        input('')
        start1()
    else:
        print("You failed to get away")
        input('')
        EAttack = random.randint(int(enemy.attack/2), enemy.attack)
        if(EAttack == EAttack/2):
            print("Enemy missed")
        else:
            PlayerIG.health -= EAttack
            print("The enemy did %i damage" %EAttack)
        input(' ')
        if(PlayerIG.health <= 0):
            dead()
        else:
            fight()

def fight():
    # clear()
    print("%s   vs  %s" %(PlayerIG.name, enemy.name))
    print("%s's Health: %i/%i   %s's Health: %i/%i"
          %(PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("1. Attack")
    print("2. Drink Potion")
    print("3. Run")
    option = int(input('-->'))
    if(option == 1):
        attack()
    elif(option == 2):
        drinkpotion()
    elif(option == 3):
        run()
    else:
        fight()

def start1():
    #clear()
    print( "Name: %s"   %(PlayerIG.name) )
    print( "Attack: %i" %(PlayerIG.attack))
    print( "Health: %i/%i" %(PlayerIG.health, PlayerIG.maxhealth))
    print( "Gold: %i" %(PlayerIG.gold))
    print( "Potions: %i" %(PlayerIG.potions))
    print("1. Fight")
    print("2. Store")
    print("3. Save")
    print("4. Exit")
    option = int(input("-->"))
    if(option == 1):
        prefight()
    elif(option == 2):
        store()
    elif(option == 3):
        pass
    elif(option == 4):
        sys.exit()
    else:
        start1()


def start():
    #clear()
    print("Hello, what's your name!\n")
    name = input("-->")
    global PlayerIG
    PlayerIG = Player(name)
    start1()

def main():
    #clear()
    print("Welcome to my game!\n")
    print("1. Start")
    print("2. Load")
    print("3. Exit")
    option = int(input("-->"))

    if(option == 1):
        start()
    elif(option == 2):
        pass
    elif(option == 3):
        sys.exit()
    else:
        main()

main()
