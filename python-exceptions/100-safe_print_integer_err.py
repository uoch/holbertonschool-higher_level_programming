#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return False
    except TypeError as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return False
