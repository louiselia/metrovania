import pygame
import sys

class Player(pygame.sprite.sprite):



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Test Animation")

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites = add(player)

loop = True
while loop:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   sys.exit()
 screen.fill((255,255,255))
 moving_sprites.draw(screen)
 pygame.display.flip()
 clock.tick(60)

