import pygame
from data.backgrounds import Backgound as Back

class Plataform:
    def __init__(self, screen, nrImage,menuEsc, nivel):
        self.screen = screen
        # self.display = pygame.Surface((300,200))
        self.game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['0','0','0','0','0','2','2','2','0','0','2','2','2','0','0','0','0','0','0'],
                         ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                         ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
                         ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
                         ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                         ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
                         ]
        self.nivel = nivel
        self.background = Back(nrImage, menuEsc, nivel)
        self.plat_green = pygame.image.load("resources/image/platform/florest/p4.png").convert_alpha()
        self.plat_black = pygame.image.load("resources/image/platform/florest/p4_dark.png").convert_alpha()

    def settingPlataform(self):
        self.background.settingBackground(self.screen)
        tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(self.plat_black, (x*40, y*40))
                elif(tile == '2'):
                    self.screen.blit(self.plat_green, (x*40, y*40))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*38.6,y*36.9,40,59))
                x += 1
            y += 1
        return tile_rects
