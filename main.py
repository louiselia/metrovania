import pygame, sys, pytmx

def frame(fnum, f_w, f_h):
    returner = []
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
    #pygame.Rect(x, y, w, h)
    test_rect = pygame.Rect(1200, 600, 2000, 300)
    test_rect.center = (bg_y, 900)
    pygame.draw.rect(screen, (color), test_rect)

def map_lister():
    map_data = pytmx.load_pygame('images/map/starting are/tiled/starting_area.tmx')
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

    #frame zeugs
    f_h = 16
    f_w = 16
    fnum = 3
    fnow = 0
    sprite_sheet = pygame.image.load('images/sprites/spritesheet_animation_test.png')
    frames = frame(fnum, f_w, f_h)

    move_speed = 0
    bg_y = move_speed
    bg_x = move_speed

    #map zeugs
    map_list, map_data = map_lister()


    while True:

        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:

                # left right input
                if event.key == pygame.K_d:
                    bg_x -= 1
                    print('pressed')

                if event.key == pygame.K_a:
                    bg_x += 1
                    print('pressed')


                # up down inputs
                if event.key == pygame.K_w:
                    bg_y -= 1
                    print('pressed')

                if event.key == pygame.K_s:
                    bg_y += 1
                    print('pressed')

        time, fnow = ftimer(time, fnow, fnum)


        screen.fill('white')

        screen.blit(sprite_sheet, (100, 100), frames[fnow])

        map_drawer(screen, map_list, map_data, bg_x, bg_y)

        pygame.display.update()
        clock.tick(60)


main()
