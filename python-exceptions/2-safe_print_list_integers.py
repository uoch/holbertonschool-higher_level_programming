#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    k = 0
    while x > 0:
        try:
            if isinstance(my_list[k], int):
                print("{:d}".format(my_list[k]), end="")
                i += 1
            k += 1
        except IndexError:
            print("Traceback (most recent call last):")
        x -= 1
    print()
    return i
