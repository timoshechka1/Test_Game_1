import pygame
import settings

pygame.mixer.init()

background_music = pygame.mixer.Sound(settings.BACKGROUND_MELODY)
background_music.set_volume(settings.BACKGROUND_MELODY_VOLUME)

def play_background_music():
    background_music.play()

def stop_background_music():
    background_music.stop()