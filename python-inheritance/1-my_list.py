#!/usr/bin/python3
"""1-my list
    """


class MyList(list):
    """_summary_

    Args:
        list (list): The super() call in print_sorted()
        will call the sort() method of the parent class list.
    """

    def print_sorted(self):
        s = self.copy()
        s.sort()
        print(s)

    def __str__(self):
        return str(list(self))
