""" Module for bullets """
import pygame
from pygame.sprite import Sprite
from game_settings import MovingDirection as md

class Bullet(Sprite):
    """ Create bullet. """
    def __init__(self, g_settings, surface, screen, rect, moving_direction):
        super(Bullet, self).__init__()
        self.screen = screen
        self.surface = surface
        self.move_factor = g_settings.bullets_move_factor

        self.rect = pygame.Rect(
            0, 0, g_settings.bullets_width,
            g_settings.bullets_height
        )
        self.rect.centerx = rect.centerx
        self.rect.centery = rect.centery
        self.moving_direction = moving_direction
        self.color = g_settings.bullets_color
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def draw_bullet(self):
        """ Drawing bullet. """
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update_bullet(self):
        """ Update bullet positions. """
        if self.moving_direction == md.UP:
            self.centery -= self.move_factor
        if self.moving_direction == md.RIGHT:
            self.centerx += self.move_factor
        if self.moving_direction == md.DOWN:
            self.centery += self.move_factor
        if self.moving_direction == md.LEFT:
            self.centerx -= self.move_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
