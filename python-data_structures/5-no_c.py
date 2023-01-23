#!/usr/bin/python3
def no_c(my_string):
    ch = ""
    for i in my_string:
        if (i == "c") or (i == "C"):
            i = ""
        ch += i
    return ch
