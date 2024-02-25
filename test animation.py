import pygame
import sys


def frame(fnum, f_w, f_h, f_y):

    # this determines how big the singular animation parts will be
    # and then puts the places of each tile inside the sprite sheet provided in a list that is than returned

    returner = []   # returner creates a list containing every frame in the current row
    for j in range(7):
        liste = []
        for i in range(fnum):   # goes through the number of images

            x = pygame.Rect(f_w * i, f_y * j, f_w, f_h)   # creates a rect, with x = width times pos, y = 0 and the width and height of the rects
            liste.append(x)

        returner.append(liste)

    return returner



def ftimer(time, fnow, fnum, lasttime):
# this looks if the time ist < 100 this determins the time every part of an animation uses
    fdelay = 100
    print(time)
    print(lasttime)
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
    f_y = 0


    WIDTH = 300
    HEIGHT = 300
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Animation Test")
    sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")

    frame_list = frame(fnum, f_w, f_h, f_y)

    while True:
        time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fnow, lasttime = ftimer(time, fnow, fnum, lasttime)

        screen.fill("black")

        screen.blit(sprite_sheet,(150, 150), frame_list[fnow[fnow]])

        pygame.display.update()

main()