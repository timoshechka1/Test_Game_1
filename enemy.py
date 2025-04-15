"""
ENEMY CLASS DOCUMENTATION

This class represents enemy entities in the game that move toward the player.
Enemies feature animated movement and collision detection.
"""
import pygame
import settings

class Enemy:
    def __init__(self):
        """
        Initialize a new enemy instance.

        Initialization Process:
        1. Sets starting position from settings (ENEMY_START_X, ENEMY_START_Y)
        2. Configures movement speed from settings
        3. Loads animation frames from ENEMY_IMAGE_PATH
        4. Sets up animation system
        5. Creates initial collision rectangle

        Attributes:
            x (int): Current x-position (updated each frame)
            y (int): Fixed y-position (from settings)
            speed (int): Movement speed (from settings.ENEMY_SPEED)
            frames (int): Number of animation frames (from settings.ENEMY_ANIM_FRAMES)
            moving (list): Animation frame surfaces
            anim_count (int): Current animation frame index
            rect (pygame.Rect): Collision rectangle (updated each frame)
        """
        self.x = settings.ENEMY_START_X
        self.y = settings.ENEMY_START_Y
        self.speed = settings.ENEMY_SPEED
        self.frames = settings.ENEMY_ANIM_FRAMES
        self.moving = [
            pygame.image.load(f"{settings.ENEMY_IMAGE_PATH}policeman_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)
        ]

        self.anim_count = 0
        self.rect = self.moving[0].get_rect(topleft=(self.x, self.y))

    def update(self):
        """
        Update enemy state each frame.

        Performs:
        1. Movement: Moves left at constant speed
        2. Animation: Cycles through animation frames
        3. Collision: Updates collision rectangle position

        Animation Logic:
        - Advances anim_count each frame
        - Loops back to 0 when reaching last frame
        - Updates rect to match current frame and position
        """
        self.x -= self.speed
        self.anim_count += 1
        if self.anim_count >= len(self.moving):
            self.anim_count = 0
        self.rect = self.moving[self.anim_count].get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        """
        Render the enemy on screen.

        Args:
            screen (pygame.Surface): The game display surface

        Rendering:
        - Uses current animation frame (moving[anim_count])
        - Draws at current (x,y) position
        - No additional transformations applied
        """
        screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        """
        Get the enemy's collision rectangle.

        Returns:
            pygame.Rect: The current collision rectangle
                         (matches current frame and position)

        Note:
            Rectangle is updated each frame in update() method
        """
        return self.rect

    def is_off_screen(self):
        """
        Check if enemy has moved completely off left screen edge.

        Returns:
            bool: True if enemy's right edge is past screen left boundary
                  False if still visible on screen

        Calculation:
        Checks if x-position plus width is less than 0
        (entire sprite is left of screen)
        """
        return self.x < -self.rect.width