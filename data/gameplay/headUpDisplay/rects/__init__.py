import pygame

# Method to draw the life rect
class Rects:
    def __init__(self, screen, width,height, x, y, color):
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.lifeGradientColor = [(0,255,0), (124,255,0), (228,255,0), (255,139,0), (255,44,0), (255,0,0), (158, 0, 0)]
        self.x = x
        self.y = y

    # Method that control the gradient effect
    def drawGradientEffect(self, color, qtlife):
        self.width = qtlife
        pygame.draw.rect(self.screen, self.lifeGradientColor[color], pygame.Rect(self.x, self.y, self.width,self.height))
    
    # Method the draw a recrt whithout gradient effect
    def drawSelectColor(self, progress):
        self.width = progress
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width,self.height))
        