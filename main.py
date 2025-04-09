import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Test Game 1")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

myfont = pygame.font.Font("fonts/Roboto-Black.ttf", 40)
text_surface = myfont.render('timoshechka1', False, 'Red')

running = True
while running:
    screen.fill((172, 83, 219))
    pygame.draw.circle(screen, 'Red', (250, 150), 30)
    pygame.display.update()
    screen.blit(text_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
