"""
Game like "Battle City" for NES
"""
import pygame

import game_function
from tank import Tank
from game_settings import Game_settings


class Game():
    """ Main game class. """
    def __init__(self):
        """ Init game object. """
        pygame.init()
        self.g_settings = Game_settings()
        self.surface = pygame.display.set_mode(
            (self.g_settings.window_width, self.g_settings.window_height))
        self.game_screen = pygame.Rect(self.g_settings.game_positionx,
                self.g_settings.game_positiony, self.g_settings.game_width,
                self.g_settings.game_height)
        self.score_screen = pygame.Rect(self.g_settings.score_positionx,
                self.g_settings.score_positiony, self.g_settings.score_width,
                self.g_settings.score_height)
        # set title
        pygame.display.set_caption("Tanks 1990")
        self.player_tank = Tank(self.g_settings, self.surface, self.game_screen)
        # Sart game loop
        self.loop()

    def loop(self):
        """ Game loop """
        while True:
            game_function.catch_event(self.player_tank)
            self.surface.fill(self.g_settings.game_color, self.game_screen)
            self.surface.fill(self.g_settings.score_color, self.score_screen)
            self.player_tank.update()
            self.player_tank.drow_tank()
            pygame.display.flip()

if __name__ == '__main__':
    Game()
