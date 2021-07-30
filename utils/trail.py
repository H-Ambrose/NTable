# -*- coding: UTF-8 -*-
import json

with open('trail.json', 'r') as json1:
    load_dict = json.load(json1)
    print(load_dict)
