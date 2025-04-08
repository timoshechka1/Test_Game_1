import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

running = True

while running:
    screen.fill((172, 83, 219))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
