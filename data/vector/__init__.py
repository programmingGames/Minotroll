import math
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    @staticmethod
    def from_points(x1,x2,y1,y2):

        return Vector2( x2-x1, y2-y1 )
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
    def moveXpositive(self, move):
        self.x += move
    def moveXnegative(self, move):
        self.x -= move
    def moveYpositive(self, move):
        self.y += move
    def moveYnegative(self, move):
        self.y -= move
    # rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)