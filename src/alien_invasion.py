import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    """An overall class to manage the games components and behaviour"""
    def __init__(self):
        """Starts the game, and create game resources"""
        pygame.init()
        
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")
        
        
        self.ship = Ship(self)
    
    def run_game(self):
        """Starts the main loop of the game """
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update_movement()

    def _check_events(self):         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # If a buttun is pushed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

            # If a button is let go                       
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False



    def _update_screen(self):
        """ Updates the screen and flips to the new screen"""
    
        # Redraw the screen everytime the loop is passed
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()