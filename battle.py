from game_over import game_over
import time

def normal_battle(player_object, enemy):
    battle = True
    while battle:

        print("HP:" + str(player_object.HP))
        if player_object.HP == 1: print("You are on your last legs!\n")
        time.sleep(1)
        player_damage = player_object.calculate_attack_damage(player_object.strength, player_object.level)
        player_damage = enemy.calculate_taken_damage_enemy(enemy.defence, player_damage)
        print("You attack the " + str(enemy.name) + " for " + str(player_damage) + " damage\n")
        enemy.HP -= player_damage


        if enemy.HP <= 0:
            print("The " + str(enemy.name) + " is dead!\n ")
            print("You get " + str(enemy.xp_dropped) + " xp\n")
            battle = False
            break

        enemy_damage = enemy.calculate_damage_given_enemy(enemy.strength, enemy.level)
        enemy_damage = player_object.calculate_taken_damage(player_object.defence, player_object.HP, enemy_damage)
        print("The " + str(enemy.name) + " attacks your for " + str(enemy_damage) + " damage\n")
        player_object.HP -= enemy_damage
        time.sleep(1)

        if player_object.HP <= 0:
            print("You have died!")
            battle = False
            game_over()
