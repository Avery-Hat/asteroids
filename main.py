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
    updateable_group = pygame.sprite.Group() #created group for updated items (e.g. deltatime)
    drawable_group = pygame.sprite.Group() #created group for drawable items (e.g. char model)
    Player.containers = (updateable_group, drawable_group) #putting player with both groups
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) #the character itself

    while running: #inf loop to keep game running
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False #makes game quit
        screen.fill("black") #making background black
        dt = clock.tick(60)/1000 #converting to seconds, and FPS set to 60
        for obj in updateable_group: 
            obj.update(dt) #made updateable group with delta
        for obj in drawable_group:
            obj.draw(screen) #made drawable group with screen (character model)
        pygame.display.flip() #always at the bottom
        
        
    pygame.quit()

if __name__ == "__main__":
    main()