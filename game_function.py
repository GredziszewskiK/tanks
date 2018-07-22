""" Module for all game functions """
import sys

import pygame
from game_settings import RotatingAngle as md

def event_key_down(event, player_tank):
    """ Events for presing keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving.append(md.LEFT)
    if event.key == pygame.K_RIGHT:
        player_tank.moving.append(md.RIGHT)
    if event.key == pygame.K_UP:
        player_tank.moving.append(md.UP)
    if event.key == pygame.K_DOWN:
        player_tank.moving.append(md.DOWN)
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE:
        player_tank.fire_bullet()

def event_key_up(event, player_tank):
    """ Events for presing keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving.remove(md.LEFT)
    if event.key == pygame.K_RIGHT:
        player_tank.moving.remove(md.RIGHT)
    if event.key == pygame.K_UP:
        player_tank.moving.remove(md.UP)
    if event.key == pygame.K_DOWN:
        player_tank.moving.remove(md.DOWN)

def catch_event(player_tank):
    """ Check type of events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_key_down(event, player_tank)
        elif event.type == pygame.KEYUP:
            event_key_up(event, player_tank)

def update_bullets(bullets):
    """ Upddate all bullets """
    for bullet in bullets.copy():
        bullet.update_bullet()
        if (
                bullet.rect.bottom <= bullet.screen.top
                or bullet.rect.top >= bullet.screen.bottom
                or bullet.rect.left >= bullet.screen.right
                or bullet.rect.right <= bullet.screen.left
        ):
            bullets.remove(bullet)

def update_screen(g_settings, surface, game_screen, score_screen,
                  player_tank, enemy_tank):
    """ Update screen. """
    surface.fill(g_settings.game_color, game_screen)
    surface.fill(g_settings.score_color, score_screen)
    for bullet in player_tank.bullets.sprites():
        bullet.draw_bullet()
    enemy_tank.draw_tank()
    player_tank.draw_tank()
    pygame.display.flip()

def player_collide(p_tank, enemy_tank):
    """ Check if player tank had colision with object. """
    p_tank.update_tank()
    if pygame.sprite.collide_rect(p_tank, enemy_tank):
        return True
    else:
        return False
