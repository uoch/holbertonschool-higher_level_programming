#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = len(sys.argv)

    if (k <= 1):
        print("{} arguments.".format(k-1))
    elif (k <= 2):
        print("{} argument:".format(k-1))
        print("{}: {}".format(k-1, sys.argv[k-1]))
    else:
        for i in range(k):
            if (i == 0):
                print("{} arguments:".format(len(sys.argv)-1))
            else:
                print("{}: {}".format(i, sys.argv[i]))
