"""
BOTTLE MODULE DOCUMENTATION

This module implements the bottle projectile system, including:
- Bottle class for projectile behavior and rendering
- Global throw_bottle function for creating new projectiles
"""
import pygame
import settings
import time

class Bottle:
    """A throwable projectile that moves horizontally across the screen.

    Attributes:
        x (int): Current x-position of the bottle
        y (int): Current y-position of the bottle
        speed (int): Movement speed in pixels per frame
        frames (int): Number of animation frames
        moving (list): Loaded animation frame surfaces
        anim_count (int): Current animation frame index
        rect (pygame.Rect): Collision rectangle
        creation_time (float): Timestamp when bottle was created
        is_active (bool): Whether the bottle should be updated/drawn
    """
    def __init__(self, x, y):
        """Initialize a new bottle projectile.

        Args:
            x (int): Starting x-position
            y (int): Starting y-position

        Initialization:
            - Sets position and speed from parameters/settings
            - Loads all animation frames
            - Sets up animation system
            - Creates collision rectangle
            - Records creation time
            - Marks as active
        """
        self.x = x
        self.y = y
        self.speed = settings.BOTTLE_SPEED
        self.frames = settings.BOTTLES_ANIM_FRAMES

        # Load all animation frames
        self.moving = [
            pygame.image.load(f"{settings.BOTTLE_IMAGE_PATH}bottle_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)
        ]

        self.anim_count = 0
        self.rect = self.moving[0].get_rect(topleft=(self.x, self.y))
        self.creation_time = time.time()
        self.is_active = True

    def update(self):
        """Update bottle state each frame.

        Behavior:
            - Only updates if bottle is active
            - Moves horizontally at constant speed
            - Advances animation frame
            - Checks lifetime expiration
            - Updates collision rectangle position
        """
        if not self.is_active:
            return

        self.x += self.speed
        self.rect.x = self.x
        self.anim_count = (self.anim_count + 1) % len(self.moving)

        if time.time() - self.creation_time > settings.BOTTLE_LIFETIME:
            self.is_active = False

    def draw(self, screen):
        """Draw the bottle on screen.

        Args:
            screen (pygame.Surface): The game display surface

        Notes:
            - Only draws if bottle is active
            - Uses current animation frame
        """
        if self.is_active and self.moving:
            screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        """Get the bottle's collision rectangle.

        Returns:
            pygame.Rect: Current collision rectangle
        """
        return self.rect

    def is_off_screen(self):
        """Check if bottle has left the screen boundaries.

        Returns:
            bool: True if completely off left or right screen edge
        """
        return self.x > settings.SCREEN_WIDTH or self.x < -self.rect.width

# Bottle throwing cooldown tracking
_last_throw_time = 0 # Timestamp of last throw

def throw_bottle(player_x, player_y):
    """Create a new bottle projectile if cooldown has expired.

    Args:
        player_x (int): Player's current x-position
        player_y (int): Player's current y-position

    Returns:
        Bottle: New bottle instance if cooldown expired
        None: If still in cooldown period

    Behavior:
        - Checks time since last throw against BOTTLE_COOLDOWN
        - Creates bottle offset from player position
        - Updates last throw time on success
    """
    global _last_throw_time
    now = time.time()
    if now - _last_throw_time < settings.BOTTLE_COOLDOWN:
        return None
    _last_throw_time = now
    return Bottle(player_x + 50, player_y + 50)