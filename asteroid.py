#Chapter 3, part 1
import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) #grabbing from circleshape
        

    def draw(self, screen):
        #copying parts of draw for the aestroid
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

