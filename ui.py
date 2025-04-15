"""
UI MODULE DOCUMENTATION

This module handles all user interface rendering and interaction logic,
including game over screens, buttons, and in-game HUD elements.
"""
import pygame
import settings

# Initialize pygame font module
pygame.font.init()

# UI Elements
# Main label font for game over text
label = pygame.font.Font(settings.FONT_PATH, 80)

# Game over text surface
lose_label = label.render("LOSE", False, settings.TEXT_COLOR_LOSE)

# Restart button surface
restart_label = label.render("RESTART", False, settings.TEXT_COLOR_RESTART)

# Restart button collision rectangle
restart_label_rect = restart_label.get_rect(topleft=(190, 200))

def draw_game_over(screen):
    """
    Renders the complete game over screen interface.

    Args:
        screen (pygame.Surface): The game's display surface to render on

    Behavior:
        1. Fills the screen with the lose background color (COLOR_SCREEN_LOSE)
        2. Draws the 'LOSE' text centered horizontally at y=100
        3. Draws the restart button at its predefined position

    Note:
        Uses pre-rendered text surfaces for better performance
    """
    screen.fill(settings.COLOR_SCREEN_LOSE)
    screen.blit(lose_label, (230, 100))
    screen.blit(restart_label, restart_label_rect)

def is_restart_clicked(pos):
    """
    Detects if the restart button was clicked.

    Args:
        pos (tuple): Mouse coordinates (x, y) to check against button bounds

    Returns:
        bool: True if coordinates are within restart button's collision rect,
              False otherwise

    Implementation:
        Uses pygame.Rect.collidepoint() for precise collision detection
    """
    return restart_label_rect.collidepoint(pos)


def draw_enemy_counter(screen, count, icon, is_game_active):
    """
    Renders the enemy kill counter HUD element during active gameplay.

    Args:
        screen (pygame.Surface): Game display surface to render on
        count (int): Current number of enemy kills to display
        icon (pygame.Surface): Enemy icon image surface
        is_game_active (bool): Game state flag (True = game running)

    Behavior:
        - Only renders when is_game_active is True
        - Draws enemy icon followed by kill count
        - Positions counter at top-left (20, 20)
        - Uses white text with 34px font size

    Visual Format:
        [Enemy Icon] x [Count]
    """
    if not is_game_active:
        return

    pos_x, pos_y = 20, 20
    screen.blit(icon, (pos_x, pos_y))
    font = pygame.font.Font(settings.FONT_PATH, 34)
    text = font.render(f"x {count}", True, (255, 255, 255))
    screen.blit(text, (pos_x + icon.get_width() + 10, pos_y + 5))