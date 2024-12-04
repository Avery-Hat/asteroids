# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #importing all, per course instructions.
from player import Player #importing the character model

def main():
    pygame.init() #initialized
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #720p
    running = True
    clock = pygame.time.Clock() #new variable for FPS
    dt = 0 #delta time
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while running: #inf loop to keep game running
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False #makes game quit
        screen.fill("black") #making background black
        dt = clock.tick(60)/1000 #converting to seconds, and FPS set to 60
        player.draw(screen)
        pygame.display.flip() #always at the bottom
        
        
    pygame.quit()

if __name__ == "__main__":
    main()