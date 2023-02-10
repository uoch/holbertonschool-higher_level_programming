#!/usr/bin/python3
"""7-add_item.py"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    if len(sys.argv)==1:
        try:
            items = load_from_json_file("add_item.json")
        except FileNotFoundError:
            items = []
    else:
        items.append(sys.argv[1:])
        save_to_json_file(items, "add_item.json")