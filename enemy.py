import pygame
import settings

class Enemy:
    def __init__(self):
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
        self.x -= self.speed
        self.anim_count += 1
        if self.anim_count >= len(self.moving):
            self.anim_count = 0
        self.rect = self.moving[self.anim_count].get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        return self.rect

    def is_off_screen(self):
        return self.x < -self.rect.width