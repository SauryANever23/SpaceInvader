import pygame
import random
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

    def bullet_mechnism(self):
        """Making the bullet reapper"""
        if bullet.rect.y <= 0:
            bullet.rect.x, bullet.rect.y = player.rect.x+20, player.rect.y




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
        
        def enemy_movement(x_pos, y_pos):
            """This function will move the enemy, from left to right and vice verse."""
            change = random.randint(1, 5)
            while self.rect.x != 736:
                change = random.randint(1, 7)
                self.rect.x += change 

def main():
    # Making a window
    screen = BaiscInit.set_screen(800, 600)
    
    # Title 
    BaiscInit.set_title("Space Invader")
    
    # Player
    player = Player()
    player_x_change = 0

    # The bullet inside the game loop / Group for Bullet 
    bullet = Bullets(player.rect.x, player.rect.y)
    # bullet.add(Bullets(player.rect.x, player.rect.y)) 
    
    # Enemy Group
    enemy1 = Enemy('enemy1', random.randint(0, 800), random.randint(50, 100))
    ememy2 = Enemy('enemy1', random.randint(0, 800), random.randint(50, 150``))
    def set_boundaries(player, bullet) -> None:
        """This function gives the player the border""" 
        if player.rect.x <= 0:
            player.rect.x = 0
        elif player.rect.x >= 736:
            player.rect.x = 736
        # Making the bullet reapper
        if bullet.rect.y <= 0:
            bullet.rect.x, bullet.rect.y = player.rect.x+20, player.rect.y

    def enemy_movement(enemy: Enemy, change: int) -> None:
        """This function will move the enemy, from left to right and vice verse."""
        change = random.randint(1, 7)
        enemy.rect.x += change
        if enemy.rect.x >= 736:
            while enemy.rect.x != 0:
                enemy.rect.x -= change 
        elif enemy.rect.x <= 0:
            while enemy.rect.x != 736:
                enemy.rect.x += change
    
    def update_pos():
        """This function updates the enemies"""
        counter = 0 # This variable sets the counter 

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
        set_boundaries(player, bullet)
        
        # Enemy Movement 
        speed = random.randint(1, 4)
        # enemy_movement(enemy1, speed) # The code is dangerious, don't run now

        # Making the bullet reapper
        # Bullets.bullet_mechnism(bullet) 
       
        if enemy1.rect.colliderect(bullet):
            enemy1.rect.x = random.randint(0, 736)
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
