import pygame
from constants import *
from circleshape import CircleShape
#data copied from asteroid.py, used for bullets
#changed radius to its own using new variable in constants.py called SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        #copying parts of draw for the space laser
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt