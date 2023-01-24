#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first two elements of each tuple, or 0 if the tuple is too short
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    # Add the corresponding elements of the two tuples
    result = (a1 + b1, a2 + b2)
    return result
