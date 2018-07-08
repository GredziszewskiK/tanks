""" Module for game setting """
from enum import Enum

class GameSettings():
    """ Nie ma :"""
    def __init__(self):
        """ init game settings """
        # window settings
        self.window_height = 600
        self.window_width = 800

        # game screen
        self.game_height = 600
        self.game_width = 600
        self.game_positionx = 0
        self.game_positiony = 0
        self.game_color = (30, 30, 30)

        # score screen
        self.score_height = 600
        self.score_width = 200
        self.score_positionx = 600
        self.score_positiony = 0
        self.score_color = (20, 20, 20)

        # player tank
        self.p_tank_move_factor = 0.5
        self.p_tank_image = "images/player_tank.png"
        self.p_tank_centerx = 30
        self.p_tank_centery = 50

        # enemy tank
        self.e_tank_move_factor = 0.5
        self.e_tank_image = "images/enemy_tank.png"
        self.e_tank_centerx = 100
        self.e_tank_centery = 100

class RotatingAngle(Enum):
    """ Enum for rotating angle. """
    UP = 0
    LEFT = 90
    DOWN = 180
    RIGHT = 270
