import math

weapons_parts_stats_modifiers = {
    
    'body': {

        'Bandit': 1,
        'Dahl': 1,
        'E-Tech': 1,
        'Hyperion': 1,
        'Jakobs': 1,
        'Maliwan': 1,
        'Tediore': 1,
        'Torgue': 1,
        'Vladof': 1

    },

    'barrel': {

        'Bandit': 1,
        'Dahl': 1,
        'E-Tech': 1,
        'Hyperion': 1,
        'Jakobs': 1,
        'Maliwan': 1,
        'Tediore': 1,
        'Torgue': 1,
        'Vladof': 1

    },

    'grip': {

        'Bandit': 1,
        'Dahl': 1,
        'E-Tech': 1,
        'Hyperion': 1,
        'Jakobs': 1,
        'Maliwan': 1,
        'Tediore': 1,
        'Torgue': 1,
        'Vladof': 1

    },

    'scope': {

        'Bandit': 1,
        'Dahl': 1,
        'E-Tech': 1,
        'Hyperion': 1,
        'Jakobs': 1,
        'Maliwan': 1,
        'Tediore': 1,
        'Torgue': 1,
        'Vladof': 1

    }

}

rarity_modifiers = {
    
    'White': 1,
    'Green': 1.05,
    'Blue': 1.1,
    'Purple': 1.2,
    'E-Tech': 1.35,
    'Orange': 1.5

}

def level_modifer_function(level):

    # This will change, just putting some random function here
    # for the moment

    return math.exp(level)