import sys
import os
import random
import pickle

clear = lambda: os.system('clear')  # on Linux System
weapons = {"Great Sword": 40}


# Changes Made By Dhaval:
# Level Up Functionality For Player (Includes exp, maxexp and level data members for player
# Adaptive strength(health and attack) for enemies
# Adaptive gain(gold and exp) from enemies
# Rooms - 3 rooms for now - Increasing enemy strength and expgain - Boss in last room

# ToDo Ideas:
# Save and Load - File Handling - Simply Read and Write Player Stats
# Storyline? Boss Enemy?
# Dialogue? Humor?

# Todo:
# 1. weapons and current weapons .. ! (Great sword, Rusty Sword, .. and swapping between them)
# 2. At level advancement, health increased by drinking potion should not remain constant 50
# 3. There must be something like "maxlevel" so that if a player has not advanced even after attaining
# level up and saved his game then his current level should not show maxlevel
# 4. Storyline and Indentation ( Because style of presentation is as important as what we present. Period . )

def saveStats():
    fh = open("example", "wb")

    # getting all variables
    name = PlayerIG.name
    health = PlayerIG.health
    maxhealth = PlayerIG.maxhealth
    exp = PlayerIG.exp
    level = PlayerIG.level
    maxexp = PlayerIG.maxexp
    attack = PlayerIG.attack
    gold = PlayerIG.gold
    potions = PlayerIG.potions
    weap = PlayerIG.weap
    curweap = PlayerIG.curweap
    rkill = PlayerIG.rkill
    maxrkill = PlayerIG.maxrkill
    room = PlayerIG.room

    pickle.dump(
        [name, health, maxhealth, exp, level, maxexp, attack, gold, potions, weap, curweap, rkill, maxrkill, room], fh)
    fh.close()

    print("File succesfully saved !")


def loadStats():
    try:
        fh = open("example", "rb")
        # loading values from example file in the variables
        (name, health, maxhealth, exp, level, maxexp, attack, gold, potions, weap, curweap, rkill, maxrkill,
         room) = pickle.load(fh)

        global PlayerIG
        # initializing PlayerIG variable
        PlayerIG = Player(name)
        # setting all parameters
        PlayerIG.health = health
        PlayerIG.maxhealth = maxhealth
        PlayerIG.exp = exp
        PlayerIG.level = level
        PlayerIG.maxexp = maxexp
        PlayerIG.attack = attack
        PlayerIG.gold = gold
        PlayerIG.potions = potions
        PlayerIG.weap = weap
        PlayerIG.curweap = curweap
        PlayerIG.rkill = rkill
        PlayerIG.maxrkill = maxrkill
        PlayerIG.room = room

        start1()
        fight()

    except:
        print("No saved file exists.. You can start a new game instead")
        main()


class Player:
    maxhealth = 100
    level = 1
    room = 1
    maxexp = 100

    def __init__(self, name):
        self.name = name
        self.health = self.maxhealth
        self.exp = 0
        self.base_attack = 10
        self.gold = 40
        self.potions = 2
        self.rkill = 0
        self.maxrkill = self.room * 5
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if (self.curweap == "Rusty Sword"):
            attack += 5
        elif (self.curweap == "Great Sword"):
            attack += 15

        return attack

    # @property
    def expgain(self, gain):
        self.exp += gain
        if (self.exp >= self.maxexp):
            self.level += 1
            self.base_attack = int(self.base_attack * 1.2)
            self.maxhealth = int(self.maxhealth * 1.2)
            self.exp -= self.maxexp
            self.maxexp *= 2
            self.health = self.maxhealth
            print("Congratulations! You Have Levelled Up!")

    def roomup(self):
        if (self.rkill >= self.maxrkill):
            print("You Can Move To Next Room If You Wish")
            print("Press Y to Advance")
            choice = input('-->')
            if (choice == 'Y'):
                self.rkill = 0
                self.room += 1
                self.maxrkill = self.room * 5
                print("Congratulations! You Have Advanced To Room %i" % self.room)
                start1()
            else:
                start1()
        else:
            print("You Cannot Advance To Next Room Yet")
            print("You Only Have (%i/%i) Kills" % (self.rkill, self.maxrkill))
            print("You Must Kill %i More Enemies To Advance" % int(self.maxrkill - self.rkill))
            print("Press Return To Continue")
            input(' ')
            start1()

    @attack.setter
    def attack(self, value):
        self._attack = value


class Goblin:
    def __init__(self, name, maxh):
        self.name = name
        self.maxhealth = maxh * 0.5
        self.health = self.maxhealth
        self.attack = int(self.maxhealth / 10)
        self.goldgain = int(self.maxhealth / 5)


class Zombie:
    def __init__(self, name, maxh):
        self.name = name
        self.maxhealth = maxh * 0.7
        self.health = self.maxhealth
        self.attack = int(self.maxhealth / 10)
        self.goldgain = int(self.maxhealth / 5)


def store():
    # clear()
    print("Welcome to the shop")
    print("What would you like to buy?")
    print("1. Great Sword")
    print("2. Potion")
    print("3. Back")
    option = input('-->')

    if (option in weapons):
        if (PlayerIG.gold >= weapons[option]):
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You have bought %s" % option)
        else:
            print("You don't have enough gold")
        input('Press Return To Continue')
        store()
    elif (option == "2"):
        if (PlayerIG.gold >= 20):
            PlayerIG.gold -= 20
            PlayerIG.potions += 1
            print("You have successfully bought a potion! You now have %i potions" % PlayerIG.potions)
        else:
            print("You don't have enough gold")
        input('Press Return To Continue')
        store()
    elif (option == "3"):
        start1()
    else:
        print("That item doesn't exit")
        input('Press Return To Continue')
        store()


def prefight():
    enemynum = random.randint(1, 2)
    global enemy
    if (PlayerIG.room == 1):
        if (enemynum == 1):
            enemy = Goblin("Goblin", PlayerIG.maxhealth)
        else:
            enemy = Zombie("Zombie", PlayerIG.maxhealth)
    elif (PlayerIG.room == 2):
        if (enemynum == 1):
            enemy = Goblin("Goblin Leader", int(PlayerIG.maxhealth * 1.3))
        else:
            enemy = Zombie("Zombie Legion", int(PlayerIG.maxhealth * 1.3))
    elif (PlayerIG.room == 3):
        enemy = Goblin("Goblin King", PlayerIG.maxhealth * 2)
    fight()


def dead():
    # clear()
    print("You have died! You managed to reach room %i" % PlayerIG.room)
    sys.exit(0)


def win():
    PlayerIG.gold += enemy.goldgain
    # enemy.health = enemy.health = enemy.maxhealth
    print("You have defeated the %s" % enemy.name)
    print("You have found %i gold" % enemy.goldgain)
    if (PlayerIG.room == 1):
        print("You have gained %i experience" % int(enemy.maxhealth / 3))
    elif (PlayerIG.room == 2):
        print("You have gained %i experience" % int(enemy.maxhealth / 2))
    elif (PlayerIG.room == 3):
        print("You have gained %i experience" % int(enemy.maxhealth))
    PlayerIG.expgain(int(enemy.maxhealth / 3))
    PlayerIG.rkill += 1
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
    if (enemy.health <= 0):
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


def autoattack():
    # clear()
    PDamage = 0
    EDamage = 0
    while (PlayerIG.health > enemy.attack):
        PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
        EAttack = random.randint(int(enemy.attack / 2), enemy.attack)
        if (PAttack == PlayerIG.attack / 2):
            PAttack = 0
        else:
            enemy.health -= PAttack
            PDamage += PAttack
        if (enemy.health <= 0):
            break
        else:
            # clear()
            if (EAttack == EAttack / 2):
                EAttack = 0
            else:
                PlayerIG.health -= EAttack
                EDamage += EAttack
            # Player Shouldn't Die in AutoAttack - If It Reaches Here Then Logic Is Wrong
            if (PlayerIG.health <= 0):
                print("You Died In AutoAttack! Shouldn't Have Happened!")
                input("Press Return To Continue")
                dead()
    print("You Did %i Damage To Enemy" % PDamage)
    print("The Enemy Did %i Damage To You" % EDamage)
    if (enemy.health <= 0):
        win()
    else:
        input("Press Return To Continue ")
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
    input('Press Return To Continue')
    fight()


def run():
    # clear()
    runnum = random.randint(1, 2)
    if (runnum == 1):
        print("You have successfully ran away")
        input('Press Return To Continue')
        start1()
    else:
        print("You failed to get away")
        EAttack = random.randint(int(enemy.attack / 2), enemy.attack)
        if (EAttack == EAttack / 2):
            print("Enemy missed")
        else:
            PlayerIG.health -= EAttack
            print("The enemy did %i damage" % EAttack)
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
    print("3. Flee")
    flag = True
    while (flag):
        try:
            option = int(input("-->"))
            flag = False
        except:
            print("Invalid Input!! Try Again!!")
            flag = True
    if (option == 1):
        print("Auto Attack? (Enter 1 For To Auto Attack)")
        choice = input("-->")
        if (choice == '1'):
            autoattack()
        else:
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
    print("Current Weapon: %s" % PlayerIG.curweap)
    print("Gold: %i" % (PlayerIG.gold))
    print("Potions: %i" % (PlayerIG.potions))
    print("1. Fight")
    print("2. Store")
    print("3. Check Room Advancement")
    print("4. Save")
    print("5. Exit")
    flag = True
    while (flag):
        try:
            option = int(input("-->"))
            flag = False
        except:
            print("Invalid Input!! Try Again!!")
            flag = True
    if (option == 1):
        prefight()
    elif (option == 2):
        store()
    elif (option == 3):
        PlayerIG.roomup()
    elif (option == 4):
        saveStats()
        start1()
    elif (option == 5):
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
    flag = True
    while (flag):
        try:
            option = int(input("-->"))
            flag = False
        except:
            print("Invalid Input!! Try Again!!")
            flag = True
    if (option == 1):
        start()
    elif (option == 2):
        loadStats()
    elif (option == 3):
        sys.exit()
    else:
        main()


# GoblinIG = Goblin('Goblin')
# ZombieIG = Zombie('Zombie')
main()
