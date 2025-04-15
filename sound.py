"""
SOUND MODULE DOCUMENTATION

This module handles all audio-related functionality for the game,
including background music playback and control. It uses Pygame's
mixer system for audio playback.
"""
import pygame
import settings

# Initialize Pygame's mixer system with default parameters
pygame.mixer.init()

# Load background music file from settings and configure volume
background_music = pygame.mixer.Sound(settings.BACKGROUND_MELODY)
background_music.set_volume(settings.BACKGROUND_MELODY_VOLUME)

def play_background_music():
    """
    Starts playback of the game's background music in an infinite loop.

    Behavior:
    - Begins playback of the pre-loaded background music track
    - Music will loop continuously until explicitly stopped
    - Uses the volume level configured in settings.BACKGROUND_MELODY_VOLUME
    - If music is already playing, this will restart playback

    Example:
        >>> play_background_music()  # Starts game music playback

    Note:
        The music track is loaded during module initialization from
        settings.BACKGROUND_MELODY path
    """
    background_music.play()

def stop_background_music():
    """
    Stops the currently playing background music.

    Behavior:
    - Immediately halts playback of background music
    - Has no effect if no music is currently playing
    - Can be restarted by calling play_background_music() again

    Example:
        >>> stop_background_music()  # Stops any currently playing music

    Note:
        This function provides a clean way to stop music during
        game over/pause scenarios
    """
    background_music.stop()