import pygame
import random

def platformP1(game_map,screen, scroll):
    # components [0] = dark
    # components [1] = floor
    # components [2] = midle grass
    # components [3] = 
    # components [4] = right side grass
    # components [5] = bottom left grass
    # components [6] = bottom midle grass
    # components [7] = bottom right grass
    components = [pygame.image.load('resources/image/platform/florest/tiles/'+str(i)+'.png') for i in range(9)]
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if (tile == '1'):
                screen.blit(components[0], (x*16-scroll[0], y*16-scroll[1]))
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            elif(tile == '2'):
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                screen.blit(components[1], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '3'):
                screen.blit(components[2], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '4'):
                screen.blit(components[3], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '5'):
                screen.blit(components[4], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '6'):
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                screen.blit(components[6], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '7'):
                screen.blit(components[7], (x*16-scroll[0], y*16-scroll[1]))
            elif(tile == '8'):
                screen.blit(components[8], (x*16-scroll[0], y*16-scroll[1]))
            # elif(tile == '9'):
            #     screen.blit(components[6], (x*16-scroll[0], y*16-scroll[1]))

            x += 1
        y += 1
    return tile_rects

def platformP2(game_map,screen, scroll):
    components = [pygame.image.load('resources/image/platform/pantano/tiles/'+str(i)+'.png').convert_alpha() for i in range(6)]
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if (tile == '1'):
                screen.blit(components[0], (x*30-scroll[0], y*30-scroll[1]))
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
            elif(tile == '2'):
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                screen.blit(components[1], (x*30-scroll[0], y*30-scroll[1]))
            elif(tile == '4'):
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                screen.blit(components[2], (x*30-scroll[0], y*30-scroll[1]))
            elif(tile == '3'):
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                screen.blit(components[4], (x*30-scroll[0], y*30-scroll[1]))
            elif(tile == '6'):
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                screen.blit(components[5], (x*30-scroll[0], y*30-scroll[1]))
            elif(tile == '5'):
                tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                screen.blit(components[3], (x*30-scroll[0], y*30-scroll[1]))
            x += 1
        y += 1
    return tile_rects

# def platformP1(game_map,screen, scroll):
#         tile_rects = []
#         y = 0
#         for layer in game_map:
#             x = 0
#             for tile in layer:
#                 if (tile == '1'):
#                     screen.blit(plat_black, (x*40-scroll[0], y*40-scroll[1]))
#                     tile_rects.append(pygame.Rect(x*40,y*40,40,40))
#                 elif(tile == '2'):
#                     tile_rects.append(pygame.Rect(x*40,y*40,40,40))
#                     screen.blit(plat_green, (x*40-scroll[0], y*40-scroll[1]))
#                 x += 1
#             y += 1
#         return tile_rects