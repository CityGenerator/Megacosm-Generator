#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from generators.Generator import Generator
from util import Seeds
import logging
import json
class GeomorphDungeon(Generator):



    # This is a simple translation table 
    # bits are sorted [ left bottom right top ]
    CELL_TYPES={  
                   '0b0': {'type':'0000', 'rotation':0  }, # No connections
                   '0b1': {'type':'0001', 'rotation':0  },   # one side
                  '0b10': {'type':'0001', 'rotation':1  },   # one side
                  '0b11': {'type':'0010', 'rotation':0  },     # twoside corner
                 '0b100': {'type':'0001', 'rotation':2  },   # one side
                 '0b101': {'type':'0011', 'rotation':0  },     # twoside straight
                 '0b110': {'type':'0010', 'rotation':1  },     # twosided corner
                 '0b111': {'type':'0100', 'rotation':0  },       #Three sides
                '0b1000': {'type':'0001', 'rotation':3  },   # one side
                '0b1001': {'type':'0010', 'rotation':3  },     # twosided corner
                '0b1010': {'type':'0011', 'rotation':1  },     # twosided straight
                '0b1011': {'type':'0100', 'rotation':3  },       # three sides
                '0b1100': {'type':'0010', 'rotation':2  },     # twosided corner
                '0b1101': {'type':'0100', 'rotation':2  },       # threesided
                '0b1110': {'type':'0100', 'rotation':1  },       # three sides
                '0b1111': {'type':'0101', 'rotation':0  }          # Four connections
                }



    def __init__(self, redis, features={}):
        """ Generate a Geomorph-like dungeon """
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)
        self.generate_features('dungeon')

        self.apply_text_template() #FIXME refactor with RogueDungeon on dungeon names...
        self.width=self.gridwidth['tiles']
        self.height=self.gridheight['tiles']

        self.generate_grid()
        self.generate_connections()
        self.set_tiletypes()

    def apply_text_template(self):
        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text.title()


    def convert_to_json(self):
        resultmatrix=[]
        for row in self.spaces:
            resultrow=[]
            for cell in row:
                resultrow.append({
                            "path":cell.image,
                            "rotation":cell.imagerotation,
                            } )
            resultmatrix.append(resultrow)
        return resultmatrix


    def set_tiletypes(self):
        for row in self.spaces:
            for cell in row:
                #calculate the binary "cell type"
                cell.tiletype=bin( (cell.left << 3) + (cell.bottom << 2) + (cell.right<<1) + ( cell.top<<0 ))

                #translate it with the table
                cell.imagetype=int(self.CELL_TYPES[cell.tiletype]['type'],2)

                #Using the proper cell type, select an image from redis
                tiledata= json.loads( self.rand_value('geomorph_type_'+str(cell.imagetype)) )
                cell.image=str(tiledata['path'])
                cell.author=str(tiledata['author'])
                cell.tileset=str(tiledata['tileset'])
                # Make sure to capture the rotation needed
                cell.imagerotation= self.CELL_TYPES[cell.tiletype]['rotation']

    def generate_grid(self):
        
        self.spaces = [ [ GeomorphDungeon.Tile(i,j) for i in range(self.width) ] for j in range(self.height) ]

    def generate_connections(self):
        alltiles=[]
        for row in self.spaces:
            for cell in row:
                alltiles.append(cell)

        random.shuffle(alltiles)

        for cell in alltiles:
            self.calculate_top(cell)
            self.calculate_right(cell)
            self.calculate_bottom(cell)
            self.calculate_left(cell)

    def calculate_top(self, cell):
            if cell.y ==0:
                cell.top=False
            elif self.spaces[cell.y-1][cell.x].bottom != None :
                cell.top=self.spaces[cell.y-1][cell.x].bottom
            else:
                if random.randint(0,self.segmentation['solidchance']) ==0:
                    cell.top=False
                else:
                    cell.top=True
        
    def calculate_right(self, cell):
            if cell.x == len(self.spaces[0])-1:
                cell.right=False
            elif self.spaces[cell.y][cell.x+1].left != None :
                cell.right=self.spaces[cell.y][cell.x+1].left
            else:
                if random.randint(0,self.segmentation['solidchance']) ==0:
                    cell.right=False
                else:
                    cell.right=True

    def calculate_bottom(self, cell):
            if cell.y == len(self.spaces)-1:
                cell.bottom=False
            elif self.spaces[cell.y+1][cell.x].top != None :
                cell.bottom=self.spaces[cell.y+1][cell.x].top
            else:
                if random.randint(0,self.segmentation['solidchance']) ==0:
                    cell.bottom=False
                else:
                    cell.bottom=True
        
    def calculate_left(self, cell):
            if cell.x == 0:
                cell.left=False
            elif self.spaces[cell.y][cell.x-1].right != None :
                cell.left=self.spaces[cell.y][cell.x-1].right
            else:
                if random.randint(0,self.segmentation['solidchance']) ==0:
                    cell.left=False
                else:
                    cell.left=True

    
    class Tile(object):
        def __init__(self,x,y ):
        #def __init__(self, char='#'):
            """ test """
            self.left=None
            self.right=None
            self.top=None
            self.bottom=None
            self.char='#'
            self.x=x
            self.y=y
    
