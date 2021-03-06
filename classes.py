import random


class PlayerClass:
    def __init__(self, HP, strength, defence, level, xp, name):
        self.HP = HP
        self.strength = strength
        self.defence = defence
        self.level = level
        self.xp = xp
        self.name = name

    def level_up(self, maxHP, strength, defence, level):
        level += 1
        increase = level ** 1.03
        maxHP += increase
        strength += increase
        defence += increase

    def calculate_attack_damage(self, strength, level):
        attack_lower = round(level + 1 ** 1.02)
        attack_upper = round(level + 1 ** 1.06)
        attack = random.randint(attack_lower, attack_upper)
        attack += strength
        return attack

    def calculate_taken_damage(self, defence, HP, damage):
        damage_lower = round(damage + 1 ** 1.02)
        damage_upper = round(damage + 1 ** 1.06)
        damage = random.randint(damage_lower, damage_upper)
        damage -= defence
        if damage > HP: damage = HP - 1
        if damage < 1: damage = 1
        return damage

    def calculate_xp_requirement(self, level):
        xp_requirement = round((4 * (level ** 3)) / 5)
        return xp_requirement


class EnemyClass:
    def __init__(self, HP, strength, defence, level, xp_dropped, name):
        self.HP = HP
        self.strength = strength
        self.defence = defence
        self.level = level
        self.xp_dropped = xp_dropped
        self.name = name

    def calculate_damage_given_enemy(self, strength, level):
        attack_lower = round(level + 1 ** 1.02)
        attack_upper = round(level + 1 ** 1.06)
        given_damage = random.randint(attack_lower, attack_upper)
        given_damage += strength
        return given_damage

    def calculate_taken_damage_enemy(self, defence, damage):
        damage_lower = round(damage + 1 ** 1.02)
        damage_upper = round(damage + 1 ** 1.06)
        enemy_damage_taken = random.randint(damage_lower, damage_upper)
        enemy_damage_taken -= defence
        if enemy_damage_taken < 0: enemy_damage_taken = 1
        return enemy_damage_taken

