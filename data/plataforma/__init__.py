import pygame
from data.backgrounds import Backgound as Back

class Plataform:
    def __init__(self, screen, nrImage,menuEsc, nivel):
        self.screen = screen
        # self.display = pygame.Surface((300,200))
        self.game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
                         ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
                         ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                         ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
                         ]
        self.nivel = nivel
        self.background = Back(nrImage, menuEsc, nivel)
        self.plat_green = pygame.image.load("resources/image/platform/florest/p2.png").convert_alpha()
        self.plat_black = pygame.image.load("resources/image/platform/florest/p2_dwon.png").convert_alpha()

    def settingPlataform(self):
        self.background.settingBackground(self.screen)
        tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if (tile == '1'):
                    self.screen.blit(self.plat_black, (x*217, y*33))
                elif(tile == '2'):
                    self.screen.blit(self.plat_green, (x*217, y*33))
                x += 1
            y += 1
        return tile_rects
