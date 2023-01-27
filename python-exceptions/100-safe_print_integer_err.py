#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        sys.stderr.write(
            "Exception: unsupported format string passed to set.__format__")
        return False
