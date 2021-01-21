import pygame
from data.gameplay.collisionControl import Colision


class LifeItem(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.position = []
        self.nrItem = 0
        self.determinatePositionOfLifItems()
        self.collision = Colision()
        self.item = [PlantLife(self.screen) for i in range(self.nrItem)]
        self.item_rects = pygame.Rect(0, 0, 0, 0)
    
    def drawingTheLifeItem(self, player_rects, scroll):
        item_list=[]
        i = 0
        for pos in self.position:
            if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                print(self.nrItem)
                item_list.append(self.item[i].draw(pos, scroll))
            else:
                item_list.append(pygame.image.load("resources/image/life/1.png").get_rect())
            i+=1
        if(len(self.position)!=0):
            if(self.position[0][0] < scroll[0]-250):
                del self.position[0]      

        return self.controlingColection(item_list,player_rects)
    
    def controlingColection(self, item_list, player_rects):
        move = [0, 0]
        if(len(item_list)!=0):
            move[0] += item_list[0].x
            move[0] += item_list[0].x
        collision_types, position = self.collision.enimysCollision(move, player_rects, item_list)
        # print(player_rects)
        
        if(collision_types['top'] or collision_types['bottom'] or collision_types['right'] or collision_types['left']):
            del self.position[position]
            return True
        else:
            return False


    def determinatePositionOfLifItems(self):
        if(self.nivel == 0):
            self.position = [(1542, -20), (2890, 408),(3876,488), (4238, 408)]
            self.nrItem = 4
        elif(self.nivel == 1):
            self.position = [(1198,648), (2282,216), (3045,200)]
            self.nrItem = 3
        elif(self.nivel == 2):
            self.position = [(1178,410), (3811,-40),(5673,380)]
            self.nrItem = 3
        elif(self.nivel == 3):
            self.position = [(2474,408), (2966,232), (4081,-24),(4027,-24)]
            self.nrItem = 4


class PlantLife(object):
    def __init__(self, screen):
        self.screen = screen
        self.lifeItem = [pygame.image.load("resources/image/life/"+str(i)+".png") for i in range(28)]
        self.count=0
    def draw(self, pos, scroll):
        self.count +=1
        if(self.count<=27):
            self.screen.blit(self.lifeItem[self.count], (pos[0]-scroll[0],pos[1]-scroll[1]))
        else:
            self.count = 0
            self.screen.blit(self.lifeItem[self.count], (pos[0]-scroll[0],pos[1]-scroll[1]))
        rect = self.lifeItem[self.count].get_rect()
        rect.x = pos[0]
        rect.y = pos[1]
        return rect
        
