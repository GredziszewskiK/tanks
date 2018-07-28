""" Module for all game functions """
import sys
import pygame
from wall import Wall
from game_settings import MovingDirection as md

def event_key_down(event, p_bullets, player_tank):
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
        player_tank.fire_bullet(p_bullets)

def event_key_up(event, player_tank):
    """ Events for release keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving.remove(md.LEFT)
    if event.key == pygame.K_RIGHT:
        player_tank.moving.remove(md.RIGHT)
    if event.key == pygame.K_UP:
        player_tank.moving.remove(md.UP)
    if event.key == pygame.K_DOWN:
        player_tank.moving.remove(md.DOWN)

def catch_event(g_settings, player_tank):
    """ Cach event and invoke appropriate method. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_key_down(event, g_settings, player_tank)
        elif event.type == pygame.KEYUP:
            event_key_up(event, player_tank)

def update_bullets(bullets):
    """ Upddate bullets from passed sprite Group.  """
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

def update_player_tank(player_tank, enemys, walls):
    """ ??? """
    player_tank.change_moving_direction()
    player_tank.rotating_tank()
    temp_player_tank = player_tank.__copy__()
    temp_player_tank.move_tank()
    if not temp_player_tank.check_collide(walls, enemys):
        player_tank.move_tank()

def update_enemys(enemys, walls, e_bullets, p_tank):
    """ ??? """
    for enemy in enemys:
        temp_enemy = enemy.__copy__()
        temp_enemy.move_tank()
        temp_enemys = enemys.copy()
        temp_enemys.remove(enemy)
        if temp_enemy.check_collide(walls, temp_enemys, p_tank):
            enemy.change_moving_direction()
        else:
            enemy.move_tank()
        enemy.fire_bullet(e_bullets)

def update_screen(g_settings, surface, game_screen, score_screen,
                  player_tank, enemys, p_bullets, walls, e_bullets):
    """ Update screen. """
    surface.fill(g_settings.game_color, game_screen)
    surface.fill(g_settings.score_color, score_screen)
    for bullet in p_bullets:
        bullet.draw_bullet()
    for bullet in e_bullets:
        bullet.draw_bullet()
    for enemy in enemys:
        enemy.draw_tank()
    for wall in walls:
        wall.draw_wall()
    player_tank.draw_tank()
    pygame.display.flip()

def p_bullets_enemy_collide(enemys, p_bullet):
    """ ??? """
    pygame.sprite.groupcollide(enemys, p_bullet, True, True)

def e_bullets_player_collide(player, e_bullets):
    """ ??? """
    pygame.sprite.spritecollide(player, e_bullets, True)

def p_bullet_e_bullets_collide(p_bullets, e_bullets):
    """ ??? """
    pygame.sprite.groupcollide(p_bullets, e_bullets, True, True)

def create_walls(surface, walls):
    """Create walls"""
    wall_1 = Wall(surface, 25, 75)
    wall_2 = Wall(surface, 75, 75)
    wall_3 = Wall(surface, 75, 125)
    wall_4 = Wall(surface, 75, 175)
    wall_5 = Wall(surface, 175, 25)
    wall_6 = Wall(surface, 175, 75)
    wall_7 = Wall(surface, 175, 125)
    wall_8 = Wall(surface, 175, 175)
    # wall_9 = Wall(surface, 225, 75)
    wall_10 = Wall(surface, 275, 75)
    wall_11 = Wall(surface, 275, 125)
    wall_12 = Wall(surface, 275, 175)
    wall_13 = Wall(surface, 325, 75)
    walls.add(wall_1)
    walls.add(wall_2)
    walls.add(wall_3)
    walls.add(wall_4)
    walls.add(wall_5)
    walls.add(wall_6)
    walls.add(wall_7)
    walls.add(wall_8)
    # walls.add(wall_9)
    walls.add(wall_10)
    walls.add(wall_11)
    walls.add(wall_12)
    walls.add(wall_13)
