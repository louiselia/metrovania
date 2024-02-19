import pygame, sys


pygame.init()


screen = pygame.display.set_mode((2000,1200))
pygame.display.set_caption('t-shirts')
clock = pygame.time.Clock()
pygame.key.set_repeat(1)

sprite_sheet = pygame.image.load('main code/images/sprites/spritesheet_animation_test.png')

bg_y = 1000

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_d:
                bg_y += 10
                print('pressed')

            if event.key == pygame.K_a:
                bg_y -= 10
                print('pressed')


    screen.fill('white')

#    pygame.Rect(x, y, w, h)

    test_rect = pygame.Rect(1200, 600, 2000, 300)
    test_rect.center = (bg_y, 900)
    pygame.draw.rect(screen, (0, 0, 0), test_rect)

    pygame.display.update()
    clock.tick(60)

