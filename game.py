"""
Game like "Battle City" for NES
"""
import pygame

import game_function
from tank import Tank
from game_settings import GameSettings
from game_settings import RotatingAngle as ra

class Game():
    """ Main game class. """
    def __init__(self):
        """ Init game object. """
        pygame.init()
        self.g_settings = GameSettings()
        self.surface = pygame.display.set_mode(
            (self.g_settings.window_width, self.g_settings.window_height)
        )
        # surface part for game map
        self.game_screen = pygame.Rect(
            self.g_settings.game_positionx, self.g_settings.game_positiony,
            self.g_settings.game_width, self.g_settings.game_height
        )
        # surface part for score and statistic
        self.score_screen = pygame.Rect(
            self.g_settings.score_positionx, self.g_settings.score_positiony,
            self.g_settings.score_width, self.g_settings.score_height
        )
        # set window title
        pygame.display.set_caption(self.g_settings.game_title)
        # player rank
        self.player_tank = Tank(
            self.surface, self.game_screen, self.g_settings.p_tank_move_factor,
            self.g_settings.p_tank_image, self.g_settings.p_tank_centerx,
            self.g_settings.p_tank_centery, ra.UP
        )
        # sprites group for player bullets
        self.p_bullets = pygame.sprite.Group()
        # sprites group for enemys tanks
        self.enemys = pygame.sprite.Group()
        self.enemy_tank = Tank(
            self.surface, self.game_screen, self.g_settings.e_tank_move_factor,
            self.g_settings.e_tank_image, self.g_settings.e_tank_centerx,
            self.g_settings.e_tank_centery, ra.DOWN
        )
        self.enemys.add(self.enemy_tank)
        # Start game loop
        self.loop()

    def loop(self):
        """ Game loop """
        while True:
            game_function.catch_event(
                self.g_settings, self.player_tank, self.p_bullets
            )
            game_function.update_bullets(self.enemys, self.p_bullets)
            # create copy of player tank, and check if it can be moved
            temp_tank = self.player_tank.__copy__()
            if game_function.player_collide(self.player_tank, self.enemys):
                self.player_tank = temp_tank
            game_function.update_screen(
                self.g_settings, self.surface, self.game_screen,
                self.score_screen, self.player_tank, self.enemys,
                self.p_bullets
            )

if __name__ == '__main__':
    Game()
