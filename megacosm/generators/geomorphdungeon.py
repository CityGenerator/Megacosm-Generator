#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from name import Name
import json
import logging
import random


class GeomorphDungeon(Generator):

    # This is a simple translation table. I say simple, but it's probably not.
    # All possible connection configurations result in 16 possible combinations.
    # These combinations are described in binary (the lead string).
    # Each combination can be broken down into only 5 tiles with different rotations.
    # type: refers to one of the basic 5 tile types:
    #       one side, two sides across, two sides adjacent, three sides, four sides.
    # Rotation: refers to the orientation of the tile: It can be rotated 0-3 times.
    CELL_TYPES = {
        # bits are sorted [ left bottom right top ]
        '0b0': {'type': '0000', 'rotation': 0},     # No connections
        '0b1': {'type': '0001', 'rotation': 0},     # one side
        '0b10': {'type': '0001', 'rotation': 1},    # one side
        '0b11': {'type': '0010', 'rotation': 0},    # twoside adjacent
        '0b100': {'type': '0001', 'rotation': 2},   # one side
        '0b101': {'type': '0011', 'rotation': 0},   # twoside across
        '0b110': {'type': '0010', 'rotation': 1},   # twosided adjacent
        '0b111': {'type': '0100', 'rotation': 0},   # Three sides
        '0b1000': {'type': '0001', 'rotation': 3},  # one side
        '0b1001': {'type': '0010', 'rotation': 3},  # twosided adjacent
        '0b1010': {'type': '0011', 'rotation': 1},  # twosided across
        '0b1011': {'type': '0100', 'rotation': 3},  # three sides
        '0b1100': {'type': '0010', 'rotation': 2},  # twosided adjacent
        '0b1101': {'type': '0100', 'rotation': 2},  # threesided
        '0b1110': {'type': '0100', 'rotation': 1},  # three sides
        '0b1111': {'type': '0101', 'rotation': 0},  # Four connections
        }

    def __init__(self, redis, features={}):
        """ Generate a Geomorph-like dungeon """
        #FIXME geomorph and rogue should share a parent DungeonGenerator
        #FIXME move the dungeon_template to a dungeon_name object or something
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        #These are generic dungon features shared with RogueDungeon
        self.generate_features('dungeon')

        self.name=Name(self.redis,'dungeon')
        if not hasattr(self,'width'):
            self.width = self.gridwidth['tiles']
        
        if not hasattr(self,'height'):
            self.height = self.gridheight['tiles']

        # First Generate the Grid
        self.generate_grid()
        # Then Generate the Connections to each other.
        self.generate_connections()
        
        self.set_tiletypes()


    def generate_grid(self):
        """ Create a grid of width by height Tiles."""
        self.grid = [[GeomorphDungeon.Tile(i, j) for i in range(self.width)] for j in range(self.height)]

    def generate_connections(self):
        """ Link each tile to the tiles around it."""
        self.alltiles = []
        for row in self.grid:
            for tile in row:
                self.alltiles.append(tile)

        random.shuffle(self.alltiles)

        for tile in self.alltiles:
            self.calculate_top(tile)
            self.calculate_right(tile)
            self.calculate_bottom(tile)
            self.calculate_left(tile)

    def calculate_top(self, tile):
        """ determine whether this tile is connected to the one above it."""

        # If the tile is in the first row, it means there is no tile above it, so it isn't connected..
        if tile.y == 0:
            tile.top = False
        # If the tile above it exists AND it's bottom tile has already been decided, set this to the same decision.
        # e.g. if the tile above has already decided we're connected, say we're connected.
        elif self.grid[tile.y - 1][tile.x].bottom is not None:
            tile.top = self.grid[tile.y - 1][tile.x].bottom
        # If the tile above us exists but hasn't been checked for connectivity, we get to decide!
        else:
            # Check to see if it's disconnected, This is determined by the graphs segmentation value.
            # This can range from 
            if random.randint(0, self.segmentation['disconnect_chance']) == 0:
                tile.top = False
            else:
                # We're connected! Finally!
                tile.top = True


    def calculate_right(self, tile):
        if tile.x == len(self.grid[0]) - 1:
            tile.right = False
        elif self.grid[tile.y][tile.x + 1].left is not None:
            tile.right = self.grid[tile.y][tile.x + 1].left
        else:
            if random.randint(0, self.segmentation['disconnect_chance']) == 0:
                tile.right = False
            else:
                tile.right = True

    def calculate_bottom(self, tile):
        if tile.y == len(self.grid) - 1:
            tile.bottom = False
        elif self.grid[tile.y + 1][tile.x].top is not None:
            tile.bottom = self.grid[tile.y + 1][tile.x].top
        else:
            if random.randint(0, self.segmentation['disconnect_chance']) == 0:
                tile.bottom = False
            else:
                tile.bottom = True

    def calculate_left(self, tile):
        if tile.x == 0:
            tile.left = False
        elif self.grid[tile.y][tile.x - 1].right is not None:
            tile.left = self.grid[tile.y][tile.x - 1].right
        else:
            if random.randint(0, self.segmentation['disconnect_chance']) == 0:
                tile.left = False
            else:
                tile.left = True

    def set_tiletypes(self):
        """ """
        for row in self.grid:
            for tile in row:
                tile = self.generate_tiletype(tile)

    def generate_tiletype(self, tile):
        # calculate the binary "tile type"
        tile.tiletype = bin((tile.left << 3) + (tile.bottom << 2) + (tile.right << 1) + (tile.top << 0))

        # translate it with the table
        tile.imagetype = int(self.CELL_TYPES[tile.tiletype]['type'], 2)

        # Using the proper tile type, select an image from redis
        tiledata = json.loads(self.rand_value('geomorph_type_' + str(tile.imagetype)))
        tile.image = str(tiledata['path'])
        tile.author = str(tiledata['author'])
        tile.tileset = str(tiledata['tileset'])

        # Make sure to capture the rotation needed
        tile.imagerotation = self.CELL_TYPES[tile.tiletype]['rotation']
        return tile

    def __str__(self):
        """ print the name as a string."""
        return self.name.fullname.title()

    def simplify_for_json(self):
        """ Convert our pretty grid into something json-friendly."""
        resultmatrix = []
        for row in self.grid:
            resultrow = []
            for tile in row:
                resultrow.append({'path': tile.image, 'rotation': tile.imagerotation})
            resultmatrix.append(resultrow)
        # Note this is returning a clean array of arrays
        return resultmatrix
    


    class Tile(object):

        def __init__(self, x, y):
            """ test """
            #TODO do testing on x and y to ensure they're digits.
        # def __init__(self, char='#'):

            self.left = None
            self.right = None
            self.top = None
            self.bottom = None
            self.char = '#'
            self.x = x
            self.y = y
