""" Module for all game functions """
import sys

import pygame
from bullets import Bullet

def event_key_down(event, g_settings, player_tank, p_bullets):
    """ Events for presing keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving_left = True
    if event.key == pygame.K_RIGHT:
        player_tank.moving_right = True
    if event.key == pygame.K_UP:
        player_tank.moving_up = True
    if event.key == pygame.K_DOWN:
        player_tank.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE:
        fire_bullet(g_settings, player_tank, p_bullets)

def event_key_up(event, player_tank):
    """ Events for release keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving_left = False
    if event.key == pygame.K_RIGHT:
        player_tank.moving_right = False
    if event.key == pygame.K_UP:
        player_tank.moving_up = False
    if event.key == pygame.K_DOWN:
        player_tank.moving_down = False

def catch_event(g_settings, player_tank, p_bullets):
    """ Check type of events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_key_down(event, g_settings, player_tank, p_bullets)
        elif event.type == pygame.KEYUP:
            event_key_up(event, player_tank)

def update_bullets(enemys, bullets):
    """ Upddate all bullets """
    for bullet in bullets.copy():
        bullet.update_bullet()
        # remove bulets that reach edge of screen
        if (
                bullet.rect.bottom <= bullet.screen.top
                or bullet.rect.top >= bullet.screen.bottom
                or bullet.rect.left >= bullet.screen.right
                or bullet.rect.right <= bullet.screen.left
        ):
            bullets.remove(bullet)
    # remove bullets and enemies that hit each others
    p_bullets_enemy_collide(enemys, bullets)

def update_screen(g_settings, surface, game_screen, score_screen,
                  player_tank, enemys, p_bullets):
    """ Update screen. """
    surface.fill(g_settings.game_color, game_screen)
    surface.fill(g_settings.score_color, score_screen)
    for bullet in p_bullets.sprites():
        bullet.draw_bullet()
    for enemy in enemys.sprites():
        enemy.draw_tank()
    player_tank.draw_tank()
    pygame.display.flip()

def player_collide(p_tank, enemys):
    """ Check if player tank had colision with object. """
    p_tank.update_tank()
    if pygame.sprite.spritecollideany(p_tank, enemys):

        return True
    else:
        return False

def p_bullets_enemy_collide(enemys, p_bullet):
    """ ??? """
    pygame.sprite.pygame.sprite.groupcollide(enemys, p_bullet, True, True)

def fire_bullet(g_settings, tank, bullets):
    """ Wystrzelenie pocisku. """
    new_bullet = Bullet(
        g_settings,
        tank.surface, tank.screen,
        tank.rect, tank.rotating_angle
    )
    bullets.add(new_bullet)
