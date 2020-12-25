import classes

print("Cool Title\n") #re-do title
print("By TheBearSlicer\n")
input("Press Enter to start\n")

print("Welcome to the land of landia\n") #come up with world name
print("You are in the town of Black Hollows\n")
print("The dark lord must be stopped, go now hero")

def shop(shopLvl):
    print("What would you like to buy?\n")
    if shopLvl == 1:                         #idk how to make this better
        shopItems = {
            "Longsword" : "20gp",
            "Leather armor" : "30gp",
            "Potion" : "5gp",
            "Elixer" : "5gp"
        }
    if shopLvl == 2:         #add up to 5 shopLvl, then cry
        shopItems = {
            "Shiny sword" : "35gp",
            "Chainmail" : "50gp",
            "Potion" : "5gp",
            "Elixer" : "5gp"
        }
    if shopLvl == 3:
        shopItems = {
            "Platinum Sword" : "50gp",
            "Plate armor" : "75gp",
            "Ultra Potion" : "15gp",
            "Ultra Elixer" : "15gp"
        }
    if shopLvl == 4:
        shopItems = {
            "Blade of Heros" : "100gp",
            "Diamond Armor" : "150gp",
            "Ultra Potion" : "15gp",
            "Ultra Elixer" : "15gp"
        }
    if shopLvl == 5:
        shopItems = {
            "Legendary Blade" : "250gp",
            "Legendary Armor" : "350gp",
            "Super Potion" : "30gp",
            "Super Elixer" : "30gp"
        }
        
    print(shopLvl)

BlackHollows = location("Black Hollows", "Heros starting town", 1) #location is not defined

option1 = "1. Go to shop\n"
option2 = "2. Battle in field\n"
option3 = "3. Countinue towards the Evil Lords castle\n" #reseting options is dumb
option4 = "4. What is this place?" #whatever
option5 = "5.Equip"
print(option1, option2, option3, option4, option5)
    
playerChoice = int(input("1/2/3/4/5"))
    
if playerChoice == 1:
    shop(1)
    
