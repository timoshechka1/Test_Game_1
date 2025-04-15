"""
SPAWNER MODULE DOCUMENTATION

This module handles the random generation of spawn timers for game entities.
It provides controlled randomization of spawn intervals within configurable bounds.
"""
import random
import settings

def get_random_spawn_time():
    """
    Generates a random spawn interval for game entities using stepped randomization.

    This function creates spawn timers that are multiples of the configured step size,
    ensuring predictable intervals while maintaining randomness. The actual spawn time
    will always be between the configured minimum and maximum values, inclusive of
    the minimum but exclusive of the maximum.

    Configuration Parameters (imported from settings module):
        ENEMY_SPAWN_MIN_TIME (int): Minimum spawn interval in milliseconds
        ENEMY_SPAWN_MAX_TIME (int): Maximum spawn interval in milliseconds
        ENEMY_SPAWN_STEP (int): Increment step size in milliseconds

    Mathematical Behavior:
        The function follows the formula:
        random_value ∈ [min, max) where (value - min) % step == 0

    Returns:
        int: A randomly selected spawn time in milliseconds that is:
             - Greater than or equal to ENEMY_SPAWN_MIN_TIME
             - Less than ENEMY_SPAWN_MAX_TIME
             - A multiple of ENEMY_SPAWN_STEP plus ENEMY_SPAWN_MIN_TIME

    Quality Assurance:
        - Guaranteed to return values within configured bounds
        - Always returns whole number multiples of the step size
        - Provides even distribution across possible values

    Example Usage:
        >>> settings.ENEMY_SPAWN_MIN_TIME = 2000
        >>> settings.ENEMY_SPAWN_MAX_TIME = 5000
        >>> settings.ENEMY_SPAWN_STEP = 1000
        >>> get_random_spawn_time()
        3000  # Possible output (could be 2000 or 4000)

    Implementation Notes:
        Uses Python's random.randrange() which is ideal for:
        - Integer-based random number generation
        - Stepped intervals
        - End-exclusive ranges
    """
    return random.randrange(
        settings.ENEMY_SPAWN_MIN_TIME,
        settings.ENEMY_SPAWN_MAX_TIME,
        settings.ENEMY_SPAWN_STEP
    )