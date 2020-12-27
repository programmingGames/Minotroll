import pygame 


class Life:
    def __init__(self, screen):
        self.screen = screen
        self.player = pygame.image.load("resources/image/headUpDisplay/conteiner/faceIcon.png")
        self.lifeBox = pygame.image.load("resources/image/headUpDisplay/conteiner/box1.png")
        self.progressBox = pygame.image.load("resources/image/headUpDisplay/conteiner/progressBox.png")
        self.lifeArray = []
        self.x = 34
        self.y = 28
        self.maxLife = 190
        self.count = 0
        self.start = True

    def settingLife(self):
        pass
    def damageLife(self, damage):
        for i in range(damage):
            self.lifeArray = self.lifeArray[:-1]
    def draw(self):
        # if (self.start):
        #     self.initialLife()
        #     self.start = False
        self.x = 34
        [life.rectDraw() for life in self.lifeArray]
        self.screen.blit(self.player, (10, 10))
        self.screen.blit(self.lifeBox, (95, 20))
        self.screen.blit(self.progressBox, (90, 55))


    def initialLife(self):
        for i in range (self.maxLife):
            life = Rects(self.screen, self.count, self.x, self.y)
            self.lifeArray.append(life)
            self.x += 1

        
class Rects:
    def __init__(self, screen, curv, x, y):
        self.screen = screen
        self.color = self.setColor()
        self.width = 1
        self.curv = curv
        self.x = x
        self.y = y
        self.height = 20

    def rectDraw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width,self.height))

    def setColor(self):
        return (0,255, 0)