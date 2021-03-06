import pygame
from pygame.locals import *
from data.gameplay.collisionControl import Colision

# Class that ilustrate the player
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
        self.topColision = False
        self.firing = False
        self.preCollisionAriaRight = [0,0]
        self.preCollisionAriaLeft = [0,0]
     

        self.vertical_momentum = 0
        self.air_timer = 0
        self.player_screen_limit = 380
        self.nivel = nivel
        self.impactDelay = 0
        self.slashingControl = 0
        self.count = 0
        self.fireArray = []
        self.enimyCollision = False
        self.enimyType = ''         

    # Method that limited the player to walk back
    def controlPlayerScreenMove(self):
        ## validando o limite que o jogador pode voltar atraz
        if(self.player_rect.x <= self.player_screen_limit):
            self.moving_left = False
        

        ## atualizando o limite a que o jogador pode voltar para traz
        if(self.player_rect.x > self.player_screen_limit + 800):
            self.player_screen_limit += 80

    # Method that control all the player move
    def playerMove(self, tile_rects, player_movement, scroll, tile_rect):
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
                self.vertical_momentum = -15
        
        if self.hurtten:
            self.hurt()

        if self.attack :
            # self.firing = True
            self.determinateAttack(player_movement, tile_rect)
        
        self.fireEnimyCollision, self.fireCollisionPos = self.fireControl(tile_rects, scroll)

        if((not self.moving_left)and(not self.moving_right)and not self.attack):
            self.idle()

        player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.8
        if self.vertical_momentum > 10:
            self.vertical_momentum = 10
        self.player_rect, self.platformCollisions = self.collision.platformCollision(player_movement,self.player_rect,tile_rects)
        if (self.platformCollisions['bottom']):
            self.air_timer = 0
            self.vertical_momentum = 0
            self.bottomColision = True
        else:
            self.bottomColision = False

        if self.platformCollisions['top']:
            self.vertical_momentum = 10
        else:
            self.topColision = False
            self.air_timer += 4

        if(self.platformCollisions['right']):
            self.moving_right = False
        elif(self.platformCollisions['left']):
            self.moving_left = False
        
        if self.air_timer == 4:
            self.jumping = False

        self.screen.blit(self.player_img,(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))

    # Method that control the fire collision
    def fireControl(self, tile_rect, scroll):
        platfcolision = []
        enimyCollision = False
        pos = 0
        if self.firing:
            platfcolision = [fire.draw(tile_rect,self.enimyRectList, scroll) for fire in self.fireArray]
        i = 0

        ## cheching all the condition to delete one fire
        for colid in platfcolision:
            if colid[0]:
                del self.fireArray[i]
                enimyCollision = colid[1]
                pos = colid[2]


        i = 0
        for fire in self.fireArray:
            if ((fire.rect.x > self.player_rect.x + 700)or(-1*fire.rect.x > (self.player_rect.x - 700)*-1)):
                del self.fireArray[i]
        return enimyCollision, pos

    # Method that control and blit the player on the screen
    def settingPlayer(self, tile_rects, scroll, allEnimysRectsAndType, inUse):
        self.platformCollisions = {'top':False,'bottom':False,'right':False,'left':False}
        self.skillsInUse = inUse
        player_movement = [0,0]
        self.determinateMove(scroll)
        self.controlPlayerScreenMove()
        self.playerMove(tile_rects, player_movement, scroll, tile_rects)

        scroll[0] += (self.player_rect.x-scroll[0]-300)/20
        scroll[1] += (self.player_rect.y-scroll[1]-300)/10
        # Transformando a scroll em um valor inteiro 
        correct_scroll = scroll.copy()
        correct_scroll[0] = int(correct_scroll[0])
        correct_scroll[1] = int(correct_scroll[1])
        position = self.checkingEnimysCollision(player_movement,allEnimysRectsAndType)
        self.collisionInpact(tile_rects, player_movement)
        return correct_scroll, self.player_rect,self.fireArray, self.enimyCollision, self.enimyType,self.fireEnimyCollision, self.fireCollisionPos, (self.attack,position)

    # Methodd that control the enimys collision
    def checkingEnimysCollision(self, player_move,enimysRectsAndType):
        self.enimyRectList = []
        enimyList = []
        for enimy in enimysRectsAndType:
            self.enimyRectList.append(enimy[0])
            enimyList.append(enimy[1])
        

        collision, position = self.collision.enimysCollision(player_move,self.player_rect,self.enimyRectList)
        if(collision['top'] or collision['right'] or collision['bottom'] or collision['left']):
            self.hurtten = True
            self.enimyCollision = True
            self.impactDelay = 0
            self.enimyType = enimyList[position]
        else:
            self.hurtten = False
        return position

    # Method that control the platform collision
    def collisionInpact(self, tile_rect, playerMove):
        player_rect, prePlatformCollisionsRight = self.collision.platformCollision(playerMove,pygame.Rect(self.player_rect.x + 20, self.player_rect.y ,30, 40),tile_rect)
        player_rect, prePlatformCollisionsLeft = self.collision.platformCollision(playerMove,pygame.Rect(self.player_rect.x - 20, self.player_rect.y ,30, 40),tile_rect)
        del player_rect

        if(prePlatformCollisionsRight['right']or prePlatformCollisionsRight['left']):
            self.preCollisionAriaRight = []
            self.preCollisionAriaRight.append(self.player_rect.x)
            self.preCollisionAriaRight.append( self.player_rect.y)
        if(prePlatformCollisionsLeft['right']or prePlatformCollisionsLeft['left']):
            self.preCollisionAriaLeft = []
            self.preCollisionAriaLeft.append(self.player_rect.x)
            self.preCollisionAriaLeft.append( self.player_rect.y)

        if self.enimyCollision and self.attack == False:
            if((self.impactDelay <= 5)and(self.player_rect.x not in range(self.preCollisionAriaRight[0]-20, self.preCollisionAriaRight[0]+20))and (self.player_rect.x not in range(self.preCollisionAriaLeft[0]-20, self.preCollisionAriaLeft[0]+20))):
                if(self.move_direction == 'right'):
                    self.player_rect.x -= 4
                    self.player_rect.y -= 4
                elif(self.move_direction == 'left'):
                    self.player_rect.x += 4
                    self.player_rect.y -= 4
                self.impactDelay += 1
            else:
                self.enimyCollision = False

    # Method that determinate the player move according to the keyboard inputs
    def determinateMove(self, scroll):
        key_press = pygame.key.get_pressed()
        if(key_press[K_RIGHT]):
            self.move_direction = 'right'
            self.moving_right = True
            self.state = 'Walking'

            if(key_press[K_UP]and self.bottomColision==True):
                self.jumping = True

        elif(key_press[K_LEFT]):
            self.move_direction = 'left'
            self.moving_left = True
            self.state = 'Walking'

            if(key_press[K_UP] and self.bottomColision==True):
                self.jumping = True

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
            if((self.skillsInUse == 'bluefire' or self.skillsInUse == 'greenfire') and (self.count >= 10)):
                self.fireArray.append(Fire(self.screen, self.skillsInUse,(self.player_rect.x, self.player_rect.y), self.move_direction))
                self.firing = True
                self.count = 0
            self.attack = True
        else:
            self.slashingControl = 0
            self.attack = False
        self.count += 1
        
    # Methods above are all related to the player sprites
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
    def determinateAttack(self, playerMove, tile_rect):

        player_rect, prePlatformCollisionsRight = self.collision.platformCollision(playerMove,pygame.Rect(self.player_rect.x + 20, self.player_rect.y ,30, 40),tile_rect)
        player_rect, prePlatformCollisionsLeft = self.collision.platformCollision(playerMove,pygame.Rect(self.player_rect.x - 20, self.player_rect.y ,30, 40),tile_rect)
        del player_rect

        if(prePlatformCollisionsRight['right']or prePlatformCollisionsRight['left']):
            self.preCollisionAriaRight = []
            self.preCollisionAriaRight.append(self.player_rect.x)
            self.preCollisionAriaRight.append( self.player_rect.y)
        if(prePlatformCollisionsLeft['right']or prePlatformCollisionsLeft['left']):
            self.preCollisionAriaLeft = []
            self.preCollisionAriaLeft.append(self.player_rect.x)
            self.preCollisionAriaLeft.append( self.player_rect.y)

        self.state = self.skillsInUse
        if (self.skillsInUse == 'kicking'):
            self.kicking()
        elif(self.skillsInUse == 'greenfire'):
            self.throwing()
        elif(self.skillsInUse == 'bluefire'):
            self.throwing()
        ## just for hork
        
        elif((self.skillsInUse == 'slashing')and(self.player_rect.x not in range(self.preCollisionAriaRight[0]-20, self.preCollisionAriaRight[0]+20))and (self.player_rect.x not in range(self.preCollisionAriaLeft[0]-20, self.preCollisionAriaLeft[0]+20))):
            if((self.slashingControl <= 10) and(self.player_rect.x >= self.player_screen_limit)):
                    self.sliding()
            else:
                self.attack = False
                if(self.moving_left or self.moving_right):
                    self.walk()
                else:
                    self.idle()
            self.slashingControl += 1

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
        self.state = 'Sliding'
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 5)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 5)):
            self.move_frame = 0
            # self.hurtten = False
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()
        if(self.move_direction=='right'):
            self.player_rect.x  += 9
        else:
            self.player_rect.x -= 9

    def throwing(self):
        self.state = 'Throwing' 
        if(((not self.moving_right)or(not self.moving_left ))and(self.move_frame <= 11)):
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.moving_right)or(not self.moving_left))and(self.move_frame > 11)):
            self.move_frame = 0
            # self.hurtten = False
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.player_img = pygame.image.load("resources/image/Golem/"+self.state+"/"+self.move_direction+"/0_Goblin_"+self.state+"_0.png").convert_alpha()

