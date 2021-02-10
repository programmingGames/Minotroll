import pygame
import random

# Class to display random animation on the screen
class Animation(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.itemName = 'sheets'
        self.count = 0
        self.items = []
        self.suport = []

    # Method to draw the animation
    def draw(self):
        if(self.itemName != None):
            self.createNewItems()
        [item.draw() for item in self.items]
        [item.draw() for item in self.suport]

    # Method to create new animation elemente and delete the old ones to best memory managment
    def createNewItems(self):
        if (self.count >= 100):
            if(len(self.items) >= 160):
                self.suport = self.items
                self.items = [Item(self.itemName, self.screen) for b in range(random.randint(10,30))]
            else:
                [self.items.append(Item(self.itemName, self.screen)) for b in range(random.randint(10,30))]
            self.count = 0
        else:
            self.count += 1            

# Class that represente elementes items
class Item:
    def __init__(self, nameItem, screen):
        self.screen = screen
        self.y = random.randint(0, 430)
        self.angulo_x = random.randint(1, 2)
        self.angulo_y = random.randint(1, 2)
        self.imgNb = random.randint(1, 6)
        aux = [-1, 1]
        self.side = random.choice(aux)
        self.randomApperingPosition()
        self.sinal_x = random.choice(aux)
        self.sinal_y = random.choice(aux)
        self.item = pygame.image.load("resources/image/animation/"+str(nameItem)+"/"+str(self.imgNb)+".png")
    
    # Method to draw the items
    def draw(self):
        self.screen.blit(self.item, (self.x, self.y))
        self.x -= self.angulo_x * self.sinal_x
        self.y -= self.angulo_y * self.sinal_y

    # Method to choice in random form the position of the item
    def randomApperingPosition(self):
        if (self.side == -1):
            self.x = random.randint(-20, -10)
        else:
            self.x = random.randint(710, 720)
