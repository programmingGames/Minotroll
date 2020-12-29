import pygame
from pygame.locals import *
from data.gameplay.player import Player
from data.gameplay.plataforma import Plataform
from data.gameplay.enimy.wizard import WizardSimpleAI as Wizard
from data.gameplay.headUpDisplay import HeadUpDisplay as H_u_d


class GamePlay(object):
    def __init__(self, screen, nivel, lastPassPoint,qtlife, pygameEvent):
        self.screen = screen
        self.nivel = nivel
        self.lastPassPoint = lastPassPoint
        self.qtlife = qtlife
        self.pygameEvent = pygameEvent
        self.player = Player(self.screen, self.nivel, self.lastPassPoint)
        self.wizard = Wizard(self.screen)
        self.headUpDisplay = H_u_d(self.screen, self.nivel, self.lastPassPoint, self.qtlife)
        self. nivel = 1 # default value of the level started usualy in 1 
        self.skills = 1 # default value of skills the player have
        self.lastPassPoint = 500 # default Value for position of the player in the platform
        self.player_rect = pygame.Rect(0, 0, 0, 0) # To control the player rects
        self.scroll = [0, 0]  # Variable to control the scroll of the screen
    
    # method to display all the components in the platform
    def drawingTheGamePlayEnvirement(self):
        plataforma = Plataform(self.screen)
        tile_rects, tile_item = plataforma.settingPlataform(self.scroll)
        self.headUpDisplay.headUpDisplayScreenDraw(self.lastPassPoint)
        
        self.scroll, player_rect = self.player.settingPlayer(self.pygameEvent, tile_rects,tile_item, self.scroll)
        wizard_rect = self.wizard.activation(self.pygameEvent, tile_rects, self.scroll, player_rect)
        # tile_rects.append(wizard_rect)
        tile_rects.append(player_rect)

        self.lastPassPoint = player_rect.x