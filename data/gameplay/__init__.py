import pygame
from pygame.locals import *
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
        self.enimys = ControlEnimys(self.screen)
        self.animation = Animation(self.screen, self.nivel)
        self.headUpDisplay = H_u_d(self.screen, self.nivel, self.lastPassPoint, self.qtlife)
        self.player = Player(self.screen, self.nivel, self.lastPassPoint)
        self.platform = Plataform(self.screen, self.nivel)
        self.liveItem = LifeItem(self.screen, self.nivel)
        self. nivel = 1 # default value of the level started usualy in 1 
        self.skills = 1 # default value of skills the player have
        self.lastPassPoint = 500 # default Value for position of the player in the platform
        self.player_rect = pygame.Rect(0, 0, 0, 0) # To control the player rects
        self.scroll = [0, 0]  # Variable to control the scroll of the screen
        self.enimyCollision = False
        self.enimyType = ''
        self.allEnimysRectsAndTypes = []
        self.ptforStart = True        

    
    # method to display all the components in the platform
    def drawingTheGamePlayEnvirement(self):
        tile_rects = self.platform.settingPlataform(self.scroll)
        self.scroll, self.player_rect, self.enimyCollision, self.enimyType  = self.player.settingPlayer(tile_rects, self.scroll, self.allEnimysRectsAndTypes)

        # update after we check the collision
        self.allEnimysRectsAndTypes = self.enimys.enimysAdd(tile_rects, self.player_rect, self.scroll)

        # Drawing some visual animation
        self.animation.draw()
        painelState = self.headUpDisplay.headUpDisplayScreenDraw(self.lastPassPoint)

        self.itemLifeCollision = self.liveItem.drawingTheLifeItem(self.player_rect, self.scroll)
        
        self.lastPassPoint = self.player_rect.x

        self.controllingThePlayerLife()
 
        if(self.player_rect.y >= 720):
            painelState = 11    
        # print(self.player_rect.x, self.player_rect.y)
        return painelState
    
    def controllingThePlayerLife(self):
        if self.enimyCollision:
            self.headUpDisplay.updatingPlayerLife(self.enimyType)
        elif self.itemLifeCollision:
            self.headUpDisplay.updatingPlayerLife('life plant')
        