import pygame
import random
import settings

def animation_character(current_count, max_frames):
    return (current_count + 1) % max_frames


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())

background = pygame.image.load(settings.BACKGROUND_IMAGE_PATH).convert_alpha()

enemy_police = pygame.image.load(settings.ENEMY_IMAGE_PATH + "enemy_movement_1.png").convert_alpha()
enemy_anim_count = 0
enemy_list_in_game = []

moving_left = [
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_1.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_2.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_3.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_4.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_5.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_LEFT_PATH + "player_movement_left_6.png").convert_alpha()
]
moving_right = [
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_1.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_2.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_3.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_4.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_5.png").convert_alpha(),
    pygame.image.load(settings.PLAYER_RIGHT_PATH + "player_movement_right_6.png").convert_alpha()
]
player_anim_count = 0
is_jump = False

background_x = 0
background_melody = pygame.mixer.Sound(settings.BACKGROUND_MELODY)
background_melody.set_volume(settings.BACKGROUND_MELODY_VOLUME)
background_melody.play()


enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, random.randrange(settings.ENEMY_SPAWN_MIN_TIME,
                                                    settings.ENEMY_SPAWN_MAX_TIME,
                                                    settings.ENEMY_SPAWN_STEP))

label = pygame.font.Font(settings.FONT_PATH, 80)
lose_label = label.render("LOSE", False, settings.TEXT_COLOR_LOSE)
restart_label = label.render("RESTART", False, settings.TEXT_COLOR_RESTART)
restart_label_rect = restart_label.get_rect(topleft=(120, 200))

bottle = pygame.image.load(settings.BOTTLE_IMAGE_PATH + "glass-bottle.png").convert_alpha()
bottles = []

gameplay = True

running = True
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))
    if gameplay:
        player_rect = moving_left[0].get_rect(topleft=(settings.PLAYER_START_X, settings.PLAYER_START_Y))

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
            screen.blit(moving_left[player_anim_count], (settings.PLAYER_START_X, settings.PLAYER_START_Y))
        else:
            screen.blit(moving_right[player_anim_count], (settings.PLAYER_START_X, settings.PLAYER_START_Y))

        if keys[pygame.K_LEFT] and settings.PLAYER_START_X > settings.PLAYER_MOVE_LIMIT_LEFT:
            settings.PLAYER_START_X -= settings.PLAYER_SPEED
        elif keys[pygame.K_RIGHT] and settings.PLAYER_START_X < settings.PLAYER_MOVE_LIMIT_RIGHT:
            settings.PLAYER_START_X += settings.PLAYER_SPEED

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if settings.PLAYER_JUMP_COUNT >= -5:
                if settings.PLAYER_JUMP_COUNT > 0:
                    settings.PLAYER_START_Y -= (settings.PLAYER_JUMP_COUNT ** 2)
                else:
                    settings.PLAYER_START_Y += (settings.PLAYER_JUMP_COUNT ** 2)
                settings.PLAYER_JUMP_COUNT -= 1
            else:
                is_jump = False
                settings.PLAYER_JUMP_COUNT = 5

        player_anim_count = animation_character(player_anim_count, len(moving_right))

        background_x -= 5

        if background_x == -600:
            background_x = 0

        if bottles:
            for i, el in enumerate(bottles):
                screen.blit(bottle, (el.x, el.y))
                el.x += 4
                if el.x > 610:
                    bottles.pop(i)
                if enemy_list_in_game:
                    for idx, enemy_element in enumerate(enemy_list_in_game):
                        if el.colliderect(enemy_element):
                            enemy_list_in_game.pop(idx)
                            bottles.pop(i)
    else:
        screen.fill(settings.COLOR_SCREEN_LOSE)
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
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b:
            bottles.append(bottle.get_rect(topleft=(settings.PLAYER_START_X + 50, settings.PLAYER_START_Y + 50)))

    clock.tick(settings.FPS)