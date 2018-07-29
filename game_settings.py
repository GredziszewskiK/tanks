""" Module for game setting """
from enum import Enum

class GameSettings():
    """ All static setting for game objects. """
    def __init__(self):
        """ init game settings """
        # window settings
        self.window_height = 624
        self.window_width = 824
        self.game_title = "Tanks 1990"

        # game screen size 13x13
        self.game_height = 624
        self.game_width = 624
        self.game_positionx = 0
        self.game_positiony = 0
        self.game_color = (30, 30, 30)

        # score screen
        self.score_height = 624
        self.score_width = 200
        self.score_positionx = 624
        self.score_positiony = 0
        self.score_color = (20, 20, 20)

        # player tank
        self.p_tank_move_factor = 0.3
        self.p_tank_image = "images/player_tank.png"
        self.p_tank_centerx = 100
        self.p_tank_centery = 500
        self.p_tank_bullets_limit = 3

        # enemy tank
        self.e_tank_move_factor = 0.3
        self.e_tank_image = "images/enemy_tank.png"
        self.e_tank_centerx = 100
        self.e_tank_centery = 100
        self.e_tank_shot_time = 3

        # bullets
        self.bullets_move_factor = 0.5
        self.bullets_width = 10
        self.bullets_height = 10
        self.bullets_color = (230, 230, 230)

        # walls
        self.brick_wall = "images/brick_wall.png"
        self.steal_wall = "images/steal_wall.png"

class MovingDirection(Enum):
    """ Enum for tank moving directions. """
    UP = 0
    LEFT = 90
    DOWN = 180
    RIGHT = 270
