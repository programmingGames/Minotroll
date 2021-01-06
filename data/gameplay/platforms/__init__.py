import pygame
from data.backgrounds import Backgound as Back

class Plataform:
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.parts = 0
        self.maxPixelofParts = 70
        self.positionControl = 694
        self.ajust = 0
        # self.positionControl = 694
        self.game_map = []
        self.suport = []
        self.controlDrawing = False
        self.background = Back(screen)
        self.aux = 0
        self.x = 0
        self.y = 0
         


    def load_map(self):
        self.game_map = []
        file = open('data/gameplay/platforms/level'+str(self.nivel+1)+'/p'+str(self.parts+1)+ '.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
        for row in data:
            self.game_map.append(list(row))


    def settingPlataform(self, scroll, player_x):
        # print(self.positionControl)
        # print("---------")
        # print(player_x)
        if(player_x >= self.positionControl+self.ajust):
            self.parts += 1
            self.positionControl += 694
            self.suport = self.game_map
        self.load_map()
        self.background.movingBackgourndGamePlay(1)
        if(self.nivel <= 1):
            tile_rects = []
            # print(self.maxPixelofParts*(self.parts))
            if(len(self.suport)!=0):
                if((self.maxPixelofParts*(self.parts-1))<0):
                    tile_rects += self.platformForestEnvirement(self.suport,(self.maxPixelofParts*(self.parts-1))*-1,scroll)
                else:
                    tile_rects += self.platformForestEnvirement(self.suport,self.maxPixelofParts*(self.parts-1),scroll)
            tile_rects += self.platformForestEnvirement(self.game_map,self.maxPixelofParts*(self.parts),scroll)
            return tile_rects
        elif(self.nivel == 2):
            return self.platformSwampEnvirement(scroll)
        # elif(self.nivel == 3):
        #     return self.platformForestEnvirement(scroll)


    def platformForestEnvirement(self,game_map,x,scroll):
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
        self.y = 0
        for layer in game_map:

            self.x = x 
            # self.x = self.maxPixelofParts * (self.parts-1)
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(components[0], (self.x*16-scroll[0], self.y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(self.x*16,self.y*16,16,16))
                elif(tile == '2'):
                    tile_rects.append(pygame.Rect(self.x*16,self.y*16,16,16))
                    self.screen.blit(components[1], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '3'):
                    self.screen.blit(components[2], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '4'):
                    self.screen.blit(components[3], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '5'):
                    self.screen.blit(components[4], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '6'):
                    tile_rects.append(pygame.Rect(self.x*16,self.y*16,16,16))
                    self.screen.blit(components[6], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '7'):
                    self.screen.blit(components[7], (self.x*16-scroll[0], self.y*16-scroll[1]))
                elif(tile == '8'):
                    self.screen.blit(components[8], (self.x*16-scroll[0], self.y*16-scroll[1]))
                self.x += 1
            self.y += 1
        return tile_rects


    def platformSwampEnvirement(self,scroll):
        components = [pygame.image.load('resources/image/platform/pantano/tiles/'+str(i)+'.png').convert_alpha() for i in range(6)]
        tile_rects = []
        self.y = 0
        for layer in self.game_map:
            self.x = 0
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(components[0], (self.x*30-scroll[0], self.y*30-scroll[1]))
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                elif(tile == '2'):
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                    self.screen.blit(components[1], (self.x*30-scroll[0], self.y*30-scroll[1]))
                elif(tile == '4'):
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                    self.screen.blit(components[2], (self.x*30-scroll[0], self.y*30-scroll[1]))
                elif(tile == '3'):
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                    self.screen.blit(components[4], (self.x*30-scroll[0], self.y*30-scroll[1]))
                elif(tile == '6'):
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                    self.screen.blit(components[5], (self.x*30-scroll[0], self.y*30-scroll[1]))
                elif(tile == '5'):
                    tile_rects.append(pygame.Rect(self.x*30,self.y*30,30,30))
                    self.screen.blit(components[3], (self.x*30-scroll[0], self.y*30-scroll[1]))
                self.x += 1
            self.y += 1
        return tile_rects