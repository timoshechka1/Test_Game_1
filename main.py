import pygame

pygame.init()
screen = pygame.display.set_mode((600, 476))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

background = pygame.image.load("images/background.png")
player = pygame.image.load("images/player_movement_left/player_movement_left_1.png")

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(player, (300, 350))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
