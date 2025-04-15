import random
import settings

def get_random_spawn_time():
    return random.randrange(
        settings.ENEMY_SPAWN_MIN_TIME,
        settings.ENEMY_SPAWN_MAX_TIME,
        settings.ENEMY_SPAWN_STEP
    )