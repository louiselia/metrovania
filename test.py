import pygame
import sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Character Example")




class Character:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


player = Character("images/sprites/character/Characters/king.png", 100, 100)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.x -= 10
            elif event.key == K_RIGHT:
                player.x += 10
            elif event.key == K_UP:
                player.y -= 10
            elif event.key == K_DOWN:
                player.y += 10

    player.draw(screen)
    pygame.display.update()

