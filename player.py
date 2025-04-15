"""
PLAYER CLASS DOCUMENTATION

This class implements the player character with:
- Movement controls (left/right)
- Jump mechanics with parabolic trajectory
- Animation system for both directions
- Collision detection
"""
import pygame
import settings

class Player:
    """The main player character with movement and animation capabilities.

    Attributes:
        x (int): Current x-position
        y (int): Current y-position
        frames (int): Number of animation frames
        speed (int): Horizontal movement speed
        is_jump (bool): Jump state flag
        jump_count (int): Current jump progress counter
        jump_direction_x (int): Horizontal jump direction (+right/-left)
        moving_left (list): Left-facing animation frames
        moving_right (list): Right-facing animation frames
        anim_count (int): Current animation frame index
        direction (str): Facing direction ('left'/'right')
        rect (pygame.Rect): Collision rectangle (smaller than sprite)
    """
    def __init__(self):
        """Initialize player with default position and loaded assets.

        Initializes:
        - Starting position from settings
        - Movement parameters
        - Animation frames for both directions
        - Jump system
        - Collision rectangle
        """
        self.x = settings.PLAYER_START_X
        self.y = settings.PLAYER_START_Y
        self.frames = settings.PLAYER_ANIM_FRAMES
        self.speed = settings.PLAYER_SPEED
        self.is_jump = False
        self.jump_count = settings.PLAYER_JUMP_COUNT
        self.jump_direction_x = 0

        # Load animation frames
        self.moving_left = [
            pygame.image.load(f"{settings.PLAYER_LEFT_PATH}player_movement_left_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)
        ]
        self.moving_right = [
            pygame.image.load(f"{settings.PLAYER_RIGHT_PATH}player_movement_right_{i}.png").convert_alpha()
            for i in range(1, self.frames + 1)
        ]

        self.anim_count = 0
        self.direction = "right"
        self.rect = self.moving_right[0].get_rect(topleft=(self.x, self.y))

    def move_right(self):
        """Initiate rightward movement.

        Effects:
            - Increases x-position within movement bounds
            - Sets facing direction to right
            - Respects PLAYER_MOVE_LIMIT_LEFT boundary
        """
        if self.x < settings.PLAYER_MOVE_LIMIT_LEFT:
            self.x += self.speed
        self.direction = "right"

    def move_left(self):
        """Initiate leftward movement.

        Effects:
            - Decreases x-position within movement bounds
            - Sets facing direction to left
            - Respects PLAYER_MOVE_LIMIT_RIGHT boundary
        """
        if self.x > settings.PLAYER_MOVE_LIMIT_RIGHT:
            self.x -= self.speed
        self.direction = "left"

    def get_current_image(self):
        """Get the current animation frame based on direction.

        Returns:
            pygame.Surface: Current animation frame surface
        """
        if self.direction == 'left':
            return self.moving_left[self.anim_count]
        else:
            return self.moving_right[self.anim_count]

    def jump(self):
        """Initiate jump if not already jumping.

        Sets up:
            - Jump state flag
            - Horizontal jump direction based on facing
            - Uses quadratic function for jump arc
        """
        if not self.is_jump:
            self.is_jump = True

            if self.direction == "right":
                self.jump_direction_x = 3
            else:
                self.jump_direction_x = -3

    def update(self):
        """Update player state each frame.

        Handles:
            - Animation frame progression
            - Jump physics (parabolic trajectory)
            - Movement boundaries during jump
            - Collision rectangle updates
        """
        # Advance animation
        self.anim_count = (self.anim_count + 1) % len(self.moving_right)

        # Jump mechanics
        if self.is_jump:
            if self.jump_count >= -5:
                # Vertical movement (quadratic curve)
                if self.jump_count > 0:
                    self.y -= (self.jump_count ** 2)
                else:
                    self.y += (self.jump_count ** 2)

                # Horizontal movement with boundary check
                new_x = self.x + self.jump_direction_x
                if settings.PLAYER_MOVE_LIMIT_LEFT <= new_x <= settings.PLAYER_MOVE_LIMIT_RIGHT:
                    self.x = new_x
                self.jump_count -= 1
            else:
                # Reset jump state
                self.is_jump = False
                self.jump_count = settings.PLAYER_JUMP_COUNT
                self.jump_direction_x = 0

        # Update collision rect (smaller than sprite)
        image_rect = self.get_current_image().get_rect(topleft=(self.x, self.y))

        self.rect = pygame.Rect(
            image_rect.left + 25,  # Left padding
            image_rect.top + 15,   # Top padding
            image_rect.width - 50,  # Width reduction
            image_rect.height - 30  # Height reduction
        )

    def draw(self, screen):
        """Draw player on screen.

        Args:
            screen (pygame.Surface): Target surface for rendering
        """
        current_image = self.get_current_image()
        screen.blit(current_image, (self.x, self.y))

    def reset(self):
        """Reset player to initial state.

        Resets:
            - Position to starting coordinates
            - Jump state
            - Animation frame
            - Facing direction
            - Collision rectangle
        """
        self.x = settings.PLAYER_START_X
        self.y = settings.PLAYER_START_Y
        self.is_jump = False
        self.jump_count = settings.PLAYER_JUMP_COUNT
        self.anim_count = 0
        self.direction = "right"
        image_rect = self.get_current_image().get_rect(topleft=(self.x, self.y))

        # Recalculate collision rect
        self.rect = pygame.Rect(
            image_rect.left + 25,
            image_rect.top + 15,
            image_rect.width - 50,
            image_rect.height - 30
        )

    def get_rect(self):
        """Get current collision rectangle.

        Returns:
            pygame.Rect: Current collision bounds
        """
        return self.rect