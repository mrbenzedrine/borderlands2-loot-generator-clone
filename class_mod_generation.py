import random

from gear.class_mods.class_mod import ClassMod
import gear.class_mods.assassin as assassin
import gear.class_mods.commando as commando
import gear.class_mods.gunzerker as gunzerker
import gear.class_mods.mechromancer as mechromancer
import gear.class_mods.psycho as psycho
import gear.class_mods.siren as siren

def generate(rarity, level):
    
    class_mod_character = choose_character()

    class_mod_module = get_class_mod_module(class_mod_character)

    class_mod_type = class_mod_module.choose_class_mod_type()
    class_mod_info = {
        'stat_changes': class_mod_module.get_stat_changes_function(class_mod_type)(rarity, level),
        'skill_point_changes': class_mod_module.get_skill_point_changes_function(class_mod_type)(rarity, level)
    }

    return ClassMod(level, rarity, class_mod_character, class_mod_info['stat_changes'], class_mod_info['skill_point_changes'])

def choose_character():
    random_integer = random.randint(0,5)
    switcher = {
        0: 'assassin',
        1: 'commando',
        2: 'gunzerker',
        3: 'mechromancer',
        4: 'psycho',
        5: 'siren'
    }
    return switcher.get(random_integer, 'nothing')

def get_class_mod_module(character):
    switcher = {
        'assassin': assassin,
        'commando': commando,
        'gunzerker': gunzerker,
        'mechromancer': mechromancer,
        'psycho': psycho,
        'siren': siren
    }
    return switcher.get(character, 'nothing')