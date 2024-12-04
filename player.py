#Chapter 2, Part 5
from circleshape import * #imported from circleshape.py
from constants import * #imported from constants.py

class Player(CircleShape):
    containers = []

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS) #pulling data from circleshape
        self.rotation = 0
        
        for group in Player.containers:
            group.add(self)

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

    def rotate(self, dt, direction): #grabs data from delta to create speed and direction
        self.rotation += PLAYER_TURN_SPEED * dt * direction 

    def update(self, dt):
        keys = pygame.key.get_pressed() #grabs key press data

        if keys[pygame.K_a]:
            self.rotate(dt, -1) #negative forces left, using a key
        if keys[pygame.K_d]:
            self.rotate(dt, 1) #positive forces right, using d key
        if keys[pygame.K_w]:
            self.move(dt,1)
        if keys[pygame.K_s]:
            self.move(dt,-1)

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction