import time

class monster:
    def __init__(self, name, lvl, Hp, attack):
        self.name = name
        self.lvl = lvl
        self.maxHp = Hp
        self.attack = attack
        
        
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
playerWeapon = "none" #no weapon :(
playerArmor = "none" #no naked :)
playerInventory = {
    "1.Potion" : 0,
    "2.Elixer" :0,
    "3.Super Potion" : 0,
    "4.Super Elixer" : 0,
    "5.Mega Potion" : 0,
    "6.Mega Elixer" : 0
}
playerMaxHp = 20
playerHp = playerMaxHp
playerMaxMp = 10
playerMp = playerMaxMp
playerLvl = 1
playerXp = 0



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

def shop(shopLvl, playerGp, playerInventory, playerWeapon, playerArmor):
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
            print("You bought a", shopWeapon, "for", weaponCost, "gp!\n")
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
            print("You bought a", shopArmor, "for", armorCost, "gp!\n")
            time.sleep(0.8)
            playerGp = playerGp - armorCost
            print("You now have", playerGp, "gp left\n")
            time.sleep(0.8)
            playerArmor = shopArmor
        elif armorCost > playerGp:
            print("Not enough gold\n")
        else: print('Error\n')
        
    if shopChoice == '3' :
        if potionCost < playerGp:
            print("You bought a", shopPotion, "for", potionCost, "gp!\n")
            time.sleep(0.8)
            playerGp = playerGp - potionCost
            print("You now have", playerGp, "gp left\n")
            time.sleep(0.8)
            if shopPotion == "3. Potion":
                playerInventory["1.Potion"] = playerInventory["1.Potion"] + 1
            if shopPotion == "3. Super Potion":
                playerInventory["3.Super Potion"] = playerInventory["3.Super potion"] + 1
            if shopPotion == "3. Mega Potion":
                playerInventory["3.Mega Potion"] = playerInventory["3.Mega Potion"] + 1
        elif potionCost < playerGp:
            print("Not enough gold\n")
    if shopChoice == '4' :
        if elixerCost < playerGp:
            print("You bought a", shopElixer, "for", elixerCost, "gp!\n")
            time.sleep(0.8)
            playerGp = playerGp - elixerCost
            print("You now have", playerGp, "gp left\n")
            time.sleep(0.8)
            if shopElixer == "4. Elixer":
                playerInventory["2.Elixer"] = playerInventory["2.Elixer"] + 1
            if shopElixer == "3. Super Elixer":
                playerInventory["4.Super Elixer"] = playerInventory["4.Super Elixer"] + 1
            if shopElixer == "3. Mega Elixer":
                playerInventory["6.Mega Elixer"] = playerInventory["6.Mega Elixer"] + 1
        elif elixerCost < playerGp:
            print("Not enough gold!\n")
        
def useItem(playerInventory, playerHp, playerMp):
    print(playerInventory)
    print("What to use?")
    useChoice = input("1/2/3/4/5/6")
        
    if useChoice == "1":
        if playerInventory["1.Potion"] > 0:
            playerHp = playerHp + 5
            playerInventory["1.Potion"] = playerInventory["1.Potion"] - 1
            print("You used a potion and gained 5 hp, you now have", playerHp, "hp!\n")
            time.sleep(0.8)
        elif playerInventory["1.Potion"] == 0:
            print("You have no potions!\n")
        else: print("Error")
    
    if useChoice == "2":
        if playerInventory["2.Elixer"] > 0:
            playerMp = playerMp + 3 
            playerInventory["2.Elixer"] = playerInventory["2.Elxer"] - 1
            print("You used a elixer and gained 3 mp, you now have", playerMp, "mp!\n")
            time.sleep(0.8)
        elif playerInventory["2.Elixer"] == 0:
            print("You have no elixers!\n")
        else: print("Error")
        #add these for all other potion types
        

