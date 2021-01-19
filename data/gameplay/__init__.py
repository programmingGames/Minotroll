import pygame
from pygame.locals import *
import os
from data.gameplay.headUpDisplay import HeadUpDisplay as H_u_d
from data.gameplay.lifeItem import LifeItem
from data.gameplay.enimy import ControlEnimys
from data.gameplay.animation import Animation
from data.gameplay.player import Player
from data.gameplay.platforms import Plataform


class GamePlay(object):
    def __init__(self, screen, nivel, lastPassPoint,qtlife, pygameEvent):
        # self.allEnimys = ['blue wizard', 'fire golem', 'stone golem', 'ice golem', 'blue robots', 'dark robots', 'gold robots']
        self.screen = screen
        self.nivel = nivel
        self.lastPassPoint = lastPassPoint
        self.qtlife = qtlife
        self.pygameEvent = pygameEvent
        self.enimys = ControlEnimys(self.screen, self.nivel)
        self.animation = Animation(self.screen, self.nivel)
        self.headUpDisplay = H_u_d(self.screen, self.nivel, self.lastPassPoint, self.qtlife)
        self.player = Player(self.screen, self.nivel, self.lastPassPoint)
        self.platform = Plataform(self.screen, self.nivel)
        self.liveItem = LifeItem(self.screen, self.nivel)
        self. nivel = nivel # default value of the level started usualy in 0
        self.inUse = ''
        # self.skills = 1 # default value of skills the player have
        # self.lastPassPoint = 500 # default Value for position of the player in the platform
        self.player_rect = pygame.Rect(0, 0, 0, 0) # To control the player rects
        self.scroll = [0, 0]  # Variable to control the scroll of the screen
        self.enimyCollision = False
        self.enimyType = ''
        self.allEnimysRectsAndTypes = []
        self.playerOnAttack = False

    
    # method to display all the components in the platform
    def drawingTheGamePlayEnvirement(self):
        # key_press = pygame.key.get_pressed()
        tile_rects = self.platform.settingPlataform(self.scroll)
        self.scroll, self.player_rect,self.fireArray, self.enimyCollision, self.enimyType, self.fireEnimyColision, self.fireCollsionPos, self.playerOnAttack = self.player.settingPlayer(tile_rects, self.scroll, self.allEnimysRectsAndTypes, self.inUse)

        # update after we check the collision
        self.allEnimysRectsAndTypes = self.enimys.enimysAdd(tile_rects, self.player_rect,(self.fireEnimyColision, self.fireCollsionPos),(self.playerOnAttack, self.inUse), self.scroll)

        # Drawing some visual animation
        self.animation.draw()
        painelState, self.qtlife, self.inUse = self.headUpDisplay.headUpDisplayScreenDraw(self.player_rect.x)

        self.itemLifeCollision = self.liveItem.drawingTheLifeItem(self.player_rect, self.scroll)
         
        self.controllingThePlayerLife()

        # controlling the end of the levels
        if((self.nivel == 0)or(self.nivel == 1)):
            if(self.player_rect.x >= 5460):
                painelState = 13
        elif(self.nivel==2):
            if(self.player_rect.x >= 6760):
                painelState = 13

        # controlling the falling out of the game platform
        if(self.player_rect.y >= 720):
            painelState = 11  

        # print(self.player_rect.x, self.player_rect.y)
        # print(self.playerOnAttack)
        self.controllingTheImageOfGameOverAndLevelComplete(painelState)
        return painelState, self.player_rect, self.qtlife
    
    def controllingThePlayerLife(self):
        if (self.enimyCollision and self.playerOnAttack == False):
            self.headUpDisplay.updatingPlayerLife(self.enimyType)
        if self.itemLifeCollision:
            self.headUpDisplay.updatingPlayerLife('life plant')

    def controllingTheImageOfGameOverAndLevelComplete(self, painelState):
        if(painelState==11):
            os.chdir('resources/image/menu/gamOver')
            pygame.image.save(self.screen, "back.png")
            pygame.time.delay(100)
            os.chdir('../../../..')
            surf = pygame.Surface((700, 480))
            img = pygame.image.load("resources/image/menu/gamOver/back.png").convert_alpha()
            img1 = pygame.image.load("resources/image/menu/gamOver/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/gamOver')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')

        elif(painelState==13):
            os.chdir('resources/image/menu/levelComplet')
            pygame.image.save(self.screen, "back.png")
            pygame.time.delay(100)
            os.chdir('../../../..')
            surf = pygame.Surface((700, 480))
            img = pygame.image.load("resources/image/menu/levelComplet/back.png").convert_alpha()
            img1 = pygame.image.load("resources/image/menu/gamOver/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/levelComplet')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')
        