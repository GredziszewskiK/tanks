""" Module for game setting """
from enum import Enum

class Game_settings():
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
        self.game_color = (10, 10, 10)

        # score screen
        self.score_height = 600
        self.score_width = 200
        self.score_positionx = 600
        self.score_positiony = 0
        self.score_color = (30, 30, 30)

        # tank settings
        self.tank_move_factor = 0.5

class Rotating_angle(Enum):
    """ Enum for rotating angle. """
    UP = 0
    RIGHT = 270
    DOWN = 180
    LEFT = 90
