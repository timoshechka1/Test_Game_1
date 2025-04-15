import pygame
import settings

class Player:
    def __init__(self):
        """Initializes the player character with the initial parameters.

        Loads all necessary resources and sets the initial state:
        - Position (x, y) from settings
        - Movement parameters (speed, jump)
        - Left/right movement animations
        - Hitbox (rect) for collisions

        Attributes:
        x (int): Starting X-coordinate from settings.PLAYER_START_X
        y (int): Starting Y-coordinate from settings.PLAYER_START_Y
        speed (int): Movement speed from settings.PLAYER_SPEED
        is_jump (bool): Jump state flag (False by default)
        jump_count (int): Jump counter from settings.PLAYER_JUMP_COUNT
        moving_left (list[Surface]): List of left movement sprites
        moving_right (list[Surface]): List of movement sprites right
        anim_count (int): Animation frame counter
        direction (str): Current direction ('right'/'left')
        rect (Rect): Character hitbox at starting position
        """
        self.x = settings.PLAYER_START_X
        self.y = settings.PLAYER_START_Y
        self.frames = settings.PLAYER_ANIM_FRAMES
        self.speed = settings.PLAYER_SPEED
        self.is_jump = False
        self.jump_count = settings.PLAYER_JUMP_COUNT
        self.jump_direction_x = 0
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
        """Moves the character to the right, taking into account the movement limits.

        Increases the X coordinate by the speed value if the left limit (PLAYER_MOVE_LIMIT_LEFT) has not been reached.
        Updates the view direction.
        """
        if self.x < settings.PLAYER_MOVE_LIMIT_LEFT:
            self.x += self.speed
        self.direction = "right"

    def move_left(self):
        """Moves the character to the left, taking into account the movement limits.

        Decreases the X coordinate by the speed value if the right limit (PLAYER_MOVE_LIMIT_RIGHT) is not reached.
        Updates the view direction.
        """
        if self.x > settings.PLAYER_MOVE_LIMIT_RIGHT:
            self.x -= self.speed
        self.direction = "left"

    def get_current_image(self):
        """Returns the current character sprite based on the direction.

        Returns:
        Surface: The current animation frame for the corresponding direction of movement.
        """
        if self.direction == 'left':
            return self.moving_left[self.anim_count]
        else:
            return self.moving_right[self.anim_count]

    def jump(self):
        """Triggers the character to jump if it is not in the jump state.

        Sets the is_jump flag to True, which triggers the jump physics
        in the update() method.
        """
        if not self.is_jump:
            self.is_jump = True
            # Задаём направление прыжка в зависимости от текущего направления
            if self.direction == "right":
                self.jump_direction_x = 3  # подбери значение (1–3)
            else:
                self.jump_direction_x = -3

    def update(self):
        """Updates the character state every frame.

        Performs:
        1. Cyclic update of the animation counter
        2. Processing the jump physics (parabolic trajectory)
        3. Update the character's hitbox
        """
        self.anim_count = (self.anim_count + 1) % len(self.moving_right)

        if self.is_jump:
            if self.jump_count >= -5:
                if self.jump_count > 0:
                    self.y -= (self.jump_count ** 2)
                else:
                    self.y += (self.jump_count ** 2)
                # ➕ Добавляем движение по X во время прыжка
                new_x = self.x + self.jump_direction_x
                if settings.PLAYER_MOVE_LIMIT_LEFT <= new_x <= settings.PLAYER_MOVE_LIMIT_RIGHT:
                    self.x = new_x
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = settings.PLAYER_JUMP_COUNT
                self.jump_direction_x = 0  # сброс

        image_rect = self.get_current_image().get_rect(topleft=(self.x, self.y))
        # Уменьшаем хитбокс — например, на 10 пикселей по ширине и 10 по высоте
        self.rect = pygame.Rect(
            image_rect.left + 25,
            image_rect.top + 15,
            image_rect.width - 50,
            image_rect.height - 30
        )

    def draw(self, screen):
        """Draws a character on the specified surface.

        Args:
        screen (pygame.Surface): Surface to draw on (usually the game screen)

        Actions:
        1. Gets the current character sprite
        2. Draws the sprite on the surface at position (self.x, self.y)
        """
        current_image = self.get_current_image()
        screen.blit(current_image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

    def reset(self):
        """Resets the character state to its initial values.

        Restores:
        - Position (x, y) from settings
        - Jump parameters
        - Animation counter
        - View direction
        - Hitbox (rect)
        """
        self.x = settings.PLAYER_START_X
        self.y = settings.PLAYER_START_Y
        self.is_jump = False
        self.jump_count = settings.PLAYER_JUMP_COUNT
        self.anim_count = 0
        self.direction = "right"
        image_rect = self.get_current_image().get_rect(topleft=(self.x, self.y))
        # Уменьшаем хитбокс — например, на 10 пикселей по ширине и 10 по высоте
        self.rect = pygame.Rect(
            image_rect.left + 25,
            image_rect.top + 15,
            image_rect.width - 50,
            image_rect.height - 30
        )

    def get_rect(self):
        """Returns the current hitbox of the character for collision handling.

        Returns:
        pygame.Rect: Rectangle describing the current position and size of the character
        """
        return self.rect

