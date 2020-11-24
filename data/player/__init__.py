import pygame
from pygame.locals import *
from data.vector import Vector2

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.air_timer = 0
        self.vertical_momentum = 0
        self.player_move = [0, 0]
        self.player_img = pygame.image.load("resources/image/Golem/Walking/0_Goblin_Walking_000.png").convert_alpha()
        self.player_rect=pygame.Rect(50, 200, 5, 13)
        self.moving_right = False
        self.moving_left = False
        self.vertical_momentum = 0
        self.air_timer = 0
        

    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if (rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

    def playerMove(self,rect,movement,tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += movement[0]
        hit_list = self.collision_test(rect,tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = self.collision_test(rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
        
    def settingPlayer(self, event, tile_rects, scroll):
        player_movement = [0,0]
        if self.moving_right == True:
            player_movement[0] += 3
        if self.moving_left == True:
            player_movement[0] -= 3
        player_movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 4:
            self.vertical_momentum = 4

        self.player_rect,collisions = self.playerMove(self.player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1

        self.screen.blit(self.player_img,(self.player_rect.x-scroll[0],self.player_rect.y-scroll[1]))

        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.moving_right = True
                if event.key == K_LEFT:
                    self.moving_left = True
                if event.key == K_UP:
                    if self.air_timer < 8:
                        self.vertical_momentum = -7
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.moving_right = False
                if event.key == K_LEFT:
                    self.moving_left = False
        scroll[0] += (self.player_rect.x-scroll[0]-365)/20
        scroll[1] += (self.player_rect.y-scroll[1]-260)/20

        correct_scroll = scroll.copy()
        correct_scroll[0] = int(correct_scroll[0])
        correct_scroll[1] = int(correct_scroll[1])
        return scroll
    def walk(self):
        pass
    def jump(self):
        pass
    def hurt(self):
        pass
    def die(self):
        pass
    def kiking(self):
        pass
    def slashing(self):
        pass
    def sliding(self):
        pass
    def throwing(self):
        pass
    def idle(self):
        pass
                        
