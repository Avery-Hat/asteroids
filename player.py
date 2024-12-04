#Chapter 2, Part 5
from circleshape import * #imported from circleshape.py
from constants import PLAYER_RADIUS #imported from constants.py

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS) #pulling data from circleshape
        self.rotation = 0

    # in the player class, given from chapter
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #drawing character as triangle
        pygame.draw.polygon(screen,"white",self.triangle(),2) #surface,color,points,width