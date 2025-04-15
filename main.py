"""
MAIN GAME LOOP DOCUMENTATION

This module contains the core game loop and initialization logic for 'Test Game 1'.
It manages game state, player input, object spawning, collision detection, and rendering.
"""
# Third party libraries
import pygame # Main game engine for graphics, input, and sound

# Local modules
import settings  # Game configuration constants (screen size, paths, etc.)
import player    # Player character logic and rendering
import enemy     # Enemy behavior and rendering
import spawner   # Random spawn timing for game objects
import bottle    # Projectile (bottle) physics and rendering
import ui        # User interface elements (score, game over screen)
import sound     # Audio management (background music, sound effects)
import obstacle  # Obstacle behavior and rendering

# Initialize game clock for controlling frame rate
clock = pygame.time.Clock()

# Pygame initialization and screen setup
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())

# Game background setup (parallax scrolling)
background = pygame.image.load(settings.BACKGROUND_IMAGE_PATH).convert_alpha()
background_x = 0 # Tracks background scroll position
sound.play_background_music() # Start background music

# Player initialization
player_instance = player.Player() # Main player character

# Enemy management
enemies = [] # Active enemies list
enemy_timer = pygame.USEREVENT + 1 # Custom event for enemy spawning
pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time()) # Set first spawn
enemies_killed = 0 # Score tracking
enemy_icon = pygame.image.load(settings.ASSET_PATH + "policeman_icon.png").convert_alpha()
enemy_icon = pygame.transform.scale(enemy_icon, (50, 40)) # Score display icon

# Obstacle management
obstacles = [] # Active obstacles list
obstacle_timer = pygame.USEREVENT + 2 # Custom event for obstacle spawning
pygame.time.set_timer(obstacle_timer, spawner.get_random_spawn_time())

# Projectile management
bottles = [] # Active bottles list

# Game state flags
gameplay = True  # True during active gameplay, False when game over
running = True   # Main loop control flag

# MAIN GAME LOOP
while running:
    # Render scrolling background (two copies for seamless scrolling)
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))

    if gameplay:
        # Update and draw all obstacles
        for obs in obstacles[:]: # Iterate over copy for safe modification
            obs.update()
            obs.draw(screen)

            # Remove off-screen obstacles or end game on collision
            if obs.is_off_screen():
                obstacles.remove(obs)
            elif player_instance.get_rect().colliderect(obs.get_rect()):
                gameplay = False
                sound.stop_background_music()

        # Update and draw all enemies
        if enemies:
            for idx, en in enumerate(enemies):
                en.update()
                en.draw(screen)

                # Remove off-screen enemies or end game on collision
                if en.is_off_screen():
                    enemies.pop(idx)
                elif player_instance.get_rect().colliderect(en.get_rect()):
                    gameplay = False
                    sound.stop_background_music()

        # Player input handling
        keys = pygame.key.get_pressed()
        player_rect = player_instance.get_rect()
        player_instance.draw(screen)

        # Movement controls
        if keys[pygame.K_LEFT]:
            player_instance.move_left()
        else:
            player_instance.move_right()

        if keys[pygame.K_SPACE]:
            player_instance.jump()

        player_instance.update() # Update player physics

        # Boundary checking for player movement
        if keys[pygame.K_LEFT] and player_instance.x > settings.PLAYER_MOVE_LIMIT_LEFT:
            player_instance.x -= player_instance.speed
        elif keys[pygame.K_RIGHT] and player_instance.x < settings.PLAYER_MOVE_LIMIT_RIGHT:
            player_instance.x += player_instance.speed

        # Background scrolling logic
        background_x -= 5
        if background_x == -600: # Reset position for seamless looping
            background_x = 0

        # Update and draw all bottles
        for b in bottles[:]:
            b.update()
            b.draw(screen)

            # Remove inactive or off-screen bottles
            if not b.is_active or b.is_off_screen():
                bottles.remove(b)
                continue

            # Check for bottle-enemy collisions
            for e in enemies[:]:
                if b.get_rect().colliderect(e.get_rect()):
                    enemies.remove(e)
                    bottles.remove(b)
                    enemies_killed += 1
                    break
    else:
        # Game over state - show game over screen
        ui.draw_game_over(screen)

    # Draw UI elements (score counter)
    ui.draw_enemy_counter(screen, enemies_killed, enemy_icon, gameplay)
    pygame.display.update() # Update display

    # Event handling
    for event in pygame.event.get():
        # Restart game when clicked on game over screen
        if event.type == pygame.MOUSEBUTTONDOWN and not gameplay:
            if ui.is_restart_clicked(event.pos):
                gameplay = True
                player_instance.reset()
                enemies.clear()
                obstacles.clear()
                bottles.clear()
                sound.play_background_music()
                enemies_killed = 0

        # Quit game when window is closed
        if event.type == pygame.QUIT:
            running = False

        # Spawn new enemy when timer triggers
        if event.type == enemy_timer and gameplay:
            enemies.append(enemy.Enemy())
            pygame.time.set_timer(enemy_timer, spawner.get_random_spawn_time())

        # Spawn new obstacle when timer triggers
        if event.type == obstacle_timer and gameplay:
            obstacles.append(obstacle.Obstacle())
            pygame.time.set_timer(obstacle_timer, spawner.get_random_spawn_time())

        # Throw bottle when 'B' key is pressed
        if gameplay and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                new_bottle = bottle.throw_bottle(player_instance.x, player_instance.y)
                if new_bottle:
                    bottles.append(new_bottle)

    # Maintain consistent frame rate
    clock.tick(settings.FPS)

# Clean up pygame when game ends
pygame.quit()
