#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = len(sys.argv)
    r = 0
    if (k <= 1):
        print("0")
        sys.exit()
    for i in range(1, k):
        if sys.argv[i].isnumeric() or (sys.argv[i][1:].isnumeric()
                                       and sys.argv[i][0] == '-'):
            r += int(sys.argv[i])
    print(r)
