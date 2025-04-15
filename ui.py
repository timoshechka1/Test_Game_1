import pygame
import settings

pygame.font.init()

label = pygame.font.Font(settings.FONT_PATH, 80)
lose_label = label.render("LOSE", False, settings.TEXT_COLOR_LOSE)
restart_label = label.render("RESTART", False, settings.TEXT_COLOR_RESTART)
restart_label_rect = restart_label.get_rect(topleft=(120, 200))

def draw_game_over(screen):
    screen.fill(settings.COLOR_SCREEN_LOSE)
    screen.blit(lose_label, (200, 100))
    screen.blit(restart_label, restart_label_rect)

def is_restart_clicked(pos):
    return restart_label_rect.collidepoint(pos)
