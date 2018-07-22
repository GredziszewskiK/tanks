"""
Game like "Battle City" for NES
"""
import pygame

import game_function
from tank import PlayerTank
from tank import EnemyTank
from game_settings import GameSettings
from game_settings import MovingDirection as md

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
        self.player_tank = PlayerTank(
            self.surface, self.game_screen, self.g_settings, md.UP,
            self.g_settings.p_tank_centerx, self.g_settings.p_tank_centery
        )
        # sprites group for player bullets
        self.p_bullets = pygame.sprite.Group()
        # sprites group for enemys tanks
        self.enemys = pygame.sprite.Group()
        self.enemy_tank = EnemyTank(
            self.surface, self.game_screen, self.g_settings, md.RIGHT, 25, 25
        )
        self.enemy_tank2 = EnemyTank(
            self.surface, self.game_screen, self.g_settings, md.LEFT, 225, 25
        )
        self.enemys.add(self.enemy_tank)
        self.enemys.add(self.enemy_tank2)
        # create wall
        self.walls = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()
        # Start game loop
        self.loop()

    def loop(self):
        """ Game loop """
        game_function.create_walls(self.surface, self.walls)
        while True:
            game_function.catch_event(
                self.g_settings, self.player_tank
            )
            # update enemys
            for enemy in self.enemys:
                temp_enemy = enemy.__copy__()
                temp_enemy.move_tank()
                temp_enemys = self.enemys.copy()
                temp_enemys.remove(enemy)
                if temp_enemy.check_collide(self.walls, temp_enemys):
                    enemy.change_moving_direction()
                else:
                    enemy.move_tank()
            game_function.update_player_tank(
                self.player_tank, self.enemys, self.walls
            )
            game_function.update_bullets(self.enemys, self.player_tank.bullets)
            game_function.update_screen(
                self.g_settings, self.surface, self.game_screen,
                self.score_screen, self.player_tank, self.enemys,
                self.player_tank.bullets, self.walls
            )

if __name__ == '__main__':
    Game()
