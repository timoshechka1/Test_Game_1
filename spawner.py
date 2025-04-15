import random
import settings

def get_random_spawn_time():
    """
    Generates a random time interval for enemy spawning within configured limits.

    The function uses the following settings from the settings module:
    - ENEMY_SPAWN_MIN_TIME: Minimum possible spawn time (in milliseconds)
    - ENEMY_SPAWN_MAX_TIME: Maximum possible spawn time (in milliseconds)
    - ENEMY_SPAWN_STEP: Step size for random time intervals (in milliseconds)

    Returns:
        int: A random spawn time interval in milliseconds, calculated as:
             random value between [ENEMY_SPAWN_MIN_TIME, ENEMY_SPAWN_MAX_TIME)
             with step size ENEMY_SPAWN_STEP

    Example:
        If settings are:
        ENEMY_SPAWN_MIN_TIME = 2000
        ENEMY_SPAWN_MAX_TIME = 5000
        ENEMY_SPAWN_STEP = 1000

        Possible return values: 2000, 3000, 4000
    """
    return random.randrange(
        settings.ENEMY_SPAWN_MIN_TIME,
        settings.ENEMY_SPAWN_MAX_TIME,
        settings.ENEMY_SPAWN_STEP
    )