# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #importing all, per course instructions.

def main():
    pygame.init() #initialized
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #720p
    running = True
    black = (0, 0, 0)
    screen.fill(black) #making background black

    while running: #inf loop to keep game running
        for quit in pygame.event.get(): 
            if quit.type == pygame.QUIT:
                running = False #makes game quit
        pygame.display.flip() #always at the bottom
    
    pygame.quit()
if __name__ == "__main__":
    main()