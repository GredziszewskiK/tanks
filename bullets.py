""" Module for bullets """
import pygame
from pygame.sprite import Sprite
from game_settings import RotatingAngle as ra

class Bullet(Sprite):
    """ Create bullets class """
    def __init__(self, surface, screen, rect, rotating_angle):
        super(Bullet, self).__init__()
        self.screen = screen
        self.surface = surface

        self.rect = pygame.Rect(0, 0, 3, 3)
        self.rect.centerx = rect.centerx
        self.rect.centery = rect.centery
        self.rotating_angle = rotating_angle
        self.color = (230, 230, 230)

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def draw_bullet(self):
        """ Drawing bullet. """
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update_bullet(self,):
        """ Update bullet positions. """
        if self.rotating_angle == ra.UP:
            self.centery -= 0.1
        if self.rotating_angle == ra.RIGHT:
            self.centerx += 0.1
        if self.rotating_angle == ra.DOWN:
            self.centery += 0.1
        if self.rotating_angle == ra.LEFT:
            self.centerx -= 0.1

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
