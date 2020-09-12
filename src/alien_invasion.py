import sys

import pygame

from settings import Settings

from ship import Ship

from bullets import Bullet


class AlienInvasion:
    """An overall class to manage the games components and behaviour"""
    def __init__(self):
        """Starts the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
    
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Starts the main loop of the game """
        while True:
            self._check_events()
            self.ship.update_movement()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def _check_keydown_events(self, event):
        # If a buttun is pushed
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()    

    def check_keyup_events(self, event):
        # If a button is let go                            
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