def calculate_stats(level, rarity):

    cooldown_rate_increase = calculate_cooldown_rate_increase(level, rarity)

    stats = {
        'cooldown rate': cooldown_rate_increase
    }

    return stats

def calculate_cooldown_rate_increase(level, rarity):

    return '+0%'

