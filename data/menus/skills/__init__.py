import pygame
from sys import exit
from pygame.locals import *
from data.backgrounds import Backgound as Back
from data.music import Sounds

class Skills(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.painel = pygame.image.load("resources/image/skills/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.arrows = []
        self.arrowsPosition = [(145, 160), (525, 160)]
        self.backgrounds = Back(screen)
        self.sounds = Sounds()
        self.allCard = []
        # self.timeEfect = 0
        self.cards = ['kickingCard', 'slashingCard', 'battleaxCard', 'fireCard', 'bluefireCard']
        self.description = [('5%', '5%', 'unlimited'), ('20%', '20%', 'unlimited'), ('30%', '25%', 'unlimited'), ('40%', '100%', 'limited'), ('45%', '100%', 'limited')]
        self.descrPos = 0
        self.copyCards = ['kickingCard', 'slashingCard', 'battleaxCard', 'fireCard', 'bluefireCard']
        self.state = [False,False,False,False,False]
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
        self.font.set_bold(True)
        self.cardsDiscription = ''
        self.skillsOfPlayer()
        self.skillsControl = []
        self.allCardsPosition = []
        self.cardsActive = True
        self.backButtom = ''
        self.currentCard = self.cards[int(len(self.cards)/2)]
        self.count = 0
        self.level = 0
        self.stateLock = False

    # Method to make a list it a option in skills
    def displayButtoms(self):
        self.allCard = []
        self.allCardsPosition = []
        self.arrows = []
        right = []
        img1 = ''
        self.x, self.y = 228, 130
        count = 0
        for (card, state) in zip(self.cards, self.state):
            if(self.currentCard == card):
                if self.cardsActive:
                    img1 = pygame.image.load("resources/image/skills/pergaminios/"+self.currentCard+"2-"+str(state)+".png").convert_alpha()
                    self.arrows.append(pygame.image.load("resources/image/skills/arrows/leftarrow1.png").convert_alpha())
                    self.arrows.append(pygame.image.load("resources/image/skills/arrows/rightarrow1.png").convert_alpha())
                    self.backButtom = pygame.image.load("resources/image/skills/Back1.png").convert_alpha()
                    self.stateLock = state
                else:
                    img1 = pygame.image.load("resources/image/skills/pergaminios/"+self.currentCard+"0.png").convert_alpha()
                    self.arrows.append(pygame.image.load("resources/image/skills/arrows/leftarrow0.png").convert_alpha())
                    self.arrows.append(pygame.image.load("resources/image/skills/arrows/rightarrow0.png").convert_alpha())
                    self.backButtom = pygame.image.load("resources/image/skills/Back2.png").convert_alpha()
                self.descrPos = count 
                self.cardsDiscription = pygame.image.load("resources/image/skills/description/pergaminio-"+str(state)+".png")
                self.x = 390
            else:
                img = pygame.image.load("resources/image/skills/pergaminios/"+card+"1.png").convert_alpha()
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
        self.x, self.y = 300, 114
        self.allCard.append(img1)
        self.allCardsPosition.append((self.x, self.y))
            
    # method to draw the painel skills on the screen
    def drawingSkillsPainel(self):
        self.backgrounds.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (75, 45))
        self.screen.blit(self.title, (270, 55))
        # cardName = pygame.image.load("resources/image/skills/"+self.currentCard+".png")
        # self.screen.blit(cardName, (270, 100))
        [self.screen.blit(card, pos) for card, pos in zip(self.allCard, self.allCardsPosition)]
        [self.screen.blit(arrows, pos) for arrows, pos in zip(self.arrows, self.arrowsPosition)]

        # display description
        
        self.screen.blit(self.backButtom, (260, 380))
        self.screen.blit(self.cardsDiscription, (225,240))
        ty = 280
        aux = ['Damage: ', 'Precision: ', 'Attempts: ']
        for text, text1 in zip(aux, self.description[self.descrPos]):
            size = pygame.font.Font.size(self.font, text+text1)
            line = self.font.render(text+text1, True, (0, 0,0))
            self.screen.blit(line, ((700/2-size[0]/2), ty))
            ty += 20

        self.levelToUnlockTheCards()
    # display of the level to unlock
    def levelToUnlockTheCards(self):
        count = 0
        for card in self.copyCards:
            if(card == self.currentCard):
                if(self.copyCards.index(card)==1):
                    self.level = count
                else:
                    self.level = count - 1
                break
            count += 1
        if(not self.stateLock):
            self.font.set_bold(True)
            line = self.font.render(str(self.level), True, (0, 0,0))
            self.screen.blit(line, (415, 253))

    # method to Know, how many skills the player already have
    def skillsOfPlayer(self):
        count = 0
        maxSkills = 0
        for state in self.state:
            if (self.nivel == 0):
                maxSkills = 2

            elif(self.nivel == 1):
                maxSkills = 4

            elif(self.nivel >= 2):
                maxSkills = 5

            n = self.state[count]
            if(self.state.index(n)<maxSkills):
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

        # move in the description
        fistsstatecopy = self.description[0]
        reststatescopy = self.description[1:len(self.description)]
        reststatescopy.append(fistsstatecopy)
        self.description = reststatescopy  

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

        # move in the description
        reststatescopy = []
        laststatecopy = self.description[int(len(self.description)-1)]
        reststatescopy.append(laststatecopy)
        reststatescopy += self.description[0:len(self.description)-1]
        self.description = reststatescopy

    # method to move only on the skills display
    def movingInSkillsDsiplay(self):
        key_pressed = pygame.key.get_pressed()     

        # Setting the move in skill Cards
        if(self.cardsActive and key_pressed[K_RIGHT] and (self.count > 10)):
            self.movingLeftInSkillsDisplay()
            self.sounds.skillschange()
            self.count = 0
        elif(self.cardsActive and key_pressed[K_LEFT] and (self.count > 10)):
            self.movingRightInSkillsDisplay()
            self.sounds.skillschange()
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
            self.sounds.upDownMenu()
            self.count = 0
        elif(key_pressed[K_UP] and not self.cardsActive and (self.count > 10)):
            self.cardsActive = True
            self.sounds.upDownMenu()
            self.count = 0

        # control the painelState
        if(not self.cardsActive and key_pressed[K_RETURN]):
            self.sounds.selected()
            return 3
        else:
            return 9
        
    # method of tuturial of the skills
    def skillsTuturial(self):
        pass
