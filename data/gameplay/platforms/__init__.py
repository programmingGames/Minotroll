import pygame
from data.backgrounds import Backgound as Back

class Plataform:
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.game_map = []
        self.positionForest_x =[]
        self.parts = self.determinateLevelParts()
        self.load_map()
        self.background = Back(screen)
         

    def determinateLevelParts(self):
        if(self.nivel >= 0 and self.nivel <= 1):
            self.positionForest_x =[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340]
            return int(18)
        elif(self.nivel == 3):
            self.positionForest_x =[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]
            return int(13)

    def load_map(self):
        for i in range(self.parts):
            part_map = []
            file = open('data/gameplay/platforms/level'+str(self.nivel+1)+'/p'+str(i+1)+ '.txt', 'r')
            data = file.read()
            file.close()
            data = data.split('\n')
            for row in data:
                part_map.append(list(row))
            self.game_map.append(part_map)


    def settingPlataform(self, scroll, player_x):
        self.background.movingBackgourndGamePlay(1)
        if((self.nivel==1)or(self.nivel==0)or(self.nivel==3)):
            tile_rects = []
            for pos in self.positionForest_x:
                if(pos*16 in range(scroll[0]-450, scroll[0]+650)):
                    tile_rects += self.platformForestEnvirement(self.game_map[self.positionForest_x.index(pos)],pos,scroll)
            return tile_rects
        elif(self.nivel == 2):
            return self.platformSwampEnvirement(scroll)
        # elif(self.nivel == 3):
        #     return self.platformForestEnvirement(self.game_map[0], pos,scroll)


    def platformForestEnvirement(self,game_map,pos_x,scroll):
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
            x = pos_x 
            # self.x = self.maxPixelofParts * (self.parts-1)
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(components[0], (x*16-scroll[0], y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                elif(tile == '2'):
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                    self.screen.blit(components[1], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '3'):
                    self.screen.blit(components[2], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '4'):
                    self.screen.blit(components[3], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '5'):
                    self.screen.blit(components[4], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '6'):
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                    self.screen.blit(components[6], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '7'):
                    self.screen.blit(components[7], (x*16-scroll[0], y*16-scroll[1]))
                elif(tile == '8'):
                    self.screen.blit(components[8], (x*16-scroll[0], y*16-scroll[1]))
                x += 1
            y += 1
        return tile_rects


    def platformSwampEnvirement(self,scroll):
        components = [pygame.image.load('resources/image/platform/pantano/tiles/'+str(i)+'.png').convert_alpha() for i in range(6)]
        tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if (tile == '1'):
                    self.screen.blit(components[0], (x*30-scroll[0], y*30-scroll[1]))
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                elif(tile == '2'):
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                    self.screen.blit(components[1], (x*30-scroll[0], y*30-scroll[1]))
                elif(tile == '4'):
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                    self.screen.blit(components[2], (x*30-scroll[0], y*30-scroll[1]))
                elif(tile == '3'):
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                    self.screen.blit(components[4], (x*30-scroll[0], y*30-scroll[1]))
                elif(tile == '6'):
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                    self.screen.blit(components[5], (x*30-scroll[0], y*30-scroll[1]))
                elif(tile == '5'):
                    tile_rects.append(pygame.Rect(x*30,y*30,30,30))
                    self.screen.blit(components[3], (x*30-scroll[0], y*30-scroll[1]))
                x += 1
            y += 1
        return tile_rects