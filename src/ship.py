import pygame

class Ship:
    """Manages the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship from the images file and get its rect
        self.image = pygame.image.load("src/Images/Spaceship Icon.png")
        self.rect = self.image.get_rect()

        # Start every new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Turn rect into float to store speed value4
        self.x = float(self.rect.x)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update_movement(self):
        """Update the ships postion based on the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
 
    def blitme(self):
        """ This draws the ship """
        self.screen.blit(self.image, self.rect)