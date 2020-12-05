import pygame
from data.backgrounds import Backgound as Back
from data.enimy.cactus import Cactus

class Plataform:
    def __init__(self, screen, nrImage,menuEsc, nivel):
        self.screen = screen
        # self.display = pygame.Surface((300,200))
        self.game_map = self.load_map('map')
        self.nivel = nivel
        self.background = Back(nrImage, menuEsc, nivel)
        self.plat_green = pygame.image.load("resources/image/platform/florest/p4.png").convert_alpha()
        self.plat_black = pygame.image.load("resources/image/platform/florest/p4_dark.png").convert_alpha()
        self.cactu = pygame.image.load("resources/image/platform/florest/Cactus-1.png").convert_alpha()

    def load_map(self, fileName):
        file = open('data/plataforma/'+fileName + '.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    def settingPlataform(self, scroll):
        self.background.settingBackground(self.screen)
        tile_rects = []
        cactus_mask = []
        y = 0
        # control = 1
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(self.plat_black, (x*40-scroll[0], y*40-scroll[1]))
                elif(tile == '2'):
                    self.screen.blit(self.plat_green, (x*40-scroll[0], y*40-scroll[1]))
                elif(tile == '3'):
                    self.screen.blit(self.cactu, (x*50-scroll[0], y*39-scroll[1]))
                    cactus_mask.append(pygame.mask.from_surface(self.cactu))
                if ((tile == '2')or(tile == '1')):
                    tile_rects.append(pygame.Rect(x*40,y*40,40,40))
                    
                x += 1
            y += 1
            # control += 1
        return tile_rects, cactus_mask