class Fire(object):
    def __init__(self, screen, fireType, pos, direction):
        self.screen = screen
        self.collision = Colision()
        self.img = [pygame.image.load("resources/image/Golem/fire/"+direction+"/"+fireType+""+str(i)+".png") for i in range(2)]
        self.rect = self.img[0].get_rect()
        self.player_pos = pos
        self.nrimg = 0
        if(direction == "right"):
            self.rect.x = pos[0]+40
        else:
            self.rect.x = pos[0]-40
        self.rect.y = pos[1] + 15
        self.direction = direction

    def draw(self, tile_rect,enimysRects, scroll):
        fire_move = [0, 0]
        platfcollision = False
        enimyCollision = False
        if(self.direction == 'right'):
            fire_move[0] += 5
        else:
            fire_move[0] -= 5
        
        ## cheching platoform colision
        rect, plat_collisions = self.collision.platformCollision(fire_move,self.rect, tile_rect)
        enimys_colid, pos = self.collision.enimysCollision(fire_move, self.rect, enimysRects)
        del rect
        if(plat_collisions['right'] or plat_collisions['left'] or enimys_colid['right'] or enimys_colid['left']):
            if enimys_colid['right'] or enimys_colid['left']:
                enimyCollision = True
            else:
                enimyCollision = False
            platfcollision = True
        else:
            platfcollision = False
        
        self.rect.x += fire_move[0]

        if self.nrimg == 0:
            self.nrimg = 1
        else:
            self.nrimg = 0
        
        self.screen.blit(self.img[self.nrimg],(self.rect.x-scroll[0], self.rect.y-scroll[1]))
        return platfcollision, enimyCollision, pos