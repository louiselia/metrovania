import pygame
import sys


def frame(fnum, f_w, f_h):

    # this determines how big the singular animation parts will be
    # and then puts the places of each tile inside the sprite sheet provided in a list that is than returned

    returner = []   # returner creates a list containing every frame in the current row
    for i in range(fnum):   # goes through the number of images
        x = pygame.Rect(f_w * i, 0, f_w, f_h)   # creates a rect, with x = width times pos, y = 0 and the width and height of the rects
        returner.append(x)

    return returner

fnum = 7
f_w = 48
f_h = 32

WIDTH = 300
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Animation Test")
sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")

frame_list = frame(fnum, f_w, f_h)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    screen.blit(sprite_sheet,(150, 150), frame_list[0])


    pygame.display.update()
