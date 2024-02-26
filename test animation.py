import pygame
import sys


def frame(fnum, f_w, f_h, f_y):

    # this determines how big the singular animation parts will be
    # and then puts the places of each tile inside the sprite sheet provided in a list that is than returned

    returner = []   # returner creates a list containing every frame in the current row
    for j in range(7):
        liste = []

        if j == 2 or j == 3:
            fnum = 1

        elif j == 4:
            fnum = 14

        elif j == 5:
            fnum = 2

        elif j == 6:
            fnum = 6

        for i in range(fnum):   # goes through the number of images

            x = pygame.Rect(f_w * i, f_y * j, f_w, f_h)   # creates a rect, with x = width times pos, y = 0 and the width and height of the rects
            liste.append(x)

        returner.append(liste)

    return returner



def ftimer(time, fnow, fnum, lasttime):
# this looks if the time ist < 100 this determins the time every part of an animation uses
    fdelay = 100
    if time - lasttime > fdelay:
        fnow = (fnow + 1) % fnum
        lasttime = time
    return fnow, lasttime


def main():

    pygame.init()


    fnow = 0
    fnum = 7
    lasttime = 0

    f_w = 48
    f_h = 32
    f_y = 32

    a_num = 0

    WIDTH = 300
    HEIGHT = 300
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Animation Test")
    sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")


    frame_list = frame(fnum, f_w, f_h, f_y)
    print()
    while True:
        pressed_keys = pygame.key.get_pressed()

        time = pygame.time.get_ticks()

        screen.fill("black")
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pressed_keys[pygame.K_d] == True:
                fnum = 6
                a_num = 1

            if pressed_keys[pygame.K_a] == True:
                fnum = 6
                a_num = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fnum = 13
                    a_num = 4
                    fnow = 0

            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                a_num = 0
                fnum = 7
                fnow = 0

        fnow, lasttime = ftimer(time, fnow, fnum, lasttime)

        screen.blit(sprite_sheet, (150, 150), frame_list[a_num][fnow])
        pygame.display.update()


main()