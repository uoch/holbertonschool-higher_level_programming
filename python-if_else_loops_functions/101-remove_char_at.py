#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i != n:
            if (65 <= ord(str[i]) <= 90 or 97
                    <= ord(str[i]) <= 122) or str[i] == " ":
                new_str += str[i]
    return new_str
