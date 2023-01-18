#!/usr/bin/python3
def uppercase(str):
    ch = ""
    for i in str:
        if ord(i) in range(97, 123):
            k = ord(i) - 32
            ch += chr(k)
        else:
            ch += i
    print("{}".format(ch))
