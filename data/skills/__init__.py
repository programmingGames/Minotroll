import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back


class Skills(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.backgrounds = Back(screen)

    # method to draw the painel skills on the screen
    def drawingSkillsPainel(self):
        pass

    # method to Know, how many skills the player already have
    def skillsOfPlayer(self):
        pass

    # method to move in the painel of the skills
    def movingInPainelSkills(self):
        pass

    # method of tuturial of the skills
    def skillsTuturial(self):
        pass
    