#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except ZeroDivisionError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
    except IndexError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
