""" Tank module """
import time
import random
import pygame
from pygame.sprite import Sprite
from game_settings import MovingDirection as md
from bullets import Bullet

class Tank(Sprite):
    """ ??? """
    def __init__(
            self, surface, screen, move_factor,
            image_source, centerx, centery, moving_direction
        ):
        super().__init__()
        self.surface = surface
        self.screen = screen
        self.move_factor = move_factor
        self.image_source = image_source
        self.image = pygame.image.load(image_source)
        self.rot_image = pygame.transform.rotate(self.image, 0)
        # tank positions
        self.centerx = float(centerx)
        self.centery = float(centery)
        # tank rect
        self.rect = pygame.Rect(0, 0, 26, 26)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.moving_direction = moving_direction
        self.rotating_tank()
        self.bullets = pygame.sprite.Group()

    def draw_tank(self):
        """ Drawing tank. """
        self.surface.blit(self.rot_image, self.rect)

    def rotating_tank(self):
        """ rotating to moving direction """
        self.rot_image = pygame.transform.rotate(
            self.image, self.moving_direction.value
        )

    def move_tank(self):
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

    def check_collide(self, walls, enemys, enemy=None):
        """
        sprawdzenie kolizji czołgu z innymi obiektami gry i wyjazd za ekran
        """
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        collided_enemys = pygame.sprite.spritecollide(self, enemys, False)
        if enemy is not None:
            collided_enemys.remove(enemy)
        collided_elements = collided_walls + collided_enemys
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

    def fire_bullet(self, g_settings):
        """ Create bullet and add it to tank bullet_list. """
        new_bullet = Bullet(
            g_settings,
            self.surface, self.screen,
            self.rect, self.moving_direction
        )
        self.bullets.add(new_bullet)


class PlayerTank(Tank):
    """ ??? """
    def __init__(
            self, surface, screen, g_settings, moving_direction,
            centerx, centery, moving=None
    ):
        self.g_settings = g_settings
        super().__init__(
            surface, screen, self.g_settings.p_tank_move_factor,
            self.g_settings.p_tank_image, centerx,
            centery, moving_direction
        )
        # tank moving options
        if moving is None:
            self.moving = []
        else:
            self.moving = moving

    def __copy__(self):
        return PlayerTank(
            self.surface, self.screen, self.g_settings,
            self.moving_direction, self.centerx, self.centery, self.moving
        )

    def change_moving_direction(self):
        """
        Update player tank moving direction. New direction is chosen by player.
        """
        self.moving_direction = self.moving[-1]

    def update_tank(self):
        """ ??? """
        if self.moving:
            self.change_moving_direction()
            self.rotating_tank()
            self.move_tank()

class EnemyTank(Tank):
    """ ??? """
    def __init__(
            self, surface, screen, g_settings, moving_direction, centerx,
            centery
    ):
        self.g_settings = g_settings
        super().__init__(
            surface, screen, self.g_settings.e_tank_move_factor,
            self.g_settings.e_tank_image, centerx,
            centery, moving_direction
        )
        self.move_time = 3
        self.start_timer = time.time()

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
        return EnemyTank(
            self.surface, self.screen, self.g_settings, self.moving_direction,
            self.centerx, self.centery
        )

    def change_moving_direction(self):
        """ Change enemy tank moving direction. New direction is random. """
        self.moving_direction = random.choice(list(md))
        self.rotating_tank()
