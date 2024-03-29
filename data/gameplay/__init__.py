import pygame
from pygame.locals import *
import os
from data.music import Sounds
from data.gameplay.headUpDisplay import HeadUpDisplay as H_u_d
from data.gameplay.lifeItem import LifeItemAndPlants as LifeAndPlants
from data.gameplay.enimy import ControlEnimys
from data.gameplay.animation import Animation
from data.gameplay.player import Player
from data.gameplay.platforms import Plataform


# Class that control the game envirement
class GamePlay(object):
    def __init__(self, screen, nivel, lastPassPoint,qtlife, pygameEvent, enimysKilled, greenFire, blueFire):
        # self.allEnimys = ['blue wizard', 'fire golem', 'stone golem', 'ice golem', 'blue robots', 'dark robots', 'gold robots']
        self.screen = screen
        self.nivel = nivel
        self.lastPassPoint = lastPassPoint
        self.qtlife = qtlife
        self.pygameEvent = pygameEvent
        self.greenFire = greenFire
        self.blueFire = blueFire
        self.currentEnimysKilled = enimysKilled
        self.enimys = ControlEnimys(self.screen, self.nivel, enimysKilled)
        self.sounds = Sounds()
        self.animation = Animation(self.screen, self.nivel)
        self.headUpDisplay = H_u_d(self.screen, self.nivel, self.lastPassPoint, self.qtlife)
        self.player = Player(self.screen, self.nivel, self.lastPassPoint)
        self.platform = Plataform(self.screen, self.nivel)
        self.liveItem = LifeAndPlants(self.screen, self.nivel)
        self.tutorialParts = 0
        self.showTutorial = False
        self.hiddeBackTutorial = False
        self.tutorialCount = 0
        self.tutorialTab = False
        self. nivel = nivel # default value of the level started usualy in 0
        self.inUse = ''
        self.player_rect = pygame.Rect(0, 0, 0, 0) # To control the player rects
        self.scroll = [0, 0]  # Variable to control the scroll of the screen
        self.enimyCollision = False
        self.enimyType = ''
        self.allEnimysRectsAndTypes = []
        self.nrInimys = 0
        self.knowingEnimysNr()
        self.playerOnAttack = False
        self.bossKilled = False
        self.firing = False

        self.count = 0
        self.soundTimer = 0
        self.musicControl = True
        self.soundControl = True
        self.pos = 0

    def knowingEnimysNr(self):
        if(self.nivel==0):
            self.nrInimys = 16
        elif(self.nivel == 1):
            self.nrInimys = 21
        elif(self.nivel == 2):
            self.nrInimys = 18
        elif(self.nivel == 3):
            self.nrInimys = 4

    # method to display all the components in the platform
    def drawingTheGamePlayEnvirement(self, soundControl, musicControl):
        tile_rects = []
        self.soundControl = soundControl
        self.musicControl = musicControl
        
        tile_rects = self.platform.settingPlataform(self.scroll)
        
        self.scroll, self.player_rect,self.fireArray, self.enimyCollision, self.enimyType, self.fireEnimyColision, self.fireCollsionPos, self.playerOnAttack = self.player.settingPlayer(tile_rects, self.scroll, self.allEnimysRectsAndTypes, self.inUse)
        
        if ((self.playerOnAttack[0])and(self.count >= 10)and(self.inUse == "greenfire"  or self.inUse == "bluefire")):
            self.firing = True
            self.count = 0
        else:
            self.firing = False
        self.count += 1
        if self.firing:
            if(self.inUse == 'greenfire' and (self.greenFire > 0)):
                self.greenFire -= 1
            elif(self.inUse == 'bluefire' and (self.blueFire > 0)):
                self.blueFire -= 1
            
        # update after we check the collision
        self.allEnimysRectsAndTypes, self.enimysKilled, self.bossKilled = self.enimys.enimysAdd(tile_rects, self.player_rect,(self.fireEnimyColision, self.fireCollsionPos),(self.playerOnAttack[0],self.enimyCollision, self.inUse, self.playerOnAttack[1]), self.scroll)

        # Drawing some visual animation
        self.animation.draw()
        painelState, self.qtlife, self.inUse = self.headUpDisplay.headUpDisplayScreenDraw(self.player_rect.x, self.greenFire, self.blueFire, self.enimysKilled+self.currentEnimysKilled)

        self.itemLifeCollision = self.liveItem.drawingTheLifeItem(self.player_rect, self.scroll)
        
        self.controllingThePlayerLife()

        # controlling the end of the levels
        if((self.nivel == 0)or(self.nivel == 1)):
            if(self.player_rect.x >= 5460):
                if(self.enimysKilled >=10):
                    painelState = 13
                else:
                    painelState = 18
        elif(self.nivel==2):
            if(self.player_rect.x >= 6760):
                if(self.enimysKilled >=10):
                    painelState = 13
                else:
                    painelState = 18
        elif((self.nivel == 3)and(self.bossKilled)):
            painelState = 19

        # controlling the falling out of the game platform
        if(self.player_rect.y >= 720):
            painelState = 11

        key = pygame.key.get_pressed()
        if key[K_ESCAPE]:
            painelState = 8

        # tutorial display
        if((self.nivel == 0)and(self.lastPassPoint[0] <= 500)):
            self.showTutorial = True
        else:
            self.showTutorial = False
        
        if self.showTutorial:
            self.tutorial(key)
        self.lastPassPoint = (self.player_rect.x, self.player_rect.y)

        self.controllingTheImageOfGameOverAndLevelComplete(painelState)
        self.chekingSongs()

        return painelState, self.player_rect, self.qtlife, self.enimysKilled, self.greenFire, self.blueFire
    
    # Method that control the sounds
    def chekingSongs(self):
        if self.soundControl:
            if self.playerOnAttack[0] and self.inUse == "slashing" and self.soundTimer >= 20:
                self.soundTimer = 0
                self.sounds.golemSliding()
            elif self.playerOnAttack[0] and self.inUse == "battleax" and self.soundTimer >= 20:
                self.soundTimer = 0
                self.sounds.golemSlach()
            elif self.playerOnAttack[0] and self.inUse == "kicking" and self.soundTimer >= 10:
                self.soundTimer = 0
                self.sounds.golemKicking()
            elif self.firing:
                self.sounds.golemstartFire()
            elif self.enimyCollision:
                self.sounds.golemHurt()
            elif(self.qtlife <= 40):
                self.sounds.golemTiredOut()
        if self.musicControl:
                    self.sounds.envirementOne()
            
        self.soundTimer += 1

    # Method that control the life of the player
    def controllingThePlayerLife(self):
        if (self.enimyCollision and self.playerOnAttack[0] == False):
            self.headUpDisplay.updatingPlayerLife(self.enimyType)
        elif(self.enimyCollision and self.enimyType == "cactus"):
            self.headUpDisplay.updatingPlayerLife(self.enimyType)
            
        if self.itemLifeCollision:
            self.headUpDisplay.updatingPlayerLife('life plant')

    # Method that make an backgournd image to be show in level complet, pause menu, game over, ...
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
            img1 = pygame.image.load("resources/image/menu/levelComplet/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/levelComplet')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')

        elif(painelState == 18):
            os.chdir('resources/image/menu/levelincomplet')
            pygame.image.save(self.screen, "back.png")
            pygame.time.delay(100)
            os.chdir('../../../..')
            surf = pygame.Surface((700, 480))
            img = pygame.image.load("resources/image/menu/levelincomplet/back.png").convert_alpha()
            img1 = pygame.image.load("resources/image/menu/levelincomplet/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/levelincomplet')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')

        elif(painelState == 8):
            os.chdir('resources/image/menu/pause_menu')
            pygame.image.save(self.screen, "back.png")
            pygame.time.delay(100)
            os.chdir('../../../..')
            surf = pygame.Surface((700, 480))
            img = pygame.image.load("resources/image/menu/pause_menu/back.png").convert_alpha()
            img1 = pygame.image.load("resources/image/menu/pause_menu/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/pause_menu')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')
        elif(painelState == 19):
            os.chdir('resources/image/menu/congrats')
            pygame.image.save(self.screen, "back.png")
            pygame.time.delay(100)
            os.chdir('../../../..')
            surf = pygame.Surface((700, 480))
            img = pygame.image.load("resources/image/menu/congrats/back.png").convert_alpha()
            img1 = pygame.image.load("resources/image/menu/congrats/back1.png").convert_alpha()
            surf.blit(img, (0, 0))
            surf.blit(img1, (0, 0))
            os.chdir('resources/image/menu/congrats')
            pygame.image.save(surf, "back.png")
            os.chdir('../../../..')

    # Method that control a little display an the game tutorial
    def tutorial(self, key):
        ## controlling the key pressed
        if(key[K_TAB] and (self.tutorialParts == 0)):
            self.hiddeBackTutorial = True
            self.tutorialParts  = 1
            self.tutorialCount = 0
        elif(key[K_TAB] and (self.tutorialParts == 1)):
            self.tutorialTab = True
            self.hiddeBackTutorial = True
        elif((key[K_1] or key[K_2] or key[K_3] or key[K_4]or key[K_5]) and self.tutorialTab):
            self.hiddeBackTutorial = True
            self.tutorialParts = 2
            self.tutorialCount = 0
        elif(key[K_m] and (self.tutorialParts == 2)):
            self.hiddeBackTutorial = True
            self.tutorialParts = 3
            self.tutorialCount = 0
        elif((key[K_UP] or key[K_RIGHT] or key[K_LEFT])and(self.tutorialParts == 3)):
            self.hiddeBackTutorial = True
            self.tutorialParts = 4
            self.tutorialCount = 0
        elif(key[K_q] and (self.tutorialParts == 4)):
            self.hiddeBackTutorial = True
            self.tutorialParts = 5
            self.tutorialCount = 0



        ## controlling the display    
        if(self.tutorialParts == 0):
            if(not self.hiddeBackTutorial):
                self.screen.blit(pygame.image.load("resources/image/tutorial/back1.png").convert_alpha(), (0, 0))
                font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
                font.set_bold(True)
                size = pygame.font.Font.size(font, 'Press " TAB " key,')
                line = font.render('Press " TAB " key, ', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, 480/2-size[1]))
                size = pygame.font.Font.size(font, 'to see the skills available.')
                line = font.render('to see the skills available.', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+30))
        elif(self.tutorialParts == 1):
            if(not self.hiddeBackTutorial):
                self.screen.blit(pygame.image.load("resources/image/tutorial/back1.png").convert_alpha(), (0, 0))
                font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
                font.set_bold(True)
                size = pygame.font.Font.size(font, 'Press " TAB " key,')
                line = font.render('Press " TAB " key, ', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, 480/2-size[1]))
                size = pygame.font.Font.size(font, 'and then press keys "1", "2", ..., "5",')
                line = font.render('and then press keys "1", "2", ..., "5",', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+30))
                size = pygame.font.Font.size(font, 'to change the skills in use.')
                line = font.render('to change the skills in use.', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+60))

        elif(self.tutorialParts == 2):
            if(not self.hiddeBackTutorial):
                self.screen.blit(pygame.image.load("resources/image/tutorial/back1.png").convert_alpha(), (0, 0))
                font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
                font.set_bold(True)
                size = pygame.font.Font.size(font, 'Press " M " key,')
                line = font.render('Press " M " key,', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, 480/2-size[1]))
                size = pygame.font.Font.size(font, 'to show and hide the game Map.')
                line = font.render('to show and hide the game Map.', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+30))

        elif(self.tutorialParts == 3):
            if(not self.hiddeBackTutorial):
                self.screen.blit(pygame.image.load("resources/image/tutorial/back1.png").convert_alpha(), (0, 0))
                font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
                font.set_bold(True)
                size = pygame.font.Font.size(font, 'Press the direction keys:')
                line = font.render('Press the direction keys:', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, 480/2-size[1]))
                size = pygame.font.Font.size(font, '"left", "up" and "right",')
                line = font.render('"left", "up" and "right",', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+30))
                size = pygame.font.Font.size(font, 'to move on the screen.')
                line = font.render('to move on the screen.', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+60))
        elif(self.tutorialParts == 4):
            if(not self.hiddeBackTutorial):
                self.screen.blit(pygame.image.load("resources/image/tutorial/back1.png").convert_alpha(), (0, 0))
                font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
                font.set_bold(True)
                size = pygame.font.Font.size(font, 'Press " Q " key, to attack.')
                line = font.render('Press " Q " key, to attack.', True, (255, 255,255))
                self.screen.blit(line, (700/2-size[0]/2, (480/2-size[1])+60))

        ## controlling the timer
        if(self.tutorialCount >= 30):
            self.tutorialCount = 0
            self.hiddeBackTutorial = False
            if(self.tutorialParts == 5):
                self.showTutorial = False
        else:
            self.tutorialCount += 1
