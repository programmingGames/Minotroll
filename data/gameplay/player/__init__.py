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
        self.skillsInUse = 'kicking'
        self.move_frame = 0
        self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
        self.player_rect=self.player_img.get_rect()
        self.player_rect.x = lastPassPoint[0]
        self.player_rect.y = lastPassPoint[1]

        ## atributes to control the player state
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.hurtten = False
        self.attack = False
        self.bottomColision = False

        self.vertical_momentum = 0
        self.air_timer = 0
        # self.scrollLimit_x = 245
        self.player_screen_limit = 380
        self.nivel = nivel
        self.impactDelay = 0
        self.slashingControl = 0
        self.enimyCollision = False
        self.enimyType = ''         

    def controlPlayerScreenMove(self):
        ## validando o limite que o jogador pode voltar atraz
        if(self.player_rect.x <= self.player_screen_limit):
            self.moving_left = False

        ## atualizando o limite a que o jogador pode voltar para traz
        if(self.player_rect.x > self.player_screen_limit +800):
            self.player_screen_limit += 80

    def playerMove(self, tile_rects, player_movement, scroll):
        if self.moving_right:
            if self.jumping:
                self.jump()
            else:
                self.walk()
            player_movement[0] += 4
        elif self.moving_left:
            if self.jumping:
                self.jump()
            else:
                self.walk()
            player_movement[0] -= 4
        if self.jumping:
            self.jump()
            if self.air_timer < 8:
                self.vertical_momentum = -10
        
        if self.hurtten:
            self.hurt()

        if self.attack :
            self.determinateAttack()
            

        if((not self.moving_left)and(not self.moving_right)and not self.attack):
            self.idle()
        player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.6
        if self.vertical_momentum > 6:
            self.vertical_momentum = 6
        self.player_rect, self.platformCollisions = self.collision.platformCollision(player_movement,self.player_rect,tile_rects)
        if (self.platformCollisions['bottom']):
            self.air_timer = 0
            self.vertical_momentum = 0
            self.jumping = False
            self.bottomColision = True
        else:
            self.bottomColision = False
        if self.platformCollisions['top']:
            self.jumping = False
            self.vertical_momentum += 5
        else:
            self.air_timer += 1
        self.screen.blit(self.player_img,(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))


    def settingPlayer(self, tile_rects, scroll, allEnimysRectsAndType, inUse):
        self.skillsInUse = inUse
        # print(self.skillsInUse)
        player_movement = [0,0]
        self.determinateMove()
        self.controlPlayerScreenMove()
        self.playerMove(tile_rects, player_movement, scroll)

        # if(self.player_rect.x > 500):
        scroll[0] += (self.player_rect.x-scroll[0]-300)/20
        scroll[1] += (self.player_rect.y-scroll[1]-300)/10
        # Transformando a scroll em um valor inteiro 
        correct_scroll = scroll.copy()
        correct_scroll[0] = int(correct_scroll[0])
        correct_scroll[1] = int(correct_scroll[1])
        self.checkingEnimysCollision(player_movement,allEnimysRectsAndType)
        self.collisionInpact(tile_rects)
        return correct_scroll, self.player_rect, self.enimyCollision, self.enimyType

    def checkingEnimysCollision(self, player_move,enimysRectsAndType):
        rectList = []
        enimyList = []
        for enimy in enimysRectsAndType:
            rectList.append(enimy[0])
            enimyList.append(enimy[1])

        collision, position = self.collision.enimysCollision(player_move,self.player_rect,rectList)
        if(collision['top'] or collision['right'] or collision['bottom'] or collision['left']):
            self.hurtten = True
            self.enimyCollision = True
            self.impactDelay = 0
            self.enimyType = enimyList[position]
        else:
            self.hurtten = False

    def collisionInpact(self, tile_rects):
        # player_movement=[0 , 0]
        if self.enimyCollision :
            if(self.impactDelay <= 5):
                # self.player_rect, platformCollisions = self.collision.platformCollision(player_movement,self.player_rect,tile_rects)
                if(self.move_direction == 'right'):
                    if (self.impactDelay>5):
                        self.move_direction = 'left'
                    self.player_rect.x -= 5
                    self.player_rect.y -= 10
                elif(self.move_direction == 'left'):
                    if (self.impactDelay>5):
                        self.move_direction = 'right'
                    self.player_rect.x += 5
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

            if(key_press[K_UP]and self.bottomColision==True):
                if self.air_timer < 8:
                    self.vertical_momentum = -10

        elif(key_press[K_LEFT]):
            self.move_direction = 'left'
            self.moving_left = True
            self.state = 'Walking'

            if(key_press[K_UP] and self.bottomColision==True):
                if self.air_timer < 8:
                    self.vertical_momentum = -10


        elif(key_press[K_UP]and self.bottomColision==True):
            self.state = 'JumLoop'
            self.jumping = True
            # self.state = 'Walking'
            
        elif(not key_press[K_RIGHT] and not key_press[K_LEFT]):
            self.moving_right = False
            self.moving_left = False

        elif(key_press[K_UP]and self.bottomColision==True):
            self.state = 'JumpLoop'
            if(key_press[K_RIGHT]):
                self.moving_right = False
            if(key_press[K_LEFT]):
                self.moving_left = False 
            self.jumping = True

        if(key_press[K_RIGHT] or key_press[K_LEFT]):
            if(key_press[K_UP]and self.bottomColision==True):
                self.jumping = True
        ## button for to attack
        if key_press[K_q]:
            self.attack = True
        else:
            self.slashingControl = 0
            self.attack = False

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
        self.state = 'JumpLoop'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 5)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 5)):
            self.move_frame = 0
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
            
    def hurt(self):
        self.state = 'Hurt'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 11)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 11)):
            self.move_frame = 0
            # self.hurtten = False
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()



    ### the following method is related to the player attack
    def determinateAttack(self):
        self.state = self.skillsInUse
        if (self.skillsInUse == 'kicking'):
            self.kicking()
        elif(self.skillsInUse == 'greenfire'):
            self.throwing('greenfire')
        elif(self.skillsInUse == 'bluefire'):
            self.throwing('bluefire')
        ## just for hork
        elif(self.skillsInUse == 'slashing'):
            ## Actuly is sliding not slashing after i will change this logic in all over the project
            self.sliding()
        elif(self.skillsInUse == 'battleax'):
            self.battleax()

    def kicking(self):
        self.state = 'Kicking'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 11)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 11)):
            self.move_frame = 0
            # self.hurtten = False
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()

    def battleax(self):
        self.state = 'battleax'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 11)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 11)):
            self.move_frame = 0
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
        
    def sliding(self):
        self.state = 'battleax'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 11)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 11)):
            self.move_frame = 0
            # self.hurtten = False
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()

        if(self.slashingControl <= 10):
            if(self.move_direction=='right'):
                self.player_rect.x  += 9
                self.slashingControl += 1
            else:
                self.slashingControl += 1
                self.player_rect.x -= 9
        else:
            self.attack = False

    def throwing(self, type):
        pass
    def numberSprite(self):
        if(self.state=='Walking'):
            return 23
        elif(self.state=='Idle'):
            return 17