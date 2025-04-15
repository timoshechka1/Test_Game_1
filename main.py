# Third party libraries
import pygame

# Local modules
import settings
import player
import enemy
import spawner
import bottle
import ui

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())

background = pygame.image.load(settings.BACKGROUND_IMAGE_PATH).convert_alpha()
background_x = 0
background_melody = pygame.mixer.Sound(settings.BACKGROUND_MELODY)
background_melody.set_volume(settings.BACKGROUND_MELODY_VOLUME)
background_melody.play()
music_stopped = False

player_instance = player.Player()
enemies = []
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time())
bottles = []

gameplay = True
running = True

while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))

    if gameplay:

        if enemies:
            for idx, en in enumerate(enemies):
                en.update()
                en.draw(screen)

                if en.is_off_screen():
                    enemies.pop(idx)
                elif player_instance.get_rect().colliderect(en.get_rect()):
                    gameplay = False
                    background_melody.stop()

        keys = pygame.key.get_pressed()

        player_rect = player_instance.get_rect()
        player_instance.draw(screen)

        if keys[pygame.K_LEFT]:
            player_instance.move_left()
        else:
            player_instance.move_right()

        if keys[pygame.K_SPACE]:
            player_instance.jump()

        player_instance.update()

        if keys[pygame.K_LEFT] and player_instance.x > settings.PLAYER_MOVE_LIMIT_LEFT:
            player_instance.x -= player_instance.speed
        elif keys[pygame.K_RIGHT] and player_instance.x < settings.PLAYER_MOVE_LIMIT_RIGHT:
            player_instance.x += player_instance.speed

        background_x -= 5
        if background_x == -600:
            background_x = 0

        for b in bottles[:]:
            b.update()
            b.draw(screen)

            if not b.is_active or b.is_off_screen():
                bottles.remove(b)
                continue

            for e in enemies[:]:
                if b.get_rect().colliderect(e.get_rect()):
                    enemies.remove(e)
                    bottles.remove(b)
                    break
    else:
        ui.draw_game_over(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not gameplay:
            if ui.is_restart_clicked(event.pos):
                gameplay = True
                player_instance.reset()
                enemies.clear()
                bottles.clear()
                background_melody.play()
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_timer:
            enemies.append(enemy.Enemy())
            pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time())
        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            new_bottle = bottle.throw_bottle(player_instance.x, player_instance.y)
            if new_bottle:
                bottles.append(new_bottle)

    clock.tick(settings.FPS)
pygame.quit()
