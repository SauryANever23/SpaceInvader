import pygame 
import sys
# Initializing pygame 
pygame.init()

class BaiscInit():
    
    # Function for Initializing the window
    def set_screen(lenght: int, bredth: int):
        screen = pygame.display.set_mode((lenght, bredth))
        return screen
    
    # Functino for setting the title of the program
    def set_title(name: str):
        pygame.display.set_caption(name)
    
    # Set the icon of the window 
    def set_icon():
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)


# Sprite Class for The main player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/player.png').convert_alpha
        self.rect = self.image.get_rect(midbottom = (600, 300))




def main():
    # Making a window
    screen = BaiscInit.set_screen(800, 600)
    
    # Title 
    BaiscInit.set_title("Space Invader")
    
    # Player 
    # To add a player 
    # Then adding fcuntions to the play 

    # this var determines if the program is running 
    running = True
    
    # game loop
    while running:
        
        for event in pygame.event.get(): # getting the event from pygame.event.get()
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        
        # setting the screen color to grey 
        screen.fill((50, 50, 50))

        pygame.display.flip()

if __name__ == '__main__':
    main()
