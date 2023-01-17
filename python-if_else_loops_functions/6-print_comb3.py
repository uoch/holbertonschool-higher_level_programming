#!/usr/bin/python3
for i in range(0, 10):
    for j in range(10):
        if (i != j and (i-j) != 0) and (i-j) != 1 and (i-j) != 2 and \
            (i-j) != 3 and (i-j) != 4 and (i-j) != 5 and (i-j) != 6\
                and (i-j) != 7 and (i-j) != 8 and (i-j) != 9:
            print("{}".format(i) + "{}".format(j),
                  (", " if (i+j) != 17 else "\n"), end="")
