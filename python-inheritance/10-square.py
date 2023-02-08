#!/usr/bin/python3

"""t
his task is for implimenting squar 
from Rectangle
"""

class Square (Rectangle):
    """the class square is a subclass from
rectangle

    Args:
            Rectangle (_type_): _description_
    """

    def __init__(self, size):
    	self.integer_validator("size", size)
    	super().__init__(size, size)
