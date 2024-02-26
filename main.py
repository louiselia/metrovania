import pygame, sys, pytmx

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

    f_w = 48
    f_h = 32
    f_y = 32

    a_num = 0
    #frame zeugs

    fnum = 3 # frame count
    fnow = 0 # frame the programm is currently on

    move_speed = 1
    bg_y = 0
    bg_x = 0

    #map zeugs
    map_list, map_data = map_lister('images/map/starting are/tiled/tsx/starting area.tmx') # gets two lists one withe the tiles in the rows and one with all the info from the given tmx file

    frame_list = frame(fnum, f_w, f_h, f_y)

    sprite_sheet = pygame.image.load("images/sprites/character/Characters/Knight_anin.png")

#   player zeugs

#    player = Character("images/sprites/character/Characters/king.png", screen.get_width() / 4, screen.get_height() / 4 * 3)


    while True:

        pressed_keys = pygame.key.get_pressed()
        time = pygame.time.get_ticks()

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

            #fnow, lasttime = ftimer(time, fnow, fnum, lasttime)

            map_drawer(screen, map_list, map_data, bg_x, bg_y)
            screen.blit(sprite_sheet, (150, 150), frame_list[a_num][fnow])


        fnow, lasttime = ftimer(time, fnow, fnum, lasttime)




        pygame.display.update()
        clock.tick(60)


main()
