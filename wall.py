""" Wall module """
import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    """ Create wall in screen. """
    def __init__(self, surface, centerx, centery):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.color = (80, 25, 23)
        self.surface = surface
        self.rect.centerx = centerx
        self.rect.centery = centery

    def draw_wall(self):
        """ ??? """
        pygame.draw.rect(self.surface, self.color, self.rect)
