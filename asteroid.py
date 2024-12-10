#Chapter 3, part 1
import pygame
import random #for asteroid splitting
from circleshape import *
from constants import * #grabbing data for asteroid splitting

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) #grabbing from circleshape
        

    def draw(self, screen):
        #copying parts of draw for the aestroid
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #making the split random, Chapter 3, part 6
        random_angle = random.uniform(20, 50) #to make two random angles for the new asteroids

        rotate1 = self.velocity.rotate(random_angle) #asteroid 1 angle
        rotate2 = self.velocity.rotate(-random_angle) #asteroid 2 

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius) #asteroid 1
        asteroid.velocity = rotate1 * 1.2
        asteroid = Asteroid(self.position.x,self.position.y, new_radius) #asteroid 2
        asteroid.velocity = rotate2 * 1.2


        