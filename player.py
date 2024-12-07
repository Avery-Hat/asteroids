#Chapter 2, Part 5
from circleshape import * #imported from circleshape.py
from constants import * #imported from constants.py
from shot import Shot #importing bullet from shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS) #pulling data from circleshape
        self.rotation = 0
        self.shoot_timer = 0 #timer variable for bullet rate of fire; Chapter 3, part 4

    # in the player class, given from chapter 2, part 5
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #drawing character as triangle
        pygame.draw.polygon(screen,"white",self.triangle(),2) #surface,color,points,width

    def move(self, dt, direction): #grabs delta and creates mvmt for up/down
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def rotate(self, dt, direction): #grabs data from delta to create speed and direction
        self.rotation += PLAYER_TURN_SPEED * dt * direction 

    def update(self, dt):
        keys = pygame.key.get_pressed() #grabs key press data
        self.shoot_timer -= dt #new variable for bullet rate of fire; Chapter 3, part 4

        if keys[pygame.K_a]:
            self.rotate(dt, -1) #negative forces left, using a key
        if keys[pygame.K_d]:
            self.rotate(dt, 1) #positive forces right, using d key
        if keys[pygame.K_w]: #moves character forward with W key
            self.move(dt,1)
        if keys[pygame.K_s]: #moves character backwards with S key
            self.move(dt,-1)
        if keys[pygame.K_SPACE]: #shoots bullets upon pressing SPACE
            self.shoot()

    def shoot(self): #bullets positioning, places in character and shoots from tip of triangle
        if self.shoot_timer > 0: #creates shooting rate of fire
            return
        self.shoot_timer = PLAYER_SHOOT_COUNTDOWN #set at 0.3 seconds from constants.py

        x = self.position[0]
        y = self.position[1]
        shot = Shot(x, y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED