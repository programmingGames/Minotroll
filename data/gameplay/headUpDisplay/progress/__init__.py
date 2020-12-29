import pygame 
from data.gameplay.headUpDisplay.rects import Rects

class LevelProgress(object):
    def __init__(self, screen, lastPassPoint):
        self.screen = screen
        self.lastPassPoint = lastPassPoint
        self.progressBox = pygame.image.load("resources/image/headUpDisplay/conteiner/progressBox.png")
        self.progressArray = []
        self.x = 98
        self.y = 62
        self.progressCalculum()
        # self.maxPosition = 5000
        self.start = True

    def draw(self, lastPassPoint):
        if(self.start):
            self.initialProgress()
            self.start = not self.start 
        else:
            self.updatePorgress(lastPassPoint)
        
        [progress.rectDraw() for progress in self.progressArray]
        self.screen.blit(self.progressBox, (90, 55))

    def updatePorgress(self, currentLastPassPoint):
        self.lastPassPoint = currentLastPassPoint
        lastProgres = self.currentProgress
        self.progressCalculum()
        for i in range(self.currentProgress - lastProgres):
            if(self.currentProgress <= 160):
                progress = Rects(self.screen, 1, 23, self.x, self.y,(0,69,246))
                self.progressArray.append(progress)
                self.x += 1

    def initialProgress(self):
        for i in range (self.currentProgress):
            progress = Rects(self.screen, 1, 23, self.x, self.y,(0,69,246))
            self.progressArray.append(progress)
            self.x += 1
    def progressCalculum(self):
        self.currentProgress = int(((self.lastPassPoint - 500)*160)/10000)