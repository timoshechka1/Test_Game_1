import pygame
import settings
import time

class Bottle:
    def __init__(self, x, y):
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
        if not self.is_active:
            return

        self.x += self.speed
        self.rect.x = self.x
        self.anim_count = (self.anim_count + 1) % len(self.moving)

        if time.time() - self.creation_time > settings.BOTTLE_LIFETIME:
            self.is_active = False

    def draw(self, screen):
        if self.is_active and self.moving:
            screen.blit(self.moving[self.anim_count], (self.x, self.y))

    def get_rect(self):
        return self.rect

    def is_off_screen(self):
        return self.x > settings.SCREEN_WIDTH or self.x < -self.rect.width

_last_throw_time = 0

def throw_bottle(player_x, player_y):
    global _last_throw_time
    now = time.time()
    if now - _last_throw_time < settings.BOTTLE_COOLDOWN:
        return None
    _last_throw_time = now
    return Bottle(player_x + 50, player_y + 50)