import pygame
from sys import exit
from pygame.locals import *
from data.backgrounds import Backgound as Back


class Skills(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.painel = pygame.image.load("resources/image/skills/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.arrows = []
        self.arrowsPosition = [(100, 180), (555, 180)]
        self.backgrounds = Back(screen)
        self.allCard = []
        # self.timeEfect = 0
        self.cards = {'kickingCard':False, 'slashingCard':False, 'battleaxCard':False,'handCard':False, 'smollfirecard':False, 'fireCard':False, 'bluefireCard':False}
        self.skillsControl = []
        self.allCardsPosition = []
        self.cardsActive = True
        self.backButtom = ''
        self.currentCard = self.cards[int(len(self.cards)/2)]
        self.count = 0

    # Method to make a list it a option in skills
    def displayButtoms(self):
        self.allCard = []
        self.allPosition = []
        self.arrows = []
        self.x, self.y = 130, 150
        reversCard = self.cards[::-1]
        leftCards = self.cards[0:int(len(self.cards)/2)]
        rightCards = reversCard[0:int(len(reversCard)/2)]
        rightCards = rightCards[::-1]
        for card in leftCards:
            img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
            self.x += 40
            self.allCard.append(img)
            self.allCardsPosition.append((self.x, self.y))
        self.x = 480
        for card in rightCards:
            img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
            self.x -= 40
            self.allCard.append(img)
            self.allCardsPosition.append((self.x, self.y))
        if self.cardsActive:
            img = pygame.image.load("resources/image/skills/"+self.currentCard+"2.png").convert_alpha()
            self.arrows.append(pygame.image.load("resources/image/skills/leftarrow1.png").convert_alpha())
            self.arrows.append(pygame.image.load("resources/image/skills/rightarrow1.png").convert_alpha())
            self.backButtom = pygame.image.load("resources/image/skills/back1.png").convert_alpha()
        else:
            img = pygame.image.load("resources/image/skills/"+self.currentCard+"0.png").convert_alpha()
            self.arrows.append(pygame.image.load("resources/image/skills/leftarrow0.png").convert_alpha())
            self.arrows.append(pygame.image.load("resources/image/skills/rightarrow0.png").convert_alpha())
            self.backButtom = pygame.image.load("resources/image/skills/back2.png").convert_alpha()
        self.x, self.y = 295, 134
        self.allCard.append(img)
        self.allCardsPosition.append((self.x, self.y))

    # method to draw the painel skills on the screen
    def drawingSkillsPainel(self):
        self.backgrounds.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (52, 35))
        self.screen.blit(self.title, (270, 45))
        cardName = pygame.image.load("resources/image/skills/"+self.currentCard+".png")
        self.screen.blit(cardName, (270, 100))
        [self.screen.blit(card, pos) for card, pos in zip(self.allCard, self.allCardsPosition)]
        [self.screen.blit(arrows, pos) for arrows, pos in zip(self.arrows, self.arrowsPosition)]
        self.screen.blit(self.backButtom, (250, 380))

    # method to Know, how many skills the player already have
    def skillsOfPlayer(self):
        pass
            

    # method to move only on the skills display
    def movingInSkillsDsiplay(self):
        key_pressed = pygame.key.get_pressed()     

        # Setting the move in skill Cards
        if(self.cardsActive and key_pressed[K_RIGHT] and (self.count > 10)):
            fistscardcopy = self.cards[0]
            self.currentCard = self.cards[len(self.cards)-1]
            restcardscopy = self.cards[1:len(self.cards)]
            restcardscopy.append(fistscardcopy)
            self.cards = restcardscopy
            self.count = 0
        elif(self.cardsActive and key_pressed[K_LEFT] and (self.count > 10)):
            restcardscopy = []
            lastcardcopy = self.cards[int(len(self.cards)-1)]
            restcardscopy.append(lastcardcopy)
            restcardscopy += self.cards[0:len(self.cards)-1]
            self.cards = restcardscopy
            self.currentCard = self.cards[int(len(self.cards)/2)]
            self.count = 0
        self.count += 1                

    # method to move in the painel of the skills
    def movingInPainelSkills(self):
        key_pressed = pygame.key.get_pressed()
        self.movingInSkillsDsiplay()
        self.displayButtoms()
        self.drawingSkillsPainel()

        # Setting the move in skills painel
        if (key_pressed[K_DOWN] and self.cardsActive and (self.count > 10)):
            self.cardsActive = False
            self.count = 0
        elif(key_pressed[K_UP] and not self.cardsActive and (self.count > 10)):
            self.cardsActive = True
            self.count = 0

        # control the painelState
        if(not self.cardsActive and key_pressed[K_RETURN]):
            return 3
        else:
            return 9
        
    # method of tuturial of the skills
    def skillsTuturial(self):
        pass