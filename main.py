import pygame 

# Initializing pygame 
pygame.init()

class BaiscInit():

    def set_screen(lenght, bredth):
        screen = pygame.display.set_mode((lenght, bredth))
        return screen
