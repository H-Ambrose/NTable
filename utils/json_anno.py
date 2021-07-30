# -*- coding: UTF-8 -*-
import json
import os
import re


def getRootName(name):
    j = 0
    for k in range(len(name)):
        if name[k] == '_':
            j += 1
        if j == 2:
            return name[0:k] + '.jpg'


data_list_all = []
textual_list = os.listdir('./split_source/textual')
electronic_list = os.listdir('./split_source/electronic')
wild_list = os.listdir('./split_source/wild')

upright_list = os.listdir('./split_shape/upright')
oblique_list = os.listdir('./split_shape/oblique')
distorted_list = os.listdir('./split_shape/distorted')

stat = {'train': {'textual': 0, 'electronic': 0, 'wild': 0, 'upright': 0, 'oblique': 0, 'distorted': 0},
        'test': {'textual': 0, 'electronic': 0, 'wild': 0, 'upright': 0, 'oblique': 0, 'distorted': 0},
        'val': {'textual': 0, 'electronic': 0, 'wild': 0, 'upright': 0, 'oblique': 0, 'distorted': 0}}

for dat in ['train', 'val', 'test']:
    data_list = []
    img_list = os.listdir('./dataset_scene_all/' + dat)
    # 依次处理train, val, test
    for i in range(len(img_list)):
        data = {'imgid': i, 'filename': img_list[i], 'split': dat, 'source': 'textual/electronic/wild',
                'shape': 'upright/oblique/distorted', 'anno': []}
        img_name = getRootName(img_list[i])

        if img_name in textual_list:
            data['source'] = 'textual'
            stat[dat]['textual'] += 1
        elif img_name in electronic_list:
            data['source'] = 'electronic'
            stat[dat]['electronic'] += 1
        else:
            data['source'] = 'wild'
            stat[dat]['wild'] += 1

        if img_name in upright_list:
            data['shape'] = 'upright'
            stat[dat]['upright'] += 1
        elif img_name in oblique_list:
            data['shape'] = 'oblique'
            stat[dat]['oblique'] += 1
        else:
            data['shape'] = 'distorted'
            stat[dat]['distorted'] += 1

        data['anno'] = []
        with open('./dataset_scene_all/annotation/' + dat + '/' + img_list[i][0:-3] + 'txt', "r") as f:
            txt = f.readlines()
            for w in txt:
                w = w.replace('\n', '')
                data['anno'].append(w)
        data_list.append(data)
        data_list_all.append(data)

    # 写入data文件
    with open('./dataset_scene_all/' + dat + '.json', 'w') as f:
        json.dump(data_list, f)

with open('./dataset_scene_all/info.json', 'w') as f:
    json.dump(data_list_all, f)

print(stat)
"""json_str = json.dumps(data)
print(type(json_str))
print(json_str)"""
