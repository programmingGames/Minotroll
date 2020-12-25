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
        self.arrowsPosition = [(110, 180), (553, 180)]
        self.backgrounds = Back(screen)
        self.allCard = []
        # self.timeEfect = 0
        self.cards = ['kickingCard', 'slashingCard', 'battleaxCard','handCard', 'smollfirecard', 'fireCard', 'bluefireCard']
        self.state = [False, False,False,False,False,False,False]
        self.skillsOfPlayer()
        self.skillsControl = []
        self.allCardsPosition = []
        self.cardsActive = True
        self.backButtom = ''
        self.currentCard = self.cards[int(len(self.cards)/2)]
        self.count = 0

    # Method to make a list it a option in skills
    def displayButtoms(self):
        self.allCard = []
        self.allCardsPosition = []
        self.arrows = []
        right = []
        self.x, self.y = 168, 150
        count = 0
        for (card, state) in zip(self.cards, self.state):
            if(self.currentCard == card):
                if self.cardsActive:
                    img1 = pygame.image.load("resources/image/skills/"+self.currentCard+"2-"+str(state)+".png").convert_alpha()
                    self.arrows.append(pygame.image.load("resources/image/skills/leftarrow1.png").convert_alpha())
                    self.arrows.append(pygame.image.load("resources/image/skills/rightarrow1.png").convert_alpha())
                    self.backButtom = pygame.image.load("resources/image/skills/back1.png").convert_alpha()
                else:
                    img1 = pygame.image.load("resources/image/skills/"+self.currentCard+"0.png").convert_alpha()
                    self.arrows.append(pygame.image.load("resources/image/skills/leftarrow0.png").convert_alpha())
                    self.arrows.append(pygame.image.load("resources/image/skills/rightarrow0.png").convert_alpha())
                    self.backButtom = pygame.image.load("resources/image/skills/back2.png").convert_alpha()
                self.x = 450
            else:
                img = pygame.image.load("resources/image/skills/"+card+"1.png").convert_alpha()
                if(count < self.cards.index(self.currentCard)):
                    self.allCard.append(img)
                    self.allCardsPosition.append((self.x, self.y))
                    self.x += 40
                elif(count > self.cards.index(self.currentCard)):
                    right.append(img)
                    self.allCardsPosition.append((self.x, self.y))
                    self.x -= 40
            count += 1
        self.allCard += right[::-1]
        self.x, self.y = 300, 134
        self.allCard.append(img1)
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
        count = 0
        for state in self.state:
            if(count < self.nivel-1):
                self.state[count] = not state
            if (self.nivel == 2):
                n = self.state[count]
                if(self.state.index(n)<=1):
                    self.state[count] = not state
            count += 1

    # move cards to right
    def movingLeftInSkillsDisplay(self):
        # move in the cards list
        fistscardcopy = self.cards[0]
        restcardscopy = self.cards[1:len(self.cards)]
        restcardscopy.append(fistscardcopy)
        self.cards = restcardscopy  

        # move in the state list
        fistsstatecopy = self.state[0]
        reststatescopy = self.state[1:len(self.state)]
        reststatescopy.append(fistsstatecopy)
        self.state = reststatescopy  



    # move cards to left
    def movingRightInSkillsDisplay(self):
        # move in the cards list
        restcardscopy = []
        lastcardcopy = self.cards[int(len(self.cards)-1)]
        restcardscopy.append(lastcardcopy)
        restcardscopy += self.cards[0:len(self.cards)-1]
        self.cards = restcardscopy

        # move in the state list
        reststatescopy = []
        laststatecopy = self.state[int(len(self.state)-1)]
        reststatescopy.append(laststatecopy)
        reststatescopy += self.state[0:len(self.state)-1]
        self.state = reststatescopy

    # method to move only on the skills display
    def movingInSkillsDsiplay(self):
        key_pressed = pygame.key.get_pressed()     

        # Setting the move in skill Cards
        if(self.cardsActive and key_pressed[K_RIGHT] and (self.count > 10)):
            self.movingLeftInSkillsDisplay()
            self.count = 0
        elif(self.cardsActive and key_pressed[K_LEFT] and (self.count > 10)):
            self.movingRightInSkillsDisplay()
            self.count = 0

        self.count += 1                
        self.currentCard = self.cards[int(len(self.cards)/2)]

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
