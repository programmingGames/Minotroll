import pygame
from pygame.locals import *
from data.vector import Vector2

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.air_timer = 0
        self.vertical_momentum = 0
        self.player_move = [0, 0]
        self.player = pygame.image.load("resources/image/Golem/Walking/0_Goblin_Walking_000.png").convert_alpha()
        self.player_rect=pygame.Rect(50, 200, 5, 13)
        # self.player_rect=pygame.Rect(50, 325, 5, 13)
    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if (self.player_rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list
    def playerCollision(self, tile_rects, collision, rect):
        collision_types = collision
        
        # Testando as colissões
        rect.x += self.player_move[0]
        hit_list = self.collision_test(tile_rects)
        for tile in hit_list:
            if (self.player_move[0] > 0):
                self.player_rect.right = tile.left
                collision_types['right'] = True
            elif (self.player_move[0] < 0):
                self.player_rect.left = tile.right
                collision_types['left'] = True

        rect.y += self.player_move[1]
        print(rect)
        hit_list = self.collision_test(tile_rects)
        for tile in hit_list:
            if (self.player_move[1] > 0):
                self.player_rect.bottom = tile.top
                collision_types['bottom'] = True
            elif (self.player_move[1] < 0):
                self.player_rect.top = tile.bottom
                collision_types['top'] = True
        
        return collision_types, rect
        
    def settingPlayer(self, press_keys, tile_rects, collision):    
        self.player_move[1] += self.vertical_momentum
        self.initialY = self.player_move[1]
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 0.2

        collisions, self.player_rect = self.playerCollision(tile_rects, collision, self.player_rect)

        if (collisions['bottom'] == True):
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
        
        if(self.player_rect.y >= 320):
            self.player_rect.y = 300
            self.screen.blit(self.player, (self.player_rect.x, self.player_rect.y))
        else:
            self.screen.blit(self.player, (self.player_rect.x, self.player_rect.y))
        

        if (press_keys[K_RIGHT]):
            self.player_move[0] += 1
            # self.player_move.moveXpositive(1)
        if (press_keys[K_LEFT]):
            self.player_move[0] -= 2
             # self.player_move.moveXnegative(1)
        if (press_keys[K_UP]):
            if self.air_timer < 6:
                self.vertical_momentum = -5
            # pygame.time.delay(100)
            # if event.type == KEYUP:
            #     if event.key == K_RIGHT:
            #         pass
            #         # self.player_move.moveXpositive(2)
            #     if event.key == K_LEFT:
            #         # self.player_move[0] -= 2
            #         pass
            #         # self.player_move.moveXnegative(2)
                    