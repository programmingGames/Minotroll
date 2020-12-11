import pygame
from pygame.locals import *
from data.vector import Vector2
from data.player.life import Life

class Player:
    def __init__(self, screen, nivel, skills, lastPassPoint):
        self.life = Life(screen)
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
        self.skills = skills

    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if (rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

    def allPlatformColision(self,movement,tiles, tile_item):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.player_rect.x += movement[0]
        hit_list = self.collision_test(self.player_rect,tiles)
        for tile in zip(hit_list, tile_item):
            print(tile)
            if movement[0] > 0:
                self.player_rect.right = tile[0].left
                collision_types['right'] = True
                if(tile[1]==3):
                    self.life.damageLife(1)
            elif movement[0] < 0:
                self.player_rect.left = tile[0].right
                collision_types['left'] = True
                if(tile[1]==3):
                    self.life.damageLife(10)


        self.player_rect.y += movement[1]
        hit_list = self.collision_test(self.player_rect,tiles)
        for tile in zip(hit_list, tile_item):
            if movement[1] > 0:
                self.player_rect.bottom = tile[0].top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                self.player_rect.top = tile[0].bottom
                collision_types['top'] = True
        return collision_types

    def determinateMove(self):
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.move_direction = 'right'
                    self.moving_right = True
                if event.key == K_LEFT:
                    self.move_direction = 'left'
                    self.moving_left = True
                if event.key == K_UP:
                    if self.air_timer < 8:
                        self.vertical_momentum = -7
                self.state = 'Walking'
                
            else:
                self.moving_right = False
                self.moving_left = False

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.moving_right = False
                if event.key == K_LEFT:
                    self.moving_left = False
        

    def controlPlayerScreenMove(self):
        ## Validando bordas do screen
        if(self.player_rect.x == self.player_screen_limit):
            self.moving_left = False

        ## Reduzindo o espaço a que o jogador pode voltar para traz
        if((self.player_rect.x-self.player_screen_limit)>800):
            self.player_screen_limit += 40
    
    def playerMove(self, tile_rects,tile_item, player_movement):
        if self.moving_right:
            self.walk()
            player_movement[0] += 4
        if self.moving_left:
            self.walk()
            player_movement[0] -= 4

        if((not self.moving_left)and(not self.moving_right)):
            self.idle()
        player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 6:
            self.vertical_momentum = 6
        
        platformCollisions = self.allPlatformColision(player_movement,tile_rects, tile_item)
        
        if (platformCollisions['bottom']):
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1


    def settingPlayer(self, event, tile_rects, tile_item, scroll):
        player_movement = [0,0]
        self.screen.blit(self.player_img,(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))
        self.determinateMove()
        self.controlPlayerScreenMove()
        self.playerMove(tile_rects,tile_item, player_movement)

        
        ## Calculando o scroll do ecrã
        scroll[0] += (self.player_rect.x-scroll[0]-300)/20
        scroll[1] += (self.player_rect.y-scroll[1]-350)/10
        # Transformando a scroll em um valor inteiro 
        correct_scroll = scroll.copy()
        correct_scroll[0] = int(correct_scroll[0])
        correct_scroll[1] = int(correct_scroll[1])
        self.lifeControl()
        return correct_scroll, self.player_rect
            
    def lifeControl(self):
        self.life.draw()

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