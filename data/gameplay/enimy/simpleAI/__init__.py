import random

class SimpleEnimysAI:
    def __init__(self, screen, patrolingRadius,attackRadius, position):
        # self.allEnimys = ['blue wizard', 'fire golem', 'stone golem', 'ice golem', 'blue robots', 'dark robots', 'gold robots']
        self.patrolRadius = patrolingRadius
        self.attackRadius = attackRadius
        self.attacking = False
        self.move_right = False
        self.move_left = False
        self.initialPosition = position
        self.position = position
        self.direction = 'right'
        self.timer = 0 
        


    def activation(self, enimy_rect, player_rect):
        self.enimy_rect = enimy_rect
        if(self.timer == 50):
            self.choisingMove()
            self.calculateProximity(player_rect)
            self.timer = 0
        else:
            self.timer += 1

        # Controlling the radius of patroling
        if((self.enimy_rect.x - self.position)>self.patrolRadius):
                self.move_right = False
        elif((self.enimy_rect.x - self.position)<(-1*self.patrolRadius)):
            self.move_left = False

        
        return self.direction, self.move_right, self.move_left, self.attacking

    # calculating the proximity
    def calculateProximity(self, player_rect):
        if(((self.enimy_rect.x-player_rect.x)<=self.attackRadius)and((self.enimy_rect.x-player_rect.x)>= -1*self.attackRadius)):
            self.attacking = True            
        else:
            self.attacking = False 

        if(self.attacking):
            if(self.enimy_rect.x > player_rect.x):
                self.direction = 'left'
                self.move_left = True
                self.move_right = False
            else:
                self.direction = 'right'
                self.move_left = False
                self.move_right = True


    def choisingMove(self):
        rand = random.random()
        if (rand<0.4):
            self.direction = 'left'
            self.move_right = False
            self.move_left = True
        elif((rand>=0.4)and(rand<0.8)):
            self.move_left = False
            self.move_right = False
        else:
            self.direction = 'right'
            self.move_left = False
            self.move_right = True