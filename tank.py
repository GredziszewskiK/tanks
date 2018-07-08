""" Tank module """
import pygame
from game_settings import RotatingAngle as ra
from bullets import Bullet

class Tank():
    """ Player tank class """
    def __init__(
            self, surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle
        ):
        self.surface = surface
        self.screen = screen
        self.move_factor = move_factor
        self.image_source = image_source
        self.image = pygame.image.load(image_source)
        self.rot_image = pygame.transform.rotate(self.image, 0)
        self.rect = pygame.Rect(0, 0, 28, 29)
        self.rect.centerx = float(centerx)
        self.rect.centery = float(centery)

        # tank moving options
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.colision = False

        # tank positions
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # shooting site
        self.rotating_angle = rotating_angle

        # self bullets
        self.bullets = pygame.sprite.Group()
        self.rotating_tank()

    def draw_tank(self):
        """ Drawing player tank. """
        self.surface.blit(self.rot_image, self.rect)

    def update_tank(self):
        """ updtate tank positions """
        if (self.moving_right and self.rect.right <= self.screen.right
                and not self.moving_down and not self.moving_left
                and not self.moving_up):
            self.rotating_angle = ra.RIGHT
            self.centerx += self.move_factor
        if (self.moving_left and self.rect.left >= self.screen.left
                and not self.moving_right and not self.moving_up
                and not self.moving_down):
            self.rotating_angle = ra.LEFT
            self.centerx -= self.move_factor
        if (self.moving_up and self.rect.top >= self.screen.top
                and not self.moving_down and not self.moving_left
                and not self.moving_right):
            self.rotating_angle = ra.UP
            self.centery -= self.move_factor
        if (self.moving_down and self.rect.bottom <= self.screen.bottom
                and not self.moving_up and not self.moving_left
                and not self.moving_right):
            self.rotating_angle = ra.DOWN
            self.centery += self.move_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.rotating_tank()

    def fire_bullet(self):
        """Wystrzelenie pocisku."""
        new_bullet = Bullet(
            self.surface, self.screen,
            self.rect, self.rotating_angle
        )
        self.bullets.add(new_bullet)

    def rotating_tank(self):
        """ ??? """
        self.rot_image = pygame.transform.rotate(
            self.image, self.rotating_angle.value
        )

    def __copy__(self):
        return Tank(
            self.surface, self.screen, self.move_factor, self.image_source,
            self.centerx, self.centery, self.rotating_angle
        )
