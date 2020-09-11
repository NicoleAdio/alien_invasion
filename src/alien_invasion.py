import sys

import pygame

from settings import Settings
class AlienInvasion:
    """An overall class to manage the games components and behaviour"""
    def __init__(self):
        """Starts the game, and create game resources"""
        pygame.init()
        
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")
        
        # Sets colour of background
        
    
    def run_game(self):
        """Starts the main loop of the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_colour)

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()