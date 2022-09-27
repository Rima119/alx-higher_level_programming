#!/usr/bin/python3
"""add_item"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    file = "add_item.json"
    try:
        list_p = load_from_json_file(file)
    except FileNotFoundError:
        list_p = []
    for n in sys.argv[1:]:
        list_p.append(n)
    save_to_json_file(list_p, file)
