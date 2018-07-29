""" Wall module """
import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    """ Create wall in screen. """
    def __init__(self, surface, image_source, centerx, centery):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 24, 24)
        self.color = (80, 25, 23)
        self.surface = surface
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.image = pygame.image.load(image_source)

    def draw_wall(self):
        """ ??? """
        # pygame.draw.rect(self.surface, self.color, self.rect)
        self.surface.blit(self.image, self.rect)
