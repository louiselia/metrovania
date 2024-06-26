import pygame, sys, pytmx
from Player import Player

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


def map_lister(tmxfile):
#
#   this takes every tile that is a instance(that means it will have to be drawn) and puts it in a list
#   every row has its own list inside of the map list

    map_data = pytmx.load_pygame(tmxfile)
    map_list = []
    for row in map_data.visible_layers:
        if isinstance(row, pytmx.TiledTileLayer):
            map_list.append(row)

    return map_list, map_data

def map_drawer(surface, map_list, map_data, inputw, inputh):
    upsizefaktorw, upsizefaktorh = surface.get_width() / 256, surface.get_height() / 192


    for layer in map_list:
        for x, y, gid in layer:
            tile =  map_data.get_tile_image_by_gid(gid)
            if tile:
                tile = pygame.transform.scale(tile, (map_data.tilewidth * upsizefaktorw, map_data.tileheight * upsizefaktorh))
                surface.blit(tile, (x * upsizefaktorw * map_data.tilewidth + inputw, y * upsizefaktorh * map_data.tileheight + inputh))



def main():

    pygame.init()


    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Metrovania')
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1)

    fnow = 0
    fnum = 7
    lasttime = 0

    upsizefactor = 4

    f_w = 48 * upsizefactor
    f_h = 32 * upsizefactor
    f_y = 32 * upsizefactor

    a_num = 0


    bg_y = 0
    bg_x = 0

    #map zeugs
    map_list, map_data = map_lister('images/map/starting are/tiled/tsx/starting area.tmx') # gets two lists one withe the tiles in the rows and one with all the info from the given tmx file

    frame_list = frame(fnum, f_w, f_h, f_y)

    sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")
    sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * upsizefactor, sprite_sheet.get_height() * upsizefactor))

    player = Player(screen.get_width() * 0.25,  screen.get_height() * 0.75)

    while True:

        screen.fill((0, 27, 35))

        pressed_keys = pygame.key.get_pressed()
        time = pygame.time.get_ticks()

        dt = clock.tick(60) * 0.001 * 60

        player.update(dt)

        player.RIGHT_KEY = False
        player.LEFT_KEY = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if pressed_keys[pygame.K_d] == True:
                    player.RIGHT_KEY = True
                    fnum = 6
                    a_num = 1

                if pressed_keys[pygame.K_a] == True:
                    player.LEFT_KEY = True
                    fnum = 6
                    a_num = 1

                if pressed_keys[pygame.K_SPACE] == True:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_SPACE:
                        player.velocity.y *= .25
                        player.is_jumping = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fnum = 13
                    a_num = 4
                    fnow = 0

            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                a_num = 0
                fnum = 7
                fnow = 0




        map_drawer(screen, map_list, map_data, player.position.x - screen.get_width(), bg_y)

        fnow, lasttime = ftimer(time, fnow, fnum, lasttime)

        current_frame = frame_list[a_num][fnow]

        screen.blit(sprite_sheet, (player.x, player.y), current_frame)
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()

