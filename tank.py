""" Tank module """
import pygame
from pygame.sprite import Sprite
from game_settings import RotatingAngle as ra

class Tank(Sprite):
    """ Create player and enemys tanks """
    def __init__(
            self, surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle
        ):
        super().__init__()
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

        # rotate to moving direction
        self.rotating_angle = rotating_angle
        self.rotating_tank()

    def draw_tank(self):
        """ Drawing player tank. """
        self.surface.blit(self.rot_image, self.rect)

    def update_tank(self):
        """ Update tank position """

        # check direction of moving, tank can move on one direction
        if (self.moving_right and self.rect.right <= self.screen.right
                and not self.moving_down and not self.moving_left
                and not self.moving_up
           ):
            self.rotating_angle = ra.RIGHT
            self.centerx += self.move_factor
        if (self.moving_left and self.rect.left >= self.screen.left
                and not self.moving_right and not self.moving_up
                and not self.moving_down
           ):
            self.rotating_angle = ra.LEFT
            self.centerx -= self.move_factor
        if (self.moving_up and self.rect.top >= self.screen.top
                and not self.moving_down and not self.moving_left
                and not self.moving_right
           ):
            self.rotating_angle = ra.UP
            self.centery -= self.move_factor
        if (self.moving_down and self.rect.bottom <= self.screen.bottom
                and not self.moving_up and not self.moving_left
                and not self.moving_right
           ):
            self.rotating_angle = ra.DOWN
            self.centery += self.move_factor

        # change tank position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.rotating_tank()

    def rotating_tank(self):
        """ rotating to moving direction """
        self.rot_image = pygame.transform.rotate(
            self.image, self.rotating_angle.value
        )

    def __copy__(self):
        return Tank(
            self.surface, self.screen, self.move_factor, self.image_source,
            self.centerx, self.centery, self.rotating_angle
        )
