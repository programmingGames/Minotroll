
import pygame 
from random import randint
from pygame.locals import * 
from data.backgrounds import Backgound as Back
from data.gameplay.headUpDisplay.rects import Rects

class Initiation:
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.loading = pygame.image.load("resources/image/background/loading.png")
        self.loadRect = Rects(self.screen,160,9,(700/2-150/2),315,(46,170,0))
        self.font = pygame.font.SysFont("Arial", 11)
        self.font.set_bold(True)
        self.frame = 1
        self.dicas = [('Pressing buttom "M",', 'is possible to see your position in the map.'),
                    ('Pressing Tap buttom,','is possible to see the skills that you have, ','and pressing buttom 1, 2,3, ...,5', 'you can change the skills in use.'),
                    ('Using the arrows buttom,', 'all the player movement can be controled.'),
                    ('Using the fire skills, ', 'you can cause more damage to the enimy.'),
                    ('On the skills menu', 'you can see all the skills that you have.'),
                    ('Deleting your game profile, ', 'all your progress can lose.'),
                    ('When you exit game, ', 'the current progress is automatically save.'),
                    ('On the game settings, ','is possible to change some game settings.'),
                    ('The Wizard is a powerfull enimy, ', 'that with speed makes its dangerous attack.'),
                    ('There is diferent type of Golem, ','but the more dangerous is the Ice Golem.'),
                    ('The plant of life, ', 'not only give you life but it gives you more power.'),
                    ('The end of an level, ','comes when you pass the end mark whit life, ', 'and killed some enimys.'),
                    ('The most powerfull enimy is Graveler, ', 'so use or skills to defeat him.')
                ]
        print(len(self.dicas))
        self.randomText = self.dicas[randint(0, len(self.dicas)-1)]

    # Method to blit the start game font on the screen
    def settingStart(self):
        self.background.settingBackgroundMenu(1)
        self.screen.blit(self.loading, ((700/2-150/2)-5,310))
        if(self.frame == 150):
            return 1
        else:
            self.frame += 1
        self.loadprogress =  int (((self.frame * 139)/150))
        self.loadRect.drawSelectColor(self.loadprogress)

        ty = 340
        for paragrf in self.randomText:
            size = pygame.font.Font.size(self.font, str(paragrf))
            line = self.font.render(paragrf, True, (255, 255,255))
            self.screen.blit(line, ((700/2-size[0]/2)-4, ty))
            ty += 15

        return 0