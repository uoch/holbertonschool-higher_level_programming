#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while x > 0:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except:
            break
        x -= 1
    print()
    return i
