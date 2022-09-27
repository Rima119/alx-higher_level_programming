#!/usr/bin/python3
"""add_item"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    list_p = load_from_json_file(file)
except Exception:
    list_p = []
for n in sys.argv[1:]:
    list_p.append(str(n))
save_to_json_file(list_p, file)
