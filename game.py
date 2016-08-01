import sys
import os
import random

clear = lambda: os.system('clear')  # on Linux System
weapons = {"Great Sword":40}

#Changes Made By Dhaval:
#Level Up Functionality For Player (Includes exp, maxexp and level data members for player
#Adaptive strength(health and attack) for enemies
#Adaptive gain(gold and exp) from enemies

#To Do Ideas:
#Save and Load - File Handling - Simply Read and Write Player Stats
#Storyline? Boss Enemy?
#Dialogue? Humor?
#Text Graphic Display?

class Player:
    maxhealth = 100
    level = 1
    maxexp = 100
    def __init__(self, name):
        self.name = name
        self.health = self.maxhealth
        self.exp = 0
        self.base_attack = 10
        self.gold = 40
        self.potions = 2
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if(self.curweap == "Rusty Sword"):
            attack += 5
        elif(self.curweap == "Great Sword"):
            attack += 15

        return attack

    #@property
    def expgain(self,gain):
        self.exp += gain
        if(self.exp>=self.maxexp):
            self.level += 1
            self.base_attack = int(self.base_attack * 1.2)
            self.maxhealth = int(self.maxhealth * 1.2)
            self.exp -= self.maxexp
            self.maxexp *= 2
            self.health = self.maxhealth
            print("Congratulations! You Have Levelled Up!")

class Goblin:

    def __init__(self, name, maxh):
        self.name = name
        self.maxhealth = maxh*0.5
        self.health = self.maxhealth
        self.attack = int(self.maxhealth/10)
        self.goldgain = int(self.maxhealth/5)


class Zombie:

    def __init__(self, name, maxh):
        self.name = name
        self.maxhealth = maxh*0.7
        self.health = self.maxhealth
        self.attack = int(self.maxhealth/10)
        self.goldgain = int(self.maxhealth/5)


def store():
    # clear()
    print("Welcome to the shop")
    print("What would you like to buy?")
    print("1. Great Sword")
    print("2. Potion")
    print("3. Back")
    option = input('-->')

    if(option in weapons):
        if(PlayerIG.gold >= weapons[option]):
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You have bought %s" %option)
        else:
            print("You don't have enough gold")
    elif(option == "2"):
        if(PlayerIG.gold >= 20):
            PlayerIG.gold -= 20
            PlayerIG.potions += 1
            print("You have successfully bought a potion! You now have %i potions" %PlayerIG.potions)
    elif(option == "3"):
        start1()
    else:
        print("That item doesn't exit")

    input('\nPress Return To Continue')
    store()


def prefight():
    enemynum = random.randint(1, 2)
    global enemy
    if (enemynum == 1):
        enemy = Goblin("Goblin",PlayerIG.maxhealth)
    else:
        enemy = Zombie("Zombie",PlayerIG.maxhealth)
    fight()


def dead():
    # clear()
    print("You have died")


def win():
    PlayerIG.gold += enemy.goldgain
    #enemy.health = enemy.health = enemy.maxhealth
    print("You have defeated the %s" % enemy.name)
    print("You have found %i gold" % enemy.goldgain)
    print("You have gained %i experience" % int(enemy.maxhealth/3))
    PlayerIG.expgain(int(enemy.maxhealth / 3))
    input('Press Return To Continue')
    start1()


def attack():
    # clear()
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(int(enemy.attack / 2), enemy.attack)
    if (PAttack == PlayerIG.attack / 2):
        print("You miss !")
    else:
        enemy.health -= PAttack
        print("You did %i damage" % PAttack)
    if(enemy.health<=0):
        win()
    else:
        # clear()
        if (EAttack == EAttack / 2):
            print("Enemy missed")
        else:
            PlayerIG.health -= EAttack
            print("The enemy did %i damage" % EAttack)
        if (PlayerIG.health <= 0):
            dead()
        else:
            fight()


def drinkpotion():
    pass
    # clear()
    if (PlayerIG.potions == 0):
        print("You don't have any potions")
    else:
        PlayerIG.potions -= 1
        PlayerIG.health += 50
        if (PlayerIG.health > PlayerIG.maxhealth):
            PlayerIG.health = PlayerIG.maxhealth
        print("You drank a potion")
    input('')
    fight()


def run():
    # clear()
    runnum = random.randint(1, 3)
    if (runnum == 1):
        print("You have successfully ran away")
        input('')
        start1()
    else:
        print("You failed to get away")
        input('')
        EAttack = random.randint(int(enemy.attack / 2), enemy.attack)
        if (EAttack == EAttack / 2):
            print("Enemy missed")
        else:
            PlayerIG.health -= EAttack
            print("The enemy did %i damage" % EAttack)
        input(' ')
        if (PlayerIG.health <= 0):
            dead()
        else:
            fight()


def fight():
    # clear()
    print("%s   vs  %s" % (PlayerIG.name, enemy.name))
    print("%s's Health: %i/%i   %s's Health: %i/%i"
          % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("1. Attack")
    print("2. Drink Potion")
    print("3. Run")
    option = int(input('-->'))
    if (option == 1):
        attack()
    elif (option == 2):
        drinkpotion()
    elif (option == 3):
        run()
    else:
        fight()


def start1():
    # clear()
    print("Name: %s" % (PlayerIG.name))
    print("Level: %s" % (PlayerIG.level))
    print("Attack: %i" % (PlayerIG.attack))
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Experience Points: %i/%i" % (PlayerIG.exp, PlayerIG.maxexp))
    print("Current Weapon: %s" %PlayerIG.curweap)
    print("Gold: %i" % (PlayerIG.gold))
    print("Potions: %i" % (PlayerIG.potions))
    print("1. Fight")
    print("2. Store")
    print("3. Save")
    print("4. Exit")
    option = int(input("-->"))
    if (option == 1):
        prefight()
    elif (option == 2):
        store()
    elif (option == 3):
        pass
    elif (option == 4):
        sys.exit()
    else:
        start1()


def start():
    # clear()
    print("Hello, what's your name!\n")
    name = input("-->")
    global PlayerIG
    PlayerIG = Player(name)
    start1()


def main():
    # clear()
    print("Welcome to my game!\n")
    print("1. Start")
    print("2. Load")
    print("3. Exit")
    option = int(input("-->"))

    if (option == 1):
        start()
    elif (option == 2):
        pass
    elif (option == 3):
        sys.exit()
    else:
        main()


#GoblinIG = Goblin('Goblin')
#ZombieIG = Zombie('Zombie')
main()
