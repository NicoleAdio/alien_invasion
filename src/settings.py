class Settings:
    """This class stores all the settings for the game"""

    def __init__(self):
        """Initializing the games settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (34,21,56)
        # Ship Settings
        self.ship_speed = 1.5
        # Bullet Setting
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (230, 180, 0)
        self.bullets_allowed = 5