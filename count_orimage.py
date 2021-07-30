# -*- coding: UTF-8 -*-
import os
import json

json_list = []
filelist = os.listdir('./orimage/')
data = {'upright': 0, 'oblique': 0, 'distorted': 0, 'textual': 0, 'electronic': 0, 'wild': 0}
for filename in filelist:
    if filename.find('.json') != -1:
        json_list.append(filename)

for json_file in json_list:
    json_f = open('./orimage/' + json_file, 'r')
    load_dict = json.load(json_f)
    tables = load_dict['shapes']
    for table in tables:
        label = table['label'].replace(' ', '').split(',')
        data[label[0]] += 1
        data[label[1]] += 1

print(data)