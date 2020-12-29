import pygame

class Rects:
    def __init__(self, screen, width,height, x, y, color):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def rectDraw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width,self.height))

    def setColor(self):
        return (0,255, 0)