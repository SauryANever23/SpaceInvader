import pygame 
import sys
# Initializing pygame 
pygame.init()

class BaiscInit():
    
    # Function for Initializing the window
    @staticmethod
    def set_screen(lenght: int, bredth: int):
        screen = pygame.display.set_mode((lenght, bredth))
        return screen
    
    # Functino for setting the title of the program
    @staticmethod
    def set_title(name: str):
        pygame.display.set_caption(name)
    
    # Set the icon of the window 
    @staticmethod
    def set_icon():
        icon = pygame.image.load("assets/main.png")
        pygame.display.set_icon(icon)


# Sprite Class for The main player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/main.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (412, 580))

class Bullets(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center = (player_x+32, player_y+30))

def main():
    # Making a window
    screen = BaiscInit.set_screen(800, 600)
    
    # Title 
    BaiscInit.set_title("Space Invader")
    
    # the plater 
    player = Player()

    # The bullet inside the game loop 
    bullet = Bullets(player.rect.x, player.rect.y)


    # this var determines if the program is running 
    running = True
    
    # game loop
    while running:
        
        for event in pygame.event.get(): # getting the event from pygame.event.get()
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.rect.x += 20
                if event.key == pygame.K_a:
                    player.rect.x -= 20
                if event.key == pygame.K_q:
                    sys.exit()
        if player.rect.x >= 800:
            player.rect.x = 800
        
        if bullet.rect.y <= 0:
            bullet.rect.x, bullet.rect.y = player.rect.x+20, player.rect.y

        # setting the screen color to grey 
        screen.fill((50, 50, 50))
        
        # Displaying the character in the game 
        screen.blit(player.image, player.rect)

        # The bullet inside the game loop 
        # bullet = Bullets(player.rect.x, player.rect.y)

        # Displaying the bullet 
        screen.blit(bullet.image, bullet.rect)
        
        # Making the bullet move
        bullet.rect.y -= 1


        pygame.display.flip()

if __name__ == '__main__':
    main()
