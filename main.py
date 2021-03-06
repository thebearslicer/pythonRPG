from classes import *
from welcome import *
from battle import *
from game_over import *
import json


player = PlayerClass(20, 5, 5, 1, 0, "")  # HP, str, def, level, xp, name


def load_data(path):
    with open(str(path)) as f:
        loaded_save_data = json.load(f)
    return loaded_save_data


def save_player(path, input_stats_dict):
    with open(str(path), 'w') as json_file:
        json.dump(input_stats_dict, json_file)


def create_stats_dict(playerObject):
    created_stats_dict = {
        "HP": playerObject.HP,
        "strength": playerObject.strength,
        "defence": playerObject.defence,
        "level": playerObject.level,
        "xp": playerObject.xp,
        "name": playerObject.name
    }
    return created_stats_dict





try:
    save_data = load_data('C:/programming/python/textRpg/save.json')
    player = PlayerClass(save_data["HP"],
                         save_data["strength"],
                         save_data["defence"],
                         save_data["level"],
                         save_data["xp"],
                         save_data["name"])

except FileNotFoundError:
    player.name = welcome()
    stats_dict = create_stats_dict(player)
    save_player('C:/programming/python/textRpg/save.json', stats_dict)
test_enemy = EnemyClass(10, 5, 25, 10, 40, "Test")

normal_battle(player, test_enemy)

