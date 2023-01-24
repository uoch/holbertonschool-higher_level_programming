#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if my_list is None:
        return None
    for i in range(len(my_list)):
        if my_list[i] % 2:
            new.append(False)
        else:
            new.append(True)
    return new
