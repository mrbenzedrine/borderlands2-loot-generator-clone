def calculate_stats(level, rarity):

    max_health = calculate_max_health_increase(level, rarity)

    stats = {
        'max health': max_health
    }

    return stats

def calculate_max_health_increase(level, rarity):

    return '+0%'

