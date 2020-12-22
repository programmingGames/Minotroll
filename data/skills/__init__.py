import pygame
from sys import exit
from pygame.locals import *
from data.backgrounds import Backgound as Back


class Skills(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.painel = pygame.image.load("resources/image/menu/user_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.backgrounds = Back(screen)
        self.allCard = []
        # self.timeEfect = 0
        self.cards = ['kickingCard', 'slashingCard', 'battleaxCard','handCard', 'smollfirecard', 'fireCard', 'bluefireCard']
        self.allPosition = []
        self.activeCard = False
        self.currentCard = self.cards[int(len(self.cards)/2)]

    # Method to make a list it a option in skills
    def displayButtoms(self):
        self.allCard = []
        self.allPosition = []
        self.x, self.y = 130, 180
        reversCard = self.cards[::-1]
        leftCards = self.cards[0:int(len(self.cards)/2)]
        rightCards = reversCard[0:int(len(reversCard)/2)]
        rightCards = rightCards[::-1]
        for card in leftCards:
            img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
            self.x += 40
            self.allCard.append(img)
            self.allPosition.append((self.x, self.y))

        self.x = 480

        for card in rightCards:
            img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
            self.x -= 40
            self.allCard.append(img)
            self.allPosition.append((self.x, self.y))

        img = pygame.image.load("resources/image/skills/"+self.currentCard+"0.png").convert_alpha()
        self.x, self.y = 295, 153

        self.allCard.append(img)
        self.allPosition.append((self.x, self.y))
            # if(self.currentCard == card):
            #     img = pygame.image.load("resources/image/skills/"+card+"0.png").convert_alpha()
            #     self.x += 40
            #     self.activeCard = True
            # else:
            #     img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
            #     if self.activeCard:
            #         self.x += 135
            #         self.activeCard = False
            #     else:
            #         self.x += 40
                
            # print(self.x)
            
        # exit()

    # method to draw the painel skills on the screen
    def drawingSkillsPainel(self):
        self.backgrounds.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (52, 50))
        self.screen.blit(self.title, (270, 60))
        pass

    # method to Know, how many skills the player already have
    def skillsOfPlayer(self):
        pass

    # method to move only on the skills display
    def movingInSkillsDsiplay(self):
        pass

    # method to move in the painel of the skills
    def movingInPainelSkills(self):
        self.displayButtoms()
        self.drawingSkillsPainel()
        # print(self.currentCard)
        [self.screen.blit(card, pos) for card, pos in zip(self.allCard, self.allPosition)]

    # method of tuturial of the skills
    def skillsTuturial(self):
        pass
