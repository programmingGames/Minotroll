import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back


class Skills(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.backgrounds = Back(screen)
        self.allButtom = []
        self.timeEfect = 0
        self.buttoms = []
        self.currentButtom = ''

    # Method to make a list it a option in skills
    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)
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
