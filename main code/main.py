import pygame, sys


pygame.init()


screen = pygame.display.set_mode((2000,1200))
pygame.display.set_caption('t-shirts')
clock = pygame.time.Clock()
bg_y = 0

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                bg_y += 1
                print('pressed')

            if event.key == pygame.K_a:
                bg_y -= 1
                print('pressed')




    pygame.display.update()
    clock.tick(60)

