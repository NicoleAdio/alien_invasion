import pygame

class Ship:
    """Manages the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.rect = ai_game.screen.get_rect()

        # Load the ship from the images file and get its rect
        self.image = pygame.image.load("src/Images/Spaceship Icon.png")
        self.rect = self.image.get_rect()

        # Start every new ship at the bottom centre of the screen
        self.scree.blit(self.image.rect)
 
    def blitme(self):
        """ This draws the ship """
        self.screen.blit(self.images, self.rect)