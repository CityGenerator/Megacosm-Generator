#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random
import json
from generators.Generator import Generator
from util import Seeds

import sys
import pprint

class Dungeon(Generator):
    def __init__(self, redis, features={}):
        """ test """
        Generator.__init__(self,redis,features)

        #print self.seed
        self.floor=DungeonFloor(80,50)

        self.map=self.floor.printfloor()

class DungeonFloor(object):
    def __init__(self,width,height):
        """ test """
        self.width=width
        self.height=height
        self.spaces = [ [ DungeonTile() for i in range(width) ] for j in range(height) ]
        self.rooms = []
        self.generate_rooms()


    def convert_to_json(self):
        resultmatrix=[]
        for evenrow,oddrow in zip(self.spaces[0::2], self.spaces[1::2]):
            row=[]
            for a,b,c,d in zip(evenrow[0::2], evenrow[1::2], oddrow[0::2], oddrow[1::2],):
                tile=self.tiletype(a,b,c,d)
                row.append(tile)
            resultmatrix.append(row)
        return resultmatrix

    def tiletype(self,a,b,c,d):
        return str(int(a.passable))+str(int(b.passable))+str(int(c.passable))+str(int(d.passable))







    def create_random_room(self):
        ROOM_MAX_SIZE = 10
        ROOM_MIN_SIZE = 4
        w = random.randint( ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = random.randint( ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        #random position without going out of the boundaries of the map
        x = random.randint( 0, self.width - w - 1)
        y = random.randint( 0, self.height - h - 1)
        return DungeonRoom(x, y, w, h)

    def generate_rooms(self):
        MAX_ROOMS =20
        loop=1
        for r in range(MAX_ROOMS):
            loop +=1
            new_room=self.create_random_room()

            failed = False
            for other_room in self.rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break
            if not failed:
                self.paint_room(new_room)
                (new_x, new_y) = new_room.center()
                new_room.roomid,", it's center is",new_x,",",new_y
                if len(self.rooms) == 0:
                    """d"""
                else:
                    #center coordinates of previous room
#                    (prev_x, prev_y) = self.rooms[-1].center() ; random.randint(1,2) # meh
                    (prev_x, prev_y) = random.choice(self.rooms).center()
                    pathtype=random.randint(0,3)
                    if pathtype == 0:
                        ymidpoint=random.randint(min(prev_y,new_y),max(prev_y,new_y))
                        xmidpoint=random.randint(min(prev_x,new_x),max(prev_x,new_x))
                        self.paint_h_tunnel(prev_x, xmidpoint, prev_y)
                        self.paint_v_tunnel(prev_y, new_y, xmidpoint)
                        self.paint_h_tunnel(xmidpoint, new_x, new_y)
                    elif pathtype ==1:
                        ymidpoint=random.randint(min(prev_y,new_y),max(prev_y,new_y))
                        xmidpoint=random.randint(min(prev_x,new_x),max(prev_x,new_x))
                        self.paint_v_tunnel(prev_y, ymidpoint, prev_x)
                        self.paint_h_tunnel(prev_x, new_x, ymidpoint)
                        self.paint_v_tunnel(ymidpoint, new_y, new_x)
                    elif pathtype ==2:
                        #first move horizontally, then vertically
                        self.paint_h_tunnel(prev_x, new_x, prev_y)
                        self.paint_v_tunnel(prev_y, new_y, new_x)
                    else:
                        #first move vertically, then horizontally
                        self.paint_v_tunnel(prev_y, new_y, prev_x)
                        self.paint_h_tunnel(prev_x, new_x, new_y)
                self.rooms.append(new_room)
 

    def paint_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.spaces[y][x]=FloorTile()
    def paint_h_tunnel(self,x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
                self.spaces[y][x]=FloorTile()
    
    def paint_v_tunnel(self,y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
                self.spaces[y][x]=FloorTile()

    def paint_zig_tunnel(self,x1,y1,x2,y2):
        """ TODO """



    def printfloor(self):
        output=""
        for row in self.spaces:
            for cell in row:
                output+=str(cell)+" "
            output+="\n"
        print output
        return output



class DungeonTile(object):
    def __init__(self, char='#'):
    #def __init__(self, char='#'):
        """ test """
        self.char=char
        self.passable=False

    def __str__(self):
        return self.char.encode('utf8')


class FloorTile(DungeonTile):
    def __init__(self, char='.'):
        """ test """
        self.char=char
        self.passable=True




class DungeonRoom(object):
    roomid=0
    def __init__(self, x, y, w, h):
        """ test """
        DungeonRoom.roomid+=1
        self.roomid=DungeonRoom.roomid
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
 
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)





#http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_3








# Garbage I was playing around with.

class UpTile(DungeonTile):
    def __init__(self, char=u'ߡ'):
        """ test """
        self.char=char
        self.passable=False

class DownTile(DungeonTile):
    def __init__(self, char=u'ߜ'):
        """ test """
        self.char=char
        self.passable=False

class PortalTile(DungeonTile):
    def __init__(self, char=u'Ω'):
        """ test """
        self.char=char
        self.passable=False

class WaterTile(DungeonTile):
    def __init__(self, char=u'ω'):
        """ test """
        self.char=char
        self.passable=False


class LavaTile(DungeonTile):
    def __init__(self, char=u'Ж'):
#    def __init__(self, char=u'ж'):
        """ test """
        self.char=char
        self.passable=False
