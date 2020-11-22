import pygame
from data.vector import Vector2

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_move = Vector2(0, 0)
        self.player = pygame.image.load("resources/image/Golem/Walking/0_Goblin_Walking_000.png").convert_alpha()
        self.player_rect=pygame.Rect(100, 100, 5, 13)
    def playerMove(self, press_key, tile_rects):
        if
        pass