import pygame, sys

pygame.init()

black = 0, 0, 0
red = 255, 0, 0
green = 0, 128, 0
blue = 0, 0, 255

colors = [black, red, green, blue]
i = 0
screen = pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            i = (i + 1) % 4
            screen.fill(colors[i])
    pygame.display.update()

