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