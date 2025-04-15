import pygame
import settings
import time

class Bottle:
    def __init__(self, x, y):
        """
        Initialize a Bottle object with animation and movement properties.

        Args:
            x (int): Initial x-coordinate position of the bottle
            y (int): Initial y-coordinate position of the bottle

        Attributes:
            x (int): Current x-coordinate position
            y (int): Current y-coordinate position
            speed (int): Movement speed (pixels per frame) from settings.BOTTLE_SPEED
            frames (int): Number of animation frames from settings.BOTTLES_ANIM_FRAMES
            moving (list): List of loaded animation frames as pygame.Surface objects
            anim_count (int): Current animation frame index
            rect (pygame.Rect): Collision rectangle for the bottle
            creation_time (float): Time when bottle was created (in seconds since epoch)
            is_active (bool): Whether the bottle should be updated and drawn
        """
        self.x = x
        self.y = y
        self.speed = settings.BOTTLE_SPEED
        self.frames = settings.BOTTLES_ANIM_FRAMES
        self.moving = [
            pygame.image.load(f"{settings.BOTTLE_IMAGE_PATH}bottle_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)]
        self.anim_count = 0
        self.rect = self.moving[0].get_rect(topleft=(self.x, self.y))
        self.creation_time = time.time()
        self.is_active = True

    def update(self):
        """
        Update the bottle's position and animation state.

        Handles:
        - Movement based on speed
        - Animation frame progression
        - Lifetime expiration check
        - Updates collision rectangle position

        The bottle will deactivate itself if its lifetime (settings.BOTTLE_LIFETIME)
        has expired.
        """
        if not self.is_active:
            return

        self.x += self.speed
        self.rect.x = self.x
        self.anim_count = (self.anim_count + 1) % len(self.moving)

        if time.time() - self.creation_time > settings.BOTTLE_LIFETIME:
            self.is_active = False

    def draw(self, screen):
        """
        Draw the bottle on the specified surface if it's active.

        Args:
            screen (pygame.Surface): The surface to draw the bottle on

        Only draws if:
        - The bottle is active (self.is_active == True)
        - Animation frames are loaded (self.moving is not empty)
        """
        if self.is_active and self.moving:
            screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        """
        Get the bottle's collision rectangle.

        Returns:
            pygame.Rect: The current collision rectangle of the bottle
        """
        return self.rect

    def is_off_screen(self):
        """
        Check if the bottle has moved outside the screen boundaries.

        Returns:
            bool: True if the bottle is completely off-screen (left or right),
                  False otherwise
        """
        return self.x > settings.SCREEN_WIDTH or self.x < -self.rect.width

# Module-level variable for cooldown tracking
_last_throw_time = 0

def throw_bottle(player_x, player_y):
    """
    Create a new Bottle object if cooldown period has passed.

    Args:
        player_x (int): x-coordinate of player position
        player_y (int): y-coordinate of player position

    Returns:
        Bottle or None: New Bottle object if cooldown has passed,
                       None if still in cooldown

    Uses settings.BOTTLE_COOLDOWN to determine minimum time between throws.
    Bottles are created offset from player position (+50px in both axes).
    """
    global _last_throw_time
    now = time.time()
    if now - _last_throw_time < settings.BOTTLE_COOLDOWN:
        return None
    _last_throw_time = now
    return Bottle(player_x + 50, player_y + 50)