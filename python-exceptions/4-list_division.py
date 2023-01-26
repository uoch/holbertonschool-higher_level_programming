#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = []

    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                n.append(my_list_1[i]/my_list_2[i])
            else:
                print("wrong type")
                n.append(0)
        except ZeroDivisionError:
            print("division by 0")
            n.append(0)
        except IndexError:
            print("out of range")
            n.append(0)
        finally:
            pass
    return n
