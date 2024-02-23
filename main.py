import pygame, sys, pytmx

class Character:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


player = Character("images/sprites/character/Characters/king.png", 100, 100)
def draw_character(self,screen):
    screen.blit(self.knight, (self.x, self.y))

def frame(fnum, f_w, f_h):
#   this determins how big the singular animation parts will be
#   and than puts the places of eacht tile inside of the spritesheet provided in a list wich is than returned

    returner = []
    for i in range(fnum):
        x = pygame.Rect(f_w * i, 0, f_w, f_h)
        returner.append(x)

    return returner

def ftimer(time, fnow, fnum):
#   this looks if the time ist < 100 this determins the time every part of an animation uses

    fdelay = 100
    lasttime = pygame.time.get_ticks()

    if time - lasttime < fdelay:
        fnow = (fnow +1) % fnum
        return time, fnow


def rect_drawer(screen, bg_y, color):
    test_rect = pygame.Rect(1200, 600, 2000, 300)
    test_rect.center = (bg_y, 900)
    pygame.draw.rect(screen, (color), test_rect)

def map_lister():
#   this takes every tile that is a instance(that means it will have to be drawn) and puts it in a list
#   every row has its own list inside of the map list

    map_data = pytmx.load_pygame('images/map/starting are/tiled/tsx/starting area.tmx')
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
    fnum = 3 # frame count
    fnow = 0 # frame the programm is currently on
    # sprite_sheet = pygame.image.load('images/sprites/spritesheet_animation_test.png')
    frames = frame(fnum, f_w, f_h)

    move_speed = 1
    bg_y = 0
    bg_x = 0

    #map zeugs
    map_list, map_data = map_lister() # gets two lists one withe the tiles in the rows and one with all the info from the given tmx file

#   player zeugs

    player = Character("images/sprites/character/Characters/king.png", 100, 100)


    while True:

        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:

                # left right input
                if event.key == pygame.K_d:
                    bg_x -= move_speed
                    print('pressed')

                if event.key == pygame.K_a:
                    bg_x += move_speed
                    print('pressed')


                # up down inputs
                if event.key == pygame.K_w:
                    bg_y -= move_speed
                    print('pressed')

                if event.key == pygame.K_s:
                    bg_y += move_speed
                    print('pressed')

        time, fnow = ftimer(time, fnow, fnum)


        screen.fill((0, 27, 35))

#       screen.blit(sprite_sheet, (100, 100), frames[fnow])

        map_drawer(screen, map_list, map_data, bg_x, bg_y)

        player.draw(screen)

        pygame.display.update()
        clock.tick(60)


main()
