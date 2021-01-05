import pygame
from pygame.locals import *
from data.gameplay.collisionControl import Colision


class Player(object):
    def __init__(self, screen, nivel, lastPassPoint):
        self.collision = Colision()
        self.screen = screen
        self.air_timer = 0
        self.vertical_momentum = 0
        self.player_move = [0, 0]
        self.move_direction = 'right'
        self.state = 'Idle'
        self.move_frame = 0
        self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
        self.player_rect=self.player_img.get_rect()
        self.player_rect.x = lastPassPoint
        self.moving_right = False
        self.moving_left = False
        self.vertical_momentum = 0
        self.air_timer = 0
        self.player_screen_limit = 280
        self.nivel = nivel
        self.impactDelay = 0
        self.enimyCollision = False
        self.enimyType = ''         

    def controlPlayerScreenMove(self):
        ## Validando bordas do screen
        if(self.player_rect.x <= self.player_screen_limit):
            self.moving_left = False

        ## Reduzindo o espaço a que o jogador pode voltar para traz
        if((self.player_rect.x-self.player_screen_limit)>800):
            self.player_screen_limit += 40
    
    def playerMove(self, tile_rects, player_movement):
        if self.moving_right:
            self.walk()
            player_movement[0] += 4
        if self.moving_left:
            self.walk()
            player_movement[0] -= 4

        if((not self.moving_left)and(not self.moving_right)):
            self.idle()
        player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.3
        if self.vertical_momentum > 6:
            self.vertical_momentum = 6
        platformCollisions = self.collision.platformCollision(player_movement,self.player_rect,tile_rects)
        if (platformCollisions['bottom']):
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1


    def settingPlayer(self, tile_rects, scroll, allEnimysRectsAndType):
        player_movement = [0,0]
        self.screen.blit(self.player_img,(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))
        self.determinateMove()
        self.controlPlayerScreenMove()
        self.playerMove(tile_rects, player_movement)

        
        ## Calculando o scroll do ecrã
        scroll[0] += (self.player_rect.x-scroll[0]-300)/20
        scroll[1] += (self.player_rect.y-scroll[1]-320)/10
        # Transformando a scroll em um valor inteiro 
        correct_scroll = scroll.copy()
        correct_scroll[0] = int(correct_scroll[0])
        correct_scroll[1] = int(correct_scroll[1])
        # print(allEnimysRectsAndType)
        self.checkingEnimysCollision(player_movement,allEnimysRectsAndType)
        self.collisionInpact()
        return correct_scroll, self.player_rect, self.enimyCollision, self.enimyType

    def checkingEnimysCollision(self, player_move,enimysRectsAndType):
        rectList = []
        enimyList = []
        for enimy in enimysRectsAndType:
            rectList.append(enimy[0])
            enimyList.append(enimy[1])

        collision, position = self.collision.enimysCollision(player_move,self.player_rect,rectList)
        # print(position)
        if(collision['top'] or collision['right'] or collision['bottom'] or collision['left']):
            self.enimyCollision = True
            self.impactDelay = 0
            self.enimyType = enimyList[position]

    def collisionInpact(self):
        if self.enimyCollision :
            if(self.impactDelay <= 10):
                if(self.move_direction == 'right'):
                    self.player_rect.x -= 10
                    self.player_rect.y -= 10
                elif(self.move_direction == 'left'):
                    self.player_rect.x += 10
                    self.player_rect.y -= 10
                self.impactDelay += 1
            else:
                self.enimyCollision = False
                


    def determinateMove(self):
        key_press = pygame.key.get_pressed()
        if(key_press[K_RIGHT]):
            self.move_direction = 'right'
            self.moving_right = True
            self.state = 'Walking'

            if(key_press[K_UP]):
                if self.air_timer < 8:
                    self.vertical_momentum = -7

        elif(key_press[K_LEFT]):
            self.move_direction = 'left'
            self.moving_left = True
            self.state = 'Walking'

            if(key_press[K_UP]):
                if self.air_timer < 8:
                    self.vertical_momentum = -7

        elif(key_press[K_UP]):
            if self.air_timer < 8:
                self.vertical_momentum = -7
            self.state = 'Walking'
            
        elif(not key_press[K_RIGHT] and not key_press[K_LEFT]):
            self.moving_right = False
            self.moving_left = False

        elif(key_press[K_UP]):
            if(key_press[K_RIGHT]):
                self.moving_right = False
            if(key_press[K_LEFT]):
                self.moving_left = False 

    def walk(self):
        self.state = 'Walking'
        if(((self.moving_right)or(self.moving_left))and(self.move_frame <= 23)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((self.moving_right)or(self.moving_left))and(self.move_frame > 23)):
            self.move_frame = 0 
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()        
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()

    def idle(self):
        self.state = 'Idle'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 17)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 17)):
            self.move_frame = 0
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
            
    def jump(self):
        pass
    def hurt(self):
        pass
    def die(self):
        pass
    def kicking(self):
        pass
    def slashing(self):
        pass
    def sliding(self):
        pass
    def throwing(self):
        pass
    def numberSprite(self):
        if(self.state=='Walking'):
            return 23
        elif(self.state=='Idle'):
            return 17