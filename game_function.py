""" Module for all game functions """
import sys

import pygame

def event_key_down(event, player_tank):
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

def event_key_up(event, player_tank):
    """ Events for presing keys """
    if event.key == pygame.K_LEFT:
        player_tank.moving_left = False
    if event.key == pygame.K_RIGHT:
        player_tank.moving_right = False
    if event.key == pygame.K_UP:
        player_tank.moving_up = False
    if event.key == pygame.K_DOWN:
        player_tank.moving_down = False

def catch_event(player_tank):
    """ Check type of events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_key_down(event, player_tank)
        elif event.type == pygame.KEYUP:
            event_key_up(event, player_tank)
