import pygame 


class Life:
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load("resources/image/life/conteiner-2.png").convert_alpha()
        self.lifeArray = []
        self.count = 1
        self.x = 34
        self.y = 28
        self.maxLife = 190

    def settingLife(self):
        pass
    def damage(self):
        pass
    def draw(self):
        self.initialLife()
        [life.rectDraw() for life in self.lifeArray]
        self.screen.blit(self.img, (10, 10))


    def initialLife(self):
        if(self.count <= self.maxLife):
            life = Rects(self.screen, self.count, self.x, self.y)
            self.lifeArray.append(life)
            
        self.count += 1
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