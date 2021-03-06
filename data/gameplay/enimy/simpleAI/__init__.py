import random

# Class of the state machine
class SimpleEnimysAI:
    def __init__(self, patrolingRadius,attackRadius, position):
        # self.allEnimys = ['blue wizard', 'fire golem', 'stone golem', 'ice golem', 'blue minotaur', 'graveller']
        self.patrolRadius = patrolingRadius
        self.attackRadius = attackRadius
        self.attacking = False
        self.move_right = False
        self.move_left = False
        self.initialPosition = position
        self.position = position
        self.direction = random.choice(('right', 'left'))
        self.timer = 0 

    # Method that activate the caracter move acording ti the state
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

    # Method that calculate the player proximity
    def calculateProximity(self, player_rect):
        if(((self.enimy_rect.x-player_rect.x)<=self.attackRadius)and((self.enimy_rect.x-player_rect.x)>= -1*self.attackRadius)):
                if player_rect.y in range(self.enimy_rect.y-80, self.enimy_rect.y+50):
                    self.attacking = True  
                else:
                    self.attacking = False          
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

    # Method thar choice the caracter state
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
