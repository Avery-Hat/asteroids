# this allows us to use code from
# the open-source pygame library
# throughout this file
#project made with Boot.Dev - Asteroids section
import pygame
import sys
from constants import * #importing all, per course instructions.
from player import Player #importing the character model
from asteroid import Asteroid #chapter 3, part 1
from asteroidfield import AsteroidField #chapter 3, part 1, section 7
from shot import Shot #importing bullet from shot
from score import Score #importing score screen new

def main():
    pygame.init() #initialized
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #720p
    running = True
    clock = pygame.time.Clock() #variable for FPS
    dt = 0 #delta time
    score_display = Score()

    updatable_group = pygame.sprite.Group() #created group for updated items (e.g. deltatime)
    drawable_group = pygame.sprite.Group() #created group for drawable items (e.g. char model)
    asteroids = pygame.sprite.Group() #from asteroids.py, setting up asteroids
    shots = pygame.sprite.Group() #from player.py, setting up player's space laser ~~
    score = pygame.sprite.Group() #new, from score.py, setting up player score

    Player.containers = (updatable_group, drawable_group) #putting player with both groups
    Shot.containers = (shots, updatable_group, drawable_group) #space lasers put in groups ~~
    Asteroid.containers = (asteroids, updatable_group, drawable_group) #from asteroids.py
    AsteroidField.containers = (updatable_group,) #kept as tuple for consistency
    asteroid_field = AsteroidField() #asteroidfield.py import
    Score.containers = (score, updatable_group, drawable_group) #new
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) #the character itself

    while running: #inf loop to keep game running
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False #makes game quit
        screen.fill("black") #making background black
        dt = clock.tick(60)/1000 #converting to seconds, and FPS set to 60
        score_display.show_score(screen) #showing game points, new
        for obj in asteroids: #checks for collision between player and astroid
            if obj.collision(player) == True:
                print("Game Over!")
                print(f"Your score : {score_display.count}") #adding total score at the end. new
                sys.exit()  #quits game upon collision
        for obj in asteroids: #loop for asteroid destruction upon impact; Ch3,P6
            for bullet in shots: #loop for bullet destruction upon impact
                if bullet.collision(obj) == True: #checks for collision between shot and asteroid
                    bullet.kill() #destroys bullet upon impact
                    obj.split() #splitting asteroid
                    score_display.score_up() #new, adding score upson bullet collision
        for obj in updatable_group: 
            obj.update(dt) #made updateable group with delta
        for obj in drawable_group:
            obj.draw(screen) #made drawable group with screen (character model)
        pygame.display.flip() #always at the bottom
        

        
    pygame.quit()

if __name__ == "__main__":
    main()