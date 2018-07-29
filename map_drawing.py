""" Module for all map methond """
from wall import Wall

def read_map_elements(surface, g_settings, walls):
    """ Reading map elements from .txt file and add it to walls atribute """
    map_array = []
    with open('map2.txt') as map_shema:
        for line in map_shema:
            map_array.append(line.rstrip())

    centerx = centery = 24
    for row in map_array:
        for cell in row:
            if cell == 'B': # its brick wall
                add_wall(
                    surface, g_settings.brick_wall, walls, centerx, centery
                )
            elif cell == 'S': # its steal wall
                add_wall(
                    surface, g_settings.steal_wall, walls, centerx, centery
                )
            elif cell == 'E': # spot for enemy respawn
                print('Set enemy respawn')
            elif cell == 'P': # spot for player respawn
                print('Set player respawn')
            elif cell == ' ': # its empty space on the map
                pass
            centerx += 48
        centerx = 24
        centery += 48

def add_wall(surface, image, walls, centerx, centery):
    """ Create 1 wall that contain 4 smaller parts. """
    wall = Wall(
        surface, image, centerx-12, centery-12
    )
    walls.add(wall)
    wall = Wall(
        surface, image, centerx+12, centery-12
    )
    walls.add(wall)
    wall = Wall(
        surface, image, centerx-12, centery+12
    )
    walls.add(wall)
    wall = Wall(
        surface, image, centerx+12, centery+12
    )
    walls.add(wall)
