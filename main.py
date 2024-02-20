import pygame, sys, pytmx

def frame(fnum, f_w, f_h):
    returner = [ ]
    for i in range(fnum):
        x = pygame.Rect(f_w * i, 0, f_w, f_h)
        returner.append(x)

    return returner
def ftimer(time, fnow, fnum):


    fdelay = 100
    lasttime = pygame.time.get_ticks()

    if time - lasttime < fdelay:
        fnow = (fnow +1) % fnum
        return time, fnow


def rect_drawer(screen, bg_y, color):
    #    pygame.Rect(x, y, w, h)
        test_rect = pygame.Rect(1200, 600, 2000, 300)
        test_rect.center = (bg_y, 900)
        pygame.draw.rect(screen, (color), test_rect)


def main():
    pygame.init()


    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('t-shirts')
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1)


    f_h = 16
    f_w = 16
    fnum = 3
    fnow = 0


    sprite_sheet = pygame.image.load('images/sprites/spritesheet_animation_test.png')

    map_data = pytmx.load_pygame('images/map/starting are/tiled/starting_area.tmx')
    map_list = []

    frames = frame(fnum, f_w, f_h)

    bg_y = 1000

    while True:
        time = pygame.time.get_ticks()

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

        time, fnow = ftimer(time, fnow, fnum)


        screen.fill('white')

        screen.blit(sprite_sheet, (100, 100), frames[fnow])

        rect_drawer(screen, bg_y, "pink")

        pygame.display.update()
        clock.tick(60)


main()
