import pygame
import sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Character Example")

sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")

class spritesheet:
    def __int__(self,filename, cols, rows):
        self.sheet = pygame.image.load(filename)
        self.cols = cols
        self.rows = rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeigt = self.rect.height / rows
        halfw = self.cellCenter = (w/2)
        halfh = self.cellCenter = (h/2)

        # self.cells = list([(index % cols * w, index / cols * h,w,h) for index in range(self.totalCellCount)]) wtf??????
        self.cells = []
        for index in range(self.totalCellCount):
            cell_x = index % cols * w
            cell_y = index // cols * h
            cell_width = w
            cell_height = h
            self.cells.append((cell_x, cell_y, cell_width, cell_height))

        self.handle = [(0, 0), (-halfw, 0), (-w, 0), (0, -halfh), (-halfw, -halfw), (-w, -halfh), (0, -h), (-halfw, -h), (-w, -h)]

    def draw(self,surface, cellindex, x, y, handle = 0):
        surface.blit(self.sheet,(x + self.handle[handle][0], y + self.handle[handle][1]),self.cells[cellindex])


class Character:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

player = Character("images/sprites/character/Characters/Knight_anin.png", 100, 100)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    player.draw(screen)
    pygame.display.update()


