#!/usr/bin/python3
"""rectangle.py
is a class inherteds
from Base"""

from models.base import Base
from models.rectangle import Rectangle


class Square (Rectangle):
    """Square

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    super(Rectangle, self).__init__(args[0])
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                super(Rectangle, self).__init__(kwargs['id'])

    def to_dictionary(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
