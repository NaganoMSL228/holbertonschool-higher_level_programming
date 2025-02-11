#!/usr/bin/python3
'''Module for add_item function'''

import sys
import os.path
import json

def add_item():
    '''adds all arguments to a Python list, and then save them to a file'''
    filename = 'add_item.json'
    if os.path.exists(filename):
        with open(filename,
                    'r', encoding='utf-8') as f:
                my_list = json.load(f)
    else:
        my_list = []
    my_list.extend(sys.argv[1:])
    with open
    (filename, 'w', encoding='utf-8') as f:
    json.dump(my_list, f)
