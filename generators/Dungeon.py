
import math
import random
import json
from generators.Generator import Generator
import sys
import pprint

class Dungeon(object):

    def __init__(self):
        """ test """
        self.floor=DungeonFloor(30,20)

        self.floor.printfloor()

class DungeonFloor():
    def __init__(self,width,height):
        """ test """
        self.spaces = [ [ DungeonTile() for i in range(width) ] for j in range(height) ]

        self.createRoom()


    def printfloor(self):
        for row in self.spaces:
            for cell in row:
                print cell,
            sys.stdout.write("\n")



class DungeonTile():
    def __init__(self, char='#'):
        """ test """
        self.char=char

    def __str__(self):
        return self.char






class DungeonRoom():
    def __init__(self):
        """ test """


#http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_3
