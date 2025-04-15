import pygame
import settings

# Initialize pygame mixer module for audio playback
pygame.mixer.init()

# Load background music audio file
background_music = pygame.mixer.Sound(settings.BACKGROUND_MELODY)
# Set default volume level from settings
background_music.set_volume(settings.BACKGROUND_MELODY_VOLUME)

def play_background_music():
    """
    Starts playing the background music in an infinite loop.

    Args:
        loops (int): Number of times to repeat the sound.
                   -1 (default) for infinite looping.
                   0 plays once, 1 plays twice, etc.

    Note:
        - Uses the pre-loaded background_music Sound object
        - Volume is controlled by settings.BACKGROUND_MELODY_VOLUME
        - Music will loop continuously by default
    """
    background_music.play()

def stop_background_music():
    """
    Stops the currently playing background music immediately.

    Effects:
        - Halts playback of the background_music Sound object
        - Can be restarted with play_background_music()

    Note:
        - Does not reset playback position
        - Subsequent play() calls will restart from beginning
    """
    background_music.stop()