"""
Game like "Battle City" for NES
"""
import pygame

import game_function
from tank import EnemyTank
from tank import PlayerTank
from game_settings import GameSettings
from game_settings import RotatingAngle as ra


class Game():
    """ Main game class. """
    def __init__(self):
        """ Init game object. """
        pygame.init()
        self.g_settings = GameSettings()
        self.surface = pygame.display.set_mode(
            (self.g_settings.window_width, self.g_settings.window_height))
        self.game_screen = pygame.Rect(
            self.g_settings.game_positionx, self.g_settings.game_positiony,
            self.g_settings.game_width, self.g_settings.game_height
        )
        self.score_screen = pygame.Rect(
            self.g_settings.score_positionx, self.g_settings.score_positiony,
            self.g_settings.score_width, self.g_settings.score_height
        )
        # set window title
        pygame.display.set_caption("Tanks 1990")
        self.player_tank = PlayerTank(
            self.surface, self.game_screen, self.g_settings.p_tank_move_factor,
            self.g_settings.p_tank_image, self.g_settings.p_tank_centerx,
            self.g_settings.p_tank_centery, ra.UP
        )
        self.enemy_tank = EnemyTank(
            self.surface, self.game_screen, self.g_settings.e_tank_move_factor,
            self.g_settings.e_tank_image, self.g_settings.e_tank_centerx,
            self.g_settings.e_tank_centery, ra.DOWN
        )
        self.enemys = pygame.sprite.Group()
        self.enemys.add(self.enemy_tank)
        # Start game loop
        self.loop()

    def loop(self):
        """ Game loop """
        while True:
            game_function.catch_event(self.player_tank)
            game_function.update_bullets(self.player_tank.bullets)
            temp_tank = self.player_tank.__copy__()
            temp_tank.update_tank()
            if not temp_tank.check_collide(self.enemys):
                self.player_tank.update_tank()
            for enemy in self.enemys:
                enemy_temp_tank = enemy.__copy__()
                enemy_temp_tank.moving_tank()
                enemys_temp = self.enemys.copy()
                enemys_temp.remove(enemy)
                if not enemy_temp_tank.check_collide(enemys_temp):
                    enemy.moving_tank()
                else:
                    enemy.change_moving_direction()
            game_function.update_screen(
                self.g_settings, self.surface, self.game_screen,
                self.score_screen, self.player_tank, self.enemy_tank
            )

if __name__ == '__main__':
    Game()
