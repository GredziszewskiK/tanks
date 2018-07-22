""" Tank module """
import time
import random

import pygame
from pygame.sprite import Sprite

from game_settings import RotatingAngle as md
from bullets import Bullet

class Tank(Sprite):
    """ Player tank class """
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
        self.moving_direction = rotating_angle
        # tank positions
        self.centerx = float(centerx)
        self.centery = float(centery)

        self.rect = pygame.Rect(0, 0, 28, 29)
        self.rect.centerx = float(self.centerx)
        self.rect.centery = float(self.centery)

        # self bullets
        self.bullets = pygame.sprite.Group()
        self.rotating_tank()

    def draw_tank(self):
        """ Drawing player tank. """
        self.surface.blit(self.rot_image, self.rect)

    def moving_tank(self):
        """ Move tank by move_factor. """
        if self.moving_direction.name == md.UP.name: # moving up
            self.centery -= self.move_factor
        if self.moving_direction.name == md.DOWN.name: # moving down
            self.centery += self.move_factor
        if self.moving_direction.name == md.RIGHT.name: # moving right
            self.centerx += self.move_factor
        if self.moving_direction.name == md.LEFT.name: # moving left
            self.centerx -= self.move_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def fire_bullet(self):
        """Wystrzelenie pocisku."""
        new_bullet = Bullet(
            self.surface, self.screen,
            self.rect, self.moving_direction
        )
        self.bullets.add(new_bullet)

    def rotating_tank(self):
        """ ??? """
        self.rot_image = pygame.transform.rotate(
            self.image, self.moving_direction.value
        )

    def check_collide(self, enemys, enemy=None):
        """
        sprawdzenie kolizji czołgu z innymi obiektami gry i wyjazd za ekran
        """
        collided_enemys = pygame.sprite.spritecollide(self, enemys, False)
        if enemy is not None:
            collided_enemys.remove(enemy)
        collided_elements = collided_enemys
        collide = False
        if self.moving_direction == md.UP:
            for c_element in collided_elements:
                if self.rect.top <= c_element.rect.bottom:
                    collide = True
            if self.rect.top <= self.screen.top:
                collide = True
        elif self.moving_direction == md.LEFT:
            for c_element in collided_elements:
                if self.rect.left <= c_element.rect.right:
                    collide = True
            if self.rect.left <= self.screen.left:
                collide = True
        elif self.moving_direction == md.DOWN:
            for c_element in collided_elements:
                if self.rect.bottom >= c_element.rect.top:
                    collide = True
            if self.rect.bottom >= self.screen.bottom:
                collide = True
        elif self.moving_direction == md.RIGHT:
            for c_element in collided_elements:
                if self.rect.right >= c_element.rect.left:
                    collide = True
            if self.rect.right >= self.screen.right:
                collide = True
        return collide

    def __copy__(self):
        return Tank(
            self.surface, self.screen, self.move_factor, self.image_source,
            self.centerx, self.centery, self.moving_direction
        )


class PlayerTank(Tank):
    """ ??? """
    def __init__(
            self, surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle, moving=None
    ):
        super().__init__(
            surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle
        )
        # tank moving options
        if moving is None:
            self.moving = []
        else:
            self.moving = moving

    def __copy__(self):
        return PlayerTank(
            self.surface, self.screen, self.move_factor, self.image_source,
            self.centerx, self.centery, self.moving_direction, self.moving
        )

    def update_tank(self):
        """ updtate player tank positions """
        if self.moving:
            self.moving_direction = self.moving[-1]
            self.moving_tank()
            self.rotating_tank()

class EnemyTank(Tank):
    """ ??? """
    def __init__(
            self, surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle
    ):
        super().__init__(
            surface, screen, move_factor,
            image_source, centerx, centery, rotating_angle
        )
        self.move_time = 3
        self.start_timer = time.time()

    def __copy__(self):
        return EnemyTank(
            self.surface, self.screen, self.move_factor, self.image_source,
            self.centerx, self.centery, self.moving_direction
        )

    def update_tank(self, enemys, walls):
        """ Update enemy tank. """
        enemys_copy = enemys.copy()
        enemys_copy.remove(self)
        tank_copy = self.__copy__()
        tank_copy.moving_tank()
        collide = tank_copy.check_collide(walls, enemys, self)
        if collide:
            self.change_moving_direction()
        else:
            self.moving_tank()

    def change_moving_direction(self):
        """ Change enemy tank moving direction. New direction is random. """
        self.moving_direction = random.choice(list(md))
        self.rotating_tank()
