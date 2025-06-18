import pygame 
import sys
# Initializing pygame 
pygame.init()

class BaiscInit():

    def set_screen(lenght, bredth):
        screen = pygame.display.set_mode((lenght, bredth))
        return screen

def main():
    # Making a window
    screen = BaiscInit.set_screen(800, 600)
    
    # this var determines if the program is running
    running = True
    
    # game loop
    while running:
        
        for event in pygame.event.get(): # getting the event from pygame.event.get()
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

if __name__ == '__main__':
    main()
