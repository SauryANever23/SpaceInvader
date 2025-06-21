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
    """The main player class"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/main.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (412, 580))

class Bullets(pygame.sprite.Sprite):
    """The Bullet class"""
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center = (player_x+32, player_y+30))

class Enemy(pygame.sprite.Sprite):
    """The Enemy class"""
    def __init__(self, type, position_x, position_y):
        super().__init__()
        if type == 'enemy1':
            self.image = pygame.image.load('assets/enemy1.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (position_x, position_y))
        elif type == 'enemy2':
            self.image = pygame.image.load('assets/enemy2.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (position_x, position_y))
        elif type == 'enemy3':
            self.image = pygame.image.load('assets/enemy3.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (position_x, position_y))
        else:
            return "invalid"

def main():
    # Making a window
    screen = BaiscInit.set_screen(800, 600)
    
    # Title 
    BaiscInit.set_title("Space Invader")
    
    # the plater 
    player = Player()
    player_x_change = 0
    # The bullet inside the game loop 
    bullet = Bullets(player.rect.x, player.rect.y)
    
    enemy1 = Enemy('enemy1', 300, 500)
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
                    player_x_change = 1
                if event.key == pygame.K_a:
                    player_x_change = -1
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    player_x_change = 0

        player.rect.x += player_x_change
        # Making borders
        if player.rect.x <= 0:
            player.rect.x = 0
        elif player.rect.x >= 736:
            player.rect.x = 736
        # Making the bullet reapper
        if bullet.rect.y <= 0:
            bullet.rect.x, bullet.rect.y = player.rect.x+20, player.rect.y
        

        # setting the screen color to grey 
        screen.fill((50, 50, 50))
        
        # Displaying the character in the game 
        screen.blit(player.image, player.rect)

        # The bullet inside the game loop 
        # bullet = Bullets(player.rect.x, player.rect.y    main()
        
        # Displaying the bullet 
        screen.blit(bullet.image, bullet.rect)
        
        # Making the bullet move
        bullet.rect.y -= 1
        
        # showing all the enemies on screen 
        screen.blit(enemy1.image, enemy1.rect)

        pygame.display.flip()

if __name__ == '__main__':
    main()
