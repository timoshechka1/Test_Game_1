import pygame
import settings

# Initialize pygame font module
pygame.font.init()

# UI Elements
label = pygame.font.Font(settings.FONT_PATH, 80)
lose_label = label.render("LOSE", False, settings.TEXT_COLOR_LOSE)
restart_label = label.render("RESTART", False, settings.TEXT_COLOR_RESTART)
restart_label_rect = restart_label.get_rect(topleft=(190, 200))

def draw_game_over(screen):
    """
    Draws the game over screen with lose message and restart button.

    Args:
        screen (pygame.Surface): The game screen surface to draw on

    Effects:
        - Fills screen with lose background color (settings.COLOR_SCREEN_LOSE)
        - Draws 'LOSE' text centered horizontally at y=100
        - Draws 'RESTART' button at position (120, 200)
    """
    screen.fill(settings.COLOR_SCREEN_LOSE)
    screen.blit(lose_label, (230, 100))
    screen.blit(restart_label, restart_label_rect)

def is_restart_clicked(pos):
    """
    Checks if restart button was clicked.

    Args:
        pos (tuple): (x, y) mouse position coordinates to check

    Returns:
        bool: True if mouse position is within restart button bounds,
              False otherwise

    Note:
        Uses the pre-defined restart_label_rect collision rectangle
    """
    return restart_label_rect.collidepoint(pos)


def draw_enemy_counter(screen, count, icon, is_game_active):
    """
    Рисует счетчик убийств только при активной игре

    Args:
        screen: Поверхность для отрисовки
        count: Текущее количество убийств
        icon: Иконка врага (Surface)
        is_game_active: Флаг активности игры (True/False)
    """
    if not is_game_active:
        return

    pos_x, pos_y = 20, 20
    screen.blit(icon, (pos_x, pos_y))
    font = pygame.font.Font(settings.FONT_PATH, 34)
    text = font.render(f"x {count}", True, (255, 255, 255))
    screen.blit(text, (pos_x + icon.get_width() + 10, pos_y + 5))