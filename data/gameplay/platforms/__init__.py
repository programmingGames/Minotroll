import pygame
from data.backgrounds import Backgound as Back

class Plataform:
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.game_map = []
        self.positionForest_x =[]
        self.positionSwamp_x = []
        self.determinateLevelParts()
        self.load_map()
        self.background = Back(screen)
         

    def determinateLevelParts(self):
        if(self.nivel >= 0 and self.nivel <= 1):
            self.positionForest_x =[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340]
            self.parts = int(18)
        elif(self.nivel == 3):
            self.positionForest_x =[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]
            self.parts = int(13)
        elif(self.nivel == 2):
            self.positionSwamp_x = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228]
            self.parts = int(20)

        # Controlling the size of the items on the platform
        if((self.nivel==0)or(self.nivel==1)or(self.nivel==3)):
            self.size = int(16)
        elif(self.nivel == 2):
            self.size = int(30)

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


    def settingPlataform(self, scroll):
        self.background.movingBackgourndGamePlay(self.nivel)
        if((self.nivel==1)or(self.nivel==0)or(self.nivel==3)):
            tile_rects = []
            for pos in self.positionForest_x:
                if(pos*self.size in range(scroll[0]-450, scroll[0]+750)):
                    tile_rects += self.platformForestEnvirement(self.game_map[self.positionForest_x.index(pos)],pos,scroll)
            return tile_rects
        elif(self.nivel == 2):
            tile_rects = []
            for pos in self.positionSwamp_x:
                if(pos*self.size in range(scroll[0]-450, scroll[0]+650)):
                    tile_rects += self.platformSwampEnvirement(self.game_map[self.positionSwamp_x.index(pos)],pos,scroll)
            return tile_rects


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


    def platformSwampEnvirement(self,game_map, pos_x,scroll):
        components = [pygame.image.load('resources/image/platform/pantano/tiles/'+str(i)+'.png').convert_alpha() for i in range(6)]
        tile_rects = []
        y = 0
        for layer in game_map:
            x = pos_x
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