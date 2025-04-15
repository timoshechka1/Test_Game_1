import pygame
import settings

class Enemy:
    def __init__(self):
        """Initializes the enemy with the initial parameters.

        Sets:
        - Start position (x, y) from settings
        - Movement speed (speed)
        - Loads animation frames
        - Initializes the animation counter
        - Creates a hitbox (rect) for collisions

        Attributes:
        x (int): Start X-coordinate from settings.ENEMY_START_X
        y (int): Start Y-coordinate from settings.ENEMY_START_Y
        speed (int): Movement speed from settings.ENEMY_SPEED
        frames (int): Number of animation frames from settings.ENEMY_ANIM_FRAMES
        moving (list): List of loaded Surfaces with animation frames
        anim_count (int): Current animation frame index (0..frames-1)
        rect (Rect): Enemy hitbox
        """
        self.x = settings.ENEMY_START_X
        self.y = settings.ENEMY_START_Y
        self.speed = settings.ENEMY_SPEED
        self.frames = settings.ENEMY_ANIM_FRAMES
        self.moving = [
            pygame.image.load(f"{settings.ENEMY_IMAGE_PATH}policeman_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)]
        self.anim_count = 0
        self.rect = self.moving[0].get_rect(topleft=(self.x, self.y))

    def update(self):
        """Updates the enemy state every frame.

        Does:
        1. Move the enemy left at the given speed
        2. Update the animation counter (looping)
        3. Update the hitbox position
        """
        self.x -= self.speed
        self.anim_count += 1
        if self.anim_count >= len(self.moving):
            self.anim_count = 0
        self.rect = self.moving[self.anim_count].get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        """Draws an enemy on the specified surface.

        Args:
        screen (pygame.Surface): Target surface to draw

        Note:
        Uses the current animation frame from self.anim_count
        """
        screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        """Returns the current enemy hitbox.

        Returns:
        pygame.Rect: Rectangle describing the current bounds of the enemy
        for collision handling
        """
        return self.rect

    def is_off_screen(self):
        """Checks if the enemy has left the screen boundaries on the left.

        Returns:
        bool: True if the enemy is completely hidden beyond the left border of the screen,
        False if still visible

        Note:
        Take into account the sprite width for an accurate check
        """
        return self.x < -self.rect.width