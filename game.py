"""
Game like "Battle City" for NES
"""
import pygame

import game_function as gf
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
        self.p_tank = PlayerTank(
            self.surface, self.game_screen, self.g_settings, md.UP,
            self.g_settings.p_tank_centerx, self.g_settings.p_tank_centery
        )
        # sprites group for bullets
        self.p_bullets = pygame.sprite.Group()
        self.e_bullets = pygame.sprite.Group()
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
        # Start game loop
        self.loop()

    def loop(self):
        """ Game loop """
        gf.create_walls(self.surface, self.walls)
        while True:
            gf.catch_event(
                self.p_bullets, self.p_tank
            )
            gf.update_enemys(
                self.enemys, self.walls, self.e_bullets, self.p_tank
            )
            gf.update_player_tank(
                self.p_tank, self.enemys, self.walls
            )
            gf.update_bullets(self.p_bullets)
            gf.update_bullets(self.e_bullets)
            gf.p_bullet_e_bullets_collide(self.p_bullets, self.e_bullets)
            gf.p_bullets_enemy_collide(self.enemys, self.p_bullets)
            gf.e_bullets_player_collide(self.p_tank, self.e_bullets)
            gf.update_screen(
                self.g_settings, self.surface, self.game_screen,
                self.score_screen, self.p_tank, self.enemys,
                self.p_bullets, self.walls, self.e_bullets
            )

if __name__ == '__main__':
    Game()
