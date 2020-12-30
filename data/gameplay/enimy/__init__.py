import random

class SimpleEnimysAI:
    def __init__(self, screen, patrolingRadius, position):
        self.patrolRadius = patrolingRadius
        self.attacking = False
        self.move_right = False
        self.move_left = False
        self.initialPosition = position
        self.position = position
        self.direction = 'right'
        self.timer = 0 
        
    def activation(self, enimy_rect):
        if(self.timer == 50):
            self.choisingMove()
            self.timer = 0
        else:
            self.timer += 1
        
        # Controlling the radius of patroling
        if((enimy_rect.x - self.position)>self.patrolRadius):
                self.move_right = False
        elif((enimy_rect.x - self.position)<(-1*self.patrolRadius)):
            self.move_left = False

        return self.direction, self.move_right, self.move_left, self.attacking

    # Next time i'm going to do this part here
    def calculateProximity(self, player_rect):
        if((self.position-player_rect.x)<=80):
            return True
        else:
            return False 

    def choisingMove(self):
        rand = random.random()
        if (rand<0.3):
            self.direction = 'left'
            self.move_right = False
            self.move_left = True
        elif((rand>=0.3)and(rand<0.7)):
            self.move_left = False
            self.move_right = False
        else:
            self.direction = 'right'
            self.move_left = False
            self.move_right = True