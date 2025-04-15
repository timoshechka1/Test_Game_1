"""
OBSTACLE CLASS DOCUMENTATION

This class represents obstacle objects in the game that the player must avoid.
Obstacles spawn at the right edge of the screen and move left toward the player.
"""
import pygame
import settings
import random


class Obstacle:
    def __init__(self):
        """
        Initialize a new obstacle instance.

        Initialization Process:
        1. Sets starting position at right screen edge (SCREEN_WIDTH, OBSTACLE_START_Y)
        2. Loads animation frames from OBSTACLE_IMAGE_PATH
        3. Selects random image from available frames
        4. Creates collision rectangle slightly smaller than image bounds

        Attributes:
            x (int): Current x-position (updated each frame)
            y (int): Fixed y-position (from settings)
            speed (int): Movement speed (from settings)
            images (list): All loaded obstacle image surfaces
            image (pygame.Surface): Currently selected random image
            rect (pygame.Rect): Collision rectangle (smaller than visual image)
        """
        self.x = settings.SCREEN_WIDTH
        self.y = settings.OBSTACLE_START_Y
        self.speed = settings.OBSTACLE_SPEED

        # Load all obstacle animation frames
        self.images = [
            pygame.image.load(f"{settings.OBSTACLE_IMAGE_PATH}trash_{i}.png").convert_alpha()
            for i in range(1, settings.OBSTACLES_FRAMES + 1)
        ]

        # Select random image and set up collision rect
        self.image = random.choice(self.images)
        image_rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect = pygame.Rect(
            image_rect.left + 15, # Shrink rect for better gameplay feel
            image_rect.top + 15,
            image_rect.width - 30,
            image_rect.height - 30
        )

    def update(self):
        """
        Update obstacle's position each frame.

        Movement:
        - Moves left at constant speed (self.speed)
        - Updates collision rectangle position to match new x-position
        """
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        """
        Draw obstacle on the game screen.

        Args:
            screen (pygame.Surface): The game display surface

        Note:
            Draws at current (x,y) position without additional transformations
        """
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        """
        Get the obstacle's collision rectangle.

        Returns:
            pygame.Rect: The collision rectangle (smaller than visual image)
        """
        return self.rect

    def is_off_screen(self):
        """
        Check if obstacle has moved completely off left screen edge.

        Returns:
            bool: True if obstacle's right edge is past screen left boundary
                  False if still visible on screen

        Usage:
            Used to determine when obstacle can be removed from game
        """
        return self.rect.right < 0