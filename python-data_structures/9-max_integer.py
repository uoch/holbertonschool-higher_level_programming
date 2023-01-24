#!/usr/bin/python3
def max_integer(my_list=[]):
    k = 0
    n= 0
    for i in range(len(my_list)):
        k = my_list[n]
        for j in range(1,len(my_list)):
            if k < my_list[j]:
                k = my_list[j]
        n+=1
    return(k)