def battle(playerHp, playerMp, playerInventory, playerWeapon, playerArmor, playerMaxHp, playerMaxMp, monster):
    print(monster.name, "attacks1\n")
    time.sleep(0.8)
    while battleTime == True:
        print("Your HP:", playerHp, "HP\n")
        print("Your MP:", playerMp, "MP\n")
        print("Enemy HP:", monster.Hp, "HP\n")
        print("Your action?\n")
        print("1. Attack")
        print("2. Spells")
        print("3. Items")
        battleChoice = input("1/2/3")
        
        
#weapons:  
longsword = weapons("Longsword", 5, 10)
greatsword = weapons("Greatsword", 10, 15)
crestedblade = weapons("Crested Blade", 20, 23)
diamondsword = weapons("Diamond Sword", 35, 38)
enchantedsword = weapons("Enchanted Sword", 60, 75)

#armors:
leatherarmor = armor("Leather Armor ", 2, 15)
chainmailarmor = armor("Chainmail", 4, 23)
platearmor = armor("Plate Armor", 7, 30)
diamondarmor = armor("Diamond Armor", 12, 75)
angelicarmor = armor("Angelic Armor", 20, 113)

#spells:
Bolt = spell("Bolt", 8, 3, 0) # Tier 1
Heal = spell("Heal", 0, 5, 15) # Tier 1
Fireball = spell("Fireball", 16, 8, 0) # Tier 2
Heal_II = spell("Heal II", 0, 12, 25) # Tier 2
Lightning = spell("Lightning", 33, 18, 0) # Tier 3
Heal_III = spell("Heal III", 0, 23, 40) # Tier 3
Explosion = spell("Explosion", 50, 30, 0) # Tier 4
Ultra_Heal = spell("Ultra Heal", 0, 35, 65) # Tier 4
Void = spell("Void", 99, 50, 0) #Tier 5
Full_Heal = spell("Full Heal", 0, 65, playerMaxHp) #Teir 5

oldXp = 10
    
BlackHollows = location("Black Hollows", "Heros starting town", 1)
DesertofAzerband = location("Desert of Azerband", "The great desert full of monsters", 2)
currentLocation = "Black_Hollows"
while currentLocation == "Black_Hollows":

    #monsters:

    Goblin = monster("Goblin", 1, 8, 3)
    Bear = monster("Bear", 1, 6, 4)
    Bandit = monster("Bandit", 2, 10, 5)
    Zombie = monster("Zombie", 2, 12, 4)
    Theif = monster("Theif", 3, 10, 6)
    Ghost = monster("Ghost", 3, 12, 5)
    bossDarkKnight = monster("Dark Knight", 4, 20, 8)

    if playerHp > playerMaxHp:
        playerHp = playerMaxHp
    if playerMp > playerMaxMp:
        playerMp = playerMaxHp
    option1 = "1. Go to shop\n"
    option2 = "2. Battle in field\n" #uh oh a battle system
    option3 = "3. Countinue towards the Evil Lords castle\n" #reseting options is dumb
    option4 = "4. What is this place?\n" #whatever
    option5 = "5. Use potions/elixers\n" 
    option6 = "6. View stats/equipment"
    time.sleep(0.8)
    print("Your action?\n")
    print(option1, option2, option3, option4, option5, option6)
    
    playerChoice = input("1/2/3/4/5/6")
    
    if playerChoice == '1':
        shop(BlackHollows.shopLvl, playerGp, playerInventory, playerWeapon, playerArmor)
    
    if playerChoice == '2':

    if playerChoice == '4':
        print("This is", BlackHollows.name, "It is the", BlackHollows.whatIs, "it has a shop level of", BlackHollows.shopLvl)
        
    if playerChoice == '5':
        useItem(playerInventory, playerHp, playerMp)
    if playerChoice == '6':
        time.sleep(0.8)
        print("Max HP:", playerMaxHp, "\nMax MP:", playerMaxHp, "\n Weapon:", playerWeapon, "\n Armor:", playerArmor)
        
    
    
