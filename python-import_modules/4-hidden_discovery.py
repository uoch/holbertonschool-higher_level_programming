#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    for i in dir(hidden_4):
        if i.find("__") == 0:
            continue
        print(i)
