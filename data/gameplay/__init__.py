import pygame
from pygame.locals import *
from data.gameplay.player import Player
from data.gameplay.platforms import Plataform
from data.gameplay.headUpDisplay import HeadUpDisplay as H_u_d
from data.gameplay.enimy import ControlEnimys
from data.gameplay.animation import Animation


class GamePlay(object):
    def __init__(self, screen, nivel, lastPassPoint,qtlife, pygameEvent):
        # self.allEnimys = ['blue wizard', 'fire golem', 'stone golem', 'ice golem', 'blue robots', 'dark robots', 'gold robots']
        self.screen = screen
        self.nivel = nivel
        self.lastPassPoint = lastPassPoint
        self.qtlife = qtlife
        self.pygameEvent = pygameEvent
        self.player = Player(self.screen, self.nivel, self.lastPassPoint)
        self.plataforma = Plataform(self.screen, self.nivel)
        self.enimys = ControlEnimys(self.screen)
        self.animation = Animation(self.screen, self.nivel)
        self.headUpDisplay = H_u_d(self.screen, self.nivel, self.lastPassPoint, self.qtlife)
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
        tile_rects = self.plataforma.settingPlataform(self.scroll)
        self.scroll, player_rect, self.enimyCollision, self.enimyType  = self.player.settingPlayer(tile_rects, self.scroll, self.allEnimysRectsAndTypes)

        # update after we check the collision
        self.allEnimysRectsAndTypes = self.enimys.enimysAdd(tile_rects, player_rect, self.scroll)
        # self.allEnimysRectsAndTypes.append()

        # Drawing some visual animation
        self.animation.draw()

        painelState = self.headUpDisplay.headUpDisplayScreenDraw(self.lastPassPoint)
        self.lastPassPoint = player_rect.x

        self.controllingThePlayerLife()
 
        if(player_rect.y >= 720):
            painelState = 11    
        # print(player_rect.x)
        return painelState
    
    def controllingThePlayerLife(self):
        if self.enimyCollision:
            self.headUpDisplay.damagingPlayerLife(self.enimyType)
        