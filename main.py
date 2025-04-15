# Third party libraries
import pygame

# Local modules
import settings
import player
import enemy
import spawner
import bottle
import ui
import sound
import obstacle

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())

background = pygame.image.load(settings.BACKGROUND_IMAGE_PATH).convert_alpha()
background_x = 0
sound.play_background_music()

player_instance = player.Player()
enemies = []
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time())
enemies_killed = 0
enemy_icon = pygame.image.load(settings.ASSET_PATH + "policeman_icon.png").convert_alpha()
enemy_icon = pygame.transform.scale(enemy_icon, (50, 40))
obstacles = []
obstacle_timer = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer, spawner.get_random_spawn_time())
bottles = []

gameplay = True
running = True

while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))

    if gameplay:
        for obs in obstacles[:]:
            obs.update()
            obs.draw(screen)

            if obs.is_off_screen():
                obstacles.remove(obs)
            elif player_instance.get_rect().colliderect(obs.get_rect()):
                gameplay = False
                sound.stop_background_music()

        if enemies:
            for idx, en in enumerate(enemies):
                en.update()
                en.draw(screen)

                if en.is_off_screen():
                    enemies.pop(idx)
                elif player_instance.get_rect().colliderect(en.get_rect()):
                    gameplay = False
                    sound.stop_background_music()

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
                    enemies_killed += 1
                    break
    else:
        ui.draw_game_over(screen)

    ui.draw_enemy_counter(screen, enemies_killed, enemy_icon, gameplay)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not gameplay:
            if ui.is_restart_clicked(event.pos):
                gameplay = True
                player_instance.reset()
                enemies.clear()
                obstacles.clear()
                bottles.clear()
                sound.play_background_music()
                enemies_killed = 0

        if event.type == pygame.QUIT:
            running = False

        if event.type == enemy_timer and gameplay:
            enemies.append(enemy.Enemy())
            pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time())

        if event.type == obstacle_timer and gameplay:
            obstacles.append(obstacle.Obstacle())
            pygame.time.set_timer(obstacle_timer, spawner.get_random_spawn_time())

        if gameplay and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # Четкая проверка конкретной клавиши
                new_bottle = bottle.throw_bottle(player_instance.x, player_instance.y)
                if new_bottle:
                    bottles.append(new_bottle)

    clock.tick(settings.FPS)
pygame.quit()
