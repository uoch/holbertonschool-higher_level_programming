#!/usr/bin/python3

"""t
his task is for implimenting squar 
from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle



class Square (Rectangle):
	"""Square

	Args:
		Rectangle (mother_class):
	"""
	def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
