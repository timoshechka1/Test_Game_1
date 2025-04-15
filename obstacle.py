import pygame
import settings
import random


class Obstacle:
    def __init__(self):
        """Инициализация препятствия со случайным внешним видом"""
        self.x = settings.SCREEN_WIDTH
        self.y = settings.OBSTACLE_START_Y
        self.speed = settings.OBSTACLE_SPEED

        # Загрузка всех вариантов изображений (как вы указали)
        self.images = [
            pygame.image.load(f"{settings.OBSTACLE_IMAGE_PATH}trash_{i}.png").convert_alpha()
            for i in range(1, settings.OBSTACLES_FRAMES + 1)
        ]

        # Выбираем случайное изображение при создании
        self.image = random.choice(self.images)
        image_rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect = pygame.Rect(
            image_rect.left + 15,
            image_rect.top + 15,
            image_rect.width - 30,
            image_rect.height - 30
        )

    def update(self):
        """Простое перемещение без анимации"""
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        """Отрисовка выбранного изображения"""
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

    def get_rect(self):
        return self.rect

    def is_off_screen(self):
        return self.rect.right < 0