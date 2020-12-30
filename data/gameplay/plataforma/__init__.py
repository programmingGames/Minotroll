import pygame
from data.backgrounds import Backgound as Back
from data.gameplay.enimy.cactus import Cactus

class Plataform:
    def __init__(self, screen):
        self.screen = screen
        # self.display = pygame.Surface((300,200))
        self.game_map = self.load_map('map')
        
        self.background = Back(screen)
        self.plat_green = pygame.image.load("resources/image/platform/florest/p4.png").convert_alpha()
        self.plat_black = pygame.image.load("resources/image/platform/florest/p4_dark.png").convert_alpha()
        

        

    def load_map(self, fileName):
        file = open('data/gameplay/plataforma/'+fileName + '.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    def settingPlataform(self, scroll):
        self.background.movingBackgourndGamePlay(1)
        tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(self.plat_black, (x*40-scroll[0], y*40-scroll[1]))
                    tile_rects.append(pygame.Rect(x*40,y*40,40,40))
                elif(tile == '2'):
                    tile_rects.append(pygame.Rect(x*40,y*40,40,40))
                    self.screen.blit(self.plat_green, (x*40-scroll[0], y*40-scroll[1]))
                x += 1
            y += 1
        return tile_rects
    def platformEnimys(self):
        enimys_rects = []
        return enimys_rects