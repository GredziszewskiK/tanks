""" Tank module """
import pygame
from game_settings import RotatingAngle as ra
from bullets import Bullet

class Tank():
    """ Player tank class """
    def __init__(self, g_settings, surface, screen):
        self.g_settings = g_settings
        self.surface = surface
        self.screen = screen
        self.image = pygame.image.load("images/player_tank.png")
        self.rot_image = pygame.transform.rotate(self.image, 0)
        self.rect = pygame.Rect(0, 0, 28, 29)
        self.rect.centerx = self.screen.centerx
        self.rect.centery = self.screen.centery

        # tank moving options
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # tank positions
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # shooting site
        self.rotating_angle = ra.UP

        # self bullets
        self.bullets = pygame.sprite.Group()

    def draw_tank(self):
        """ Drawing player tank. """
        self.surface.blit(self.rot_image, self.rect)

    def update_tank(self):
        """ updtate tank positions """
        if (self.moving_right and self.rect.right <= self.screen.right
                and not self.moving_down and not self.moving_left
                and not self.moving_up):
            self.rotating_angle = ra.RIGHT
            self.centerx += self.g_settings.tank_move_factor
        if (self.moving_left and self.rect.left >= self.screen.left
                and not self.moving_right and not self.moving_up
                and not self.moving_down):
            self.rotating_angle = ra.LEFT
            self.centerx -= self.g_settings.tank_move_factor
        if (self.moving_up and self.rect.top >= self.screen.top
                and not self.moving_down and not self.moving_left
                and not self.moving_right):
            self.rotating_angle = ra.UP
            self.centery -= self.g_settings.tank_move_factor
        if (self.moving_down and self.rect.bottom <= self.screen.bottom
                and not self.moving_up and not self.moving_left
                and not self.moving_right):
            self.rotating_angle = ra.DOWN
            self.centery += self.g_settings.tank_move_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.rot_image = pygame.transform.rotate(
            self.image, self.rotating_angle.value
            )

    def fire_bullet(self):
        """Wystrzelenie pocisku."""
        new_bullet = Bullet(
            self.surface, self.screen,
            self.rect, self.rotating_angle
            )
        self.bullets.add(new_bullet)
