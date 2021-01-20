import pygame 
from data.gameplay.headUpDisplay.rects import Rects

class LevelProgress(object):
    def __init__(self, screen, lastPassPoint):
        self.screen = screen
        self.progressBox = pygame.image.load("resources/image/headUpDisplay/conteiner/progressBox.png")
        self.currentProgress = int(((lastPassPoint - 500)*160)/10000)
        self.progressRect = Rects(self.screen, self.currentProgress, 23, 98, 62,(0,69,246))
        self.start = True

    def draw(self, currentLastPassPoint):
        # if(self.start):
        #     self.progressRect.drawSelectColor(self.currentProgress)
        #     self.start = not self.start 
        # else:
        #     if self.currentProgress in range(0,160):
        #         self.currentProgress = int(((currentLastPassPoint - 500)*160)/10000)
        #         self.progressRect.drawSelectColor(self.currentProgress)
        # self.screen.blit(self.progressBox, (90, 55))  
        pass