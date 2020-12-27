import time

class monster:
    def __init__(self, name, lvl, maxHp, attack, mana):
        self.name = name
        self.lvl = lvl
        self.maxHp = maxHp
        self.attack = attack
        self.mana = mana
        
class location:
    def __init__(self, name, whatIs, shopLvl):
        self.name = name
        self.whatIs = whatIs
        self.shopLvl = shopLvl
        
class spell:
    def __init__(self, name, dmg, cost, healValue):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.healValue = healValue

class consumable:
    def __init__(self, name, heal, mpheal):
        self.name = name
        self.heal = heal
        self.mpheal = mpheal
        
class weapons:
    def __init__(self, name, baseDmg, value):
        self.name = name
        self.baseDmg = baseDmg
        self.value = value

class armor:
    def __init__(self, name, dmgReduc, value):
        self.name = name            
        self.dmgReduc = dmgReduc
        self.value = value
        
playerGp = 75 #starting GP
playerWeapon = "fists" #no weapon :(
playerArmor = "clothes" #no naked :)

print("Cool Title\n") #re-do title
time.sleep(0.5)
print("By TheBearSlicer\n")
time.sleep(0.5)
input("Press Enter to start\n")
time.sleep(0.2)
print("Welcome to the land of Ziglearanth\n")
time.sleep(1)
print("You are in the town of Black Hollows\n")
time.sleep(1)
print("The dark lord must be stopped, go now hero\n")
time.sleep(1)

def shop(shopLvl, playerGp):
    print("What would you like to buy?\n")
    if shopLvl == 1:
        shopWeapon = "1. Longsword"
        weaponCost = 20
        shopArmor = "2. Leather Armor"
        armorCost = 30
        shopPotion = "3. Potion"
        potionCost = 5
        shopElixer =  "4. Elixer"
        elixerCost = 5
    if shopLvl == 2:
        shopWeapon = "1. Greatsword"
        weaponCost = 30
        shopArmor = "2. Chainmail Armor"
        armorCost = 45
        shopPotion = "3. Potion"
        potionCost = 5
        shopElixer =  "4. Elixer"
        elixerCost = 5
    if shopLvl == 3:
        shopWeapon = "1. Crested Blade"
        weaponCost = 45
        shopArmor = "2. Plate Armor"
        armorCost = 60
        shopPotion = "3. Super Potion"
        potionCost = 10
        shopElixer =  "4. Super Elixer"
        elixerCost = 10
    if shopLvl == 4:
        shopWeapon = "1. Diamond Sword"
        weaponCost = 75
        shopArmor = "2. Diamond Armor"
        armorCost = 125
        shopPotion = "3. Super Potion"
        potionCost = 10
        shopElixer =  "4. Super Elixer"
        elixerCost = 10
    if shopLvl == 5:
        shopWeapon = "1. Enchanted Sword"
        weaponCost = 150
        shopArmor = "2. Angelic Armor"
        armorCost = 225
        shopPotion = "3. Mega Potion"
        potionCost = 20
        shopElixer =  "4. Mega Elixer"
        elixerCost = 20
    
    shopItems = {
        shopWeapon : weaponCost,
        shopArmor : armorCost,
        shopPotion : potionCost,
        shopElixer : elixerCost
    }
        
    print(shopItems,"\nYour gp:", playerGp)
    shopChoice = input("1/2/3/4")
    
    if shopChoice == '1':
        if weaponCost < playerGp:
            print("You bought a", shopWeapon, "for", weaponCost, "!\n")
            time.sleep(0.8)
            playerGp = playerGp - weaponCost
            print("You now have", playerGp, "gp left\n")
            time.sleep(0.8)
            playerWeapon = shopWeapon
            
        elif weaponCost > playerGp:
            print("Not enough gold\n")
        else:  print("Error\n")
    if shopChoice == '2':
        if armorCost < playerGp:
            print("You bought a", shopArmor, "for", armorCost, "!\n")
            time.sleep(0.8)
            playerGp = playerGp - armorCost
            print("You now have", playerGp, "gp left\n")
            time.sleep(0.8)
            playerArmor = shopArmor
        elif armorCost > playerGp:
            print("Not enough gold\n")
        else: print('Error\n')
        
        #add consumable shop
    
   

BlackHollows = location("Black Hollows", "Heros starting town", 1)
currentLocation = "Black_Hollows"
while currentLocation == "Black_Hollows":
    option1 = "1. Go to shop\n"
    option2 = "2. Battle in field\n" #uh oh a battle system
    option3 = "3. Countinue towards the Evil Lords castle\n" #reseting options is dumb
    option4 = "4. What is this place?\n" #whatever
    option5 = "5.Use potions/elixers\n" #make this
    print(option1, option2, option3, option4, option5)
    
    playerChoice = int(input("1/2/3/4/5"))
    
    if playerChoice == 1:
        shop(BlackHollows.shopLvl, playerGp)
    
