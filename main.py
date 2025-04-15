import pygame
import random

def animation_character(current_count, max_frames):
    return (current_count + 1) % max_frames


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 476))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load("images/icon.png").convert_alpha())

background = pygame.image.load("images/background.png").convert_alpha()

enemy_police = pygame.image.load("images/enemy_movement/enemy_movement_1.png").convert_alpha()
enemy_anim_count = 0
enemy_list_in_game = []

moving_left = [
    pygame.image.load("images/player_movement_left/player_movement_left_1.png").convert_alpha(),
    pygame.image.load("images/player_movement_left/player_movement_left_2.png").convert_alpha(),
    pygame.image.load("images/player_movement_left/player_movement_left_3.png").convert_alpha(),
    pygame.image.load("images/player_movement_left/player_movement_left_4.png").convert_alpha(),
    pygame.image.load("images/player_movement_left/player_movement_left_5.png").convert_alpha(),
    pygame.image.load("images/player_movement_left/player_movement_left_6.png").convert_alpha()
]
moving_right = [
    pygame.image.load("images/player_movement_right/player_movement_right_1.png").convert_alpha(),
    pygame.image.load("images/player_movement_right/player_movement_right_2.png").convert_alpha(),
    pygame.image.load("images/player_movement_right/player_movement_right_3.png").convert_alpha(),
    pygame.image.load("images/player_movement_right/player_movement_right_4.png").convert_alpha(),
    pygame.image.load("images/player_movement_right/player_movement_right_5.png").convert_alpha(),
    pygame.image.load("images/player_movement_right/player_movement_right_6.png").convert_alpha()
]
player_anim_count = 0
player_speed = 5
player_x = 150
player_y= 333
is_jump = False
jump_count = 5

background_x = 0
background_melody = pygame.mixer.Sound("sounds/background_melody.mp3")
background_melody.set_volume(0.01)
background_melody.play()


enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, random.randrange(2000, 3000, 500))

label = pygame.font.Font("fonts/Roboto-Black.ttf", 80)
lose_label = label.render("LOSE", False, (193, 196, 199))
restart_label = label.render("RESTART", False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(120, 200))

bottle = pygame.image.load('images/glass-bottle.png').convert_alpha()
bottles = []

gameplay = True

running = True
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))
    if gameplay:
        player_rect = moving_left[0].get_rect(topleft=(player_x, player_y))

        if enemy_list_in_game:
            for idx, element in enumerate(enemy_list_in_game):
                screen.blit(enemy_police, element)
                element.x -= 10

                if element.x < -10:
                    enemy_list_in_game.pop(idx)

                if player_rect.colliderect(element):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(moving_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(moving_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -5:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 5

        player_anim_count = animation_character(player_anim_count, len(moving_right))

        background_x -= 5

        if background_x == -600:
            background_x = 0

        if keys[pygame.K_b]:
            bottles.append(bottle.get_rect(topleft=(player_x + 50, player_y + 50)))

        if bottles:
            for i, el in enumerate(bottles):
                screen.blit(bottle, (el.x, el.y))
                el.x += 4
                if el.x > 610:
                    bottles.pop(i)
                if enemy_list_in_game:
                    for idx, enemy in enumerate(enemy_list_in_game):
                        if el.colliderect(enemy):
                            enemy_list_in_game.pop(idx)
                            bottles.pop(i)
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (200, 100))
        screen.blit(restart_label, restart_label_rect)
        background_melody.stop()

        touch = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(touch) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            enemy_list_in_game.clear()
            bottles.clear()
            background_melody.play()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy_police.get_rect(topleft=(620, 330)))

    clock.tick(10)