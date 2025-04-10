import pygame

pygame.init()
screen = pygame.display.set_mode((600, 476))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

background = pygame.image.load("images/background.png")
moving_left = [
    pygame.image.load("images/player_movement_left/player_movement_left_1.png"),
    pygame.image.load("images/player_movement_left/player_movement_left_2.png"),
    pygame.image.load("images/player_movement_left/player_movement_left_3.png"),
    pygame.image.load("images/player_movement_left/player_movement_left_4.png"),
    pygame.image.load("images/player_movement_left/player_movement_left_5.png"),
    pygame.image.load("images/player_movement_left/player_movement_left_6.png")
]
moving_rigth = [
    pygame.image.load("images/player_movement_right/player_movement_right_1.png"),
    pygame.image.load("images/player_movement_right/player_movement_right_2.png"),
    pygame.image.load("images/player_movement_right/player_movement_right_3.png"),
    pygame.image.load("images/player_movement_right/player_movement_right_4.png"),
    pygame.image.load("images/player_movement_right/player_movement_right_5.png"),
    pygame.image.load("images/player_movement_right/player_movement_right_6.png")
]

player_anim_count = 0

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(moving_rigth[player_anim_count], (300, 350))

    if player_anim_count == 5:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
