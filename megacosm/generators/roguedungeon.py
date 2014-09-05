#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import json
import logging
import random


class RogueDungeon(Generator):

    def __init__(self, redis, features={}):
        """ Generate a Rogue-like dungeon """

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.generate_features('dungeon')

        self.apply_text_template()
        self.generate_grid()
        self.generate_rooms()
        self.generate_halls()

    def apply_text_template(self):
        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text.title()

    def generate_grid(self):
        gridsize = random.randint(self.size['minsize'], self.size['maxsize'])
        self.height = gridsize
        self.width = int(gridsize * 1.8)

        self.spaces = [[RogueDungeon.Tile() for i in range(self.width)] for j in range(self.height)]

    def convert_to_json(self):
        resultmatrix = []

        for row in self.spaces:
            resultrow = []
            for cell in row:
                resultrow.append({'passable': int(cell.passable), 'doorway': int(cell.isdoorway),
                                 'class': cell.__class__.__name__.lower()})
            resultmatrix.append(resultrow)
        return resultmatrix

    def create_random_room(self):

        # TODO FIXME  w and h is too large, need to make sure it fits in self.width

        w = min(self.width - 1, random.randint(self.room_size['minsize'], self.room_size['maxsize']))
        h = min(self.height - 1, random.randint(self.room_size['minsize'], self.room_size['maxsize']))

        # random position without going out of the boundaries of the map

        x = random.randint(0, self.width - w - 1)
        y = random.randint(0, self.height - h - 1)
        return RogueDungeon.Room(x, y, w, h)

    def generate_halls(self):
        previous_room = None
        rooms = self.rooms
        random.shuffle(rooms)
        for room in rooms:
            if previous_room is None:
                room.kind = 'entrance'
                room.kind_description = {'name': 'entrance', 'description': 'the way in'}
                room.egress = True
            else:
                self.connect_rooms(room, previous_room)
                room.kind = self.rand_value('roguedungeonroom_kind')
                kinddesc = self.redis.hmget('roguedungeonroom_kind_description', room.kind)
                room.kind_description = json.loads(kinddesc[0])
            previous_room = room

    def generate_rooms(self):
        self.rooms = []
        max_rooms = random.randint(self.room_count['minsize'], self.room_count['maxsize'])

        for r in range(max_rooms):
            new_room = self.create_random_room()

            conflict = False
            for other_room in self.rooms:
                if new_room.intersect(other_room):
                    conflict = True
                    break
            if not conflict:
                self.paint_room(new_room)
                self.rooms.append(new_room)

    def connect_rooms(self, new_room, old_room):
        pathtype = random.randint(0, 3)
        ymidpoint = random.randint(min(new_room.center['y'], old_room.center['y']), max(new_room.center['y'],
                                   old_room.center['y']))
        xmidpoint = random.randint(min(new_room.center['x'], old_room.center['x']), max(new_room.center['x'],
                                   old_room.center['x']))

        if pathtype == 0:

            # startroom new_room

            self.paint_h_tunnel(new_room.center['x'], xmidpoint, new_room.center['y'])
            self.paint_v_tunnel(new_room.center['y'], old_room.center['y'], xmidpoint)
            self.paint_h_tunnel(xmidpoint, old_room.center['x'], old_room.center['y'])
        elif pathtype == 1:

            # startroom room a

            self.paint_v_tunnel(new_room.center['y'], ymidpoint, new_room.center['x'])
            self.paint_h_tunnel(new_room.center['x'], old_room.center['x'], ymidpoint)
            self.paint_v_tunnel(ymidpoint, old_room.center['y'], old_room.center['x'])
        elif pathtype == 2:

            # startroom new_room

            self.paint_h_tunnel(new_room.center['x'], old_room.center['x'], new_room.center['y'])
            self.paint_v_tunnel(new_room.center['y'], old_room.center['y'], old_room.center['x'])
        else:

            # startroom old_room

            self.paint_v_tunnel(new_room.center['y'], old_room.center['y'], new_room.center['x'])
            self.paint_h_tunnel(new_room.center['x'], old_room.center['x'], old_room.center['y'])

    def paint_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.spaces[y][x] = RogueDungeon.RoomTile(room.roomid)

    def paint_h_tunnel(self, x1, x2, y):
        lasttile = None
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if type(self.spaces[y][x]) is RogueDungeon.RoomTile and type(lasttile) is RogueDungeon.HallTile:

                    # Ignore room tiles, but track that the last tile was a room tile

                lasttile.isdoorway = True
            elif type(self.spaces[y][x]) is RogueDungeon.Tile:
                self.spaces[y][x] = RogueDungeon.HallTile()
                if type(lasttile) is RogueDungeon.RoomTile:
                    self.spaces[y][x].isdoorway = True
            lasttile = self.spaces[y][x]

    def paint_v_tunnel(self, y1, y2, x):
        lasttile = None
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if type(self.spaces[y][x]) is RogueDungeon.RoomTile and type(lasttile) is RogueDungeon.HallTile:

                    # Ignore room tiles, but track that the last tile was a room tile

                lasttile.isdoorway = True
            elif type(self.spaces[y][x]) is RogueDungeon.Tile:
                self.spaces[y][x] = RogueDungeon.HallTile()
                if type(lasttile) is RogueDungeon.RoomTile:
                    self.spaces[y][x].isdoorway = True
            lasttile = self.spaces[y][x]

    def printfloor(self):
        output = ''
        for row in self.spaces:
            for cell in row:
                output += str(cell) + ' '
            output += '\n'
        return output

    class Tile(object):

        def __init__(self, char='#'):
            """ test """

        # def __init__(self, char='#'):

            self.char = char
            self.isdoorway = False
            self.passable = False

        def __str__(self):
            return self.char.encode('utf8')

    class RoomTile(Tile):

        def __init__(self, roomid):
            """ test """

            self.roomid = roomid
            self.char = '.'
            self.isdoorway = False
            self.passable = True

    class HallTile(Tile):

        def __init__(self, char='.'):
            """ test """

            self.char = char
            self.isdoorway = False
            self.passable = True

    class Room(object):

        roomid = 0

        def __init__(self, x, y, w, h):
            """ test """

            RogueDungeon.Room.roomid += 1
            self.egress = False
            self.roomid = RogueDungeon.Room.roomid
            self.x1 = x
            self.y1 = y
            self.x2 = x + w
            self.y2 = y + h
            center_x = (self.x1 + self.x2) / 2
            center_y = (self.y1 + self.y2) / 2
            self.center = {'x': center_x, 'y': center_y}

        def intersect(self, other):

            # returns true if this rectangle intersects with another one

            return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1


# http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_3

# Garbage I was playing around with.

# class UpTile(DungeonTile):
#    def __init__(self, char=u'ߡ'):
#        """ test """
#        self.char=char
#        self.passable=False
#
# class DownTile(DungeonTile):
#    def __init__(self, char=u'ߜ'):
#        """ test """
#        self.char=char
#        self.passable=False
#
# class PortalTile(DungeonTile):
#    def __init__(self, char=u'Ω'):
#        """ test """
#        self.char=char
#        self.passable=False
#
# class WaterTile(DungeonTile):
#    def __init__(self, char=u'ω'):
#        """ test """
#        self.char=char
#        self.passable=False
#
#
# class LavaTile(DungeonTile):
#    def __init__(self, char=u'Ж'):
#    #def __init__(self, char=u'ж'):
#        """ test """
#        self.char=char
#        self.passable=False
