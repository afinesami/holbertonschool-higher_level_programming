#!/usr/bin/python3
''' First rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''class Rectangle inherits from base
    '''
    KV_dict = {'id': 'id', 'width': '_Rectangle__width',
               'height': '_Rectangle__height',
               'x': '_Rectangle__x', 'y': '_Rectangle__y'}

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method __init__ Initialization a Rectangle
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        '''method update
        '''
        key_list = ['id', '_Rectangle__width', '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        KV_dict = {'id': 'id', 'width': '_Rectangle__width',
                   'height': '_Rectangle__height',
                   'x': '_Rectangle__x', 'y': '_Rectangle__y'}
        for idx, el in enumerate(args):
            self.__dict__[key_list[idx]] = el
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__dict__[KV_dict[key]] = val
