# -*- coding: UTF-8 -*-
import shutil
import random
import os
import json


def data_split(oridir='./midata/ori', shuffle=True):
    # train:test:val=7:2:1
    """ 数据集拆分: 将列表full_list按比例ratio（随机）划分为3个子列表 """
    full_list = os.listdir(oridir)
    ratio = [0, 0, 0]
    ratio[0] = round(len(full_list) * 0.7)
    ratio[1] = round(len(full_list) * 0.2)
    ratio[2] = len(full_list) - ratio[0] - ratio[1]
    if shuffle:
        # 在一个文件夹中进行
        random.shuffle(full_list)

    sublist_1 = full_list[:ratio[0]]
    assert ratio[0] == len(sublist_1)

    sublist_2 = full_list[ratio[0]:][:ratio[1]]
    assert ratio[1] == len(sublist_2)

    sublist_3 = full_list[ratio[0] + ratio[1]:]
    assert ratio[2] == len(sublist_3)

    return sublist_1, sublist_2, sublist_3


def json_data(name, i, setype):
    data = {'imgid': i, 'filename': name, 'split': setype, 'source': 'textual/electronic/wild',
            'shape': 'upright/oblique/distorted', 'anno': []}

    json_f = open('./midata/ori_annotations/' + name[0:-3] + 'json', 'r')
    load_dict = json.load(json_f)
    tables = load_dict['shapes']
    table = tables[0]
    label = table['label'].split(',')
    data['shape'] = label[0]
    data['source'] = label[1]

    with open('./midata/ori_annotations/' + name[0:-3] + 'txt', "r") as f:
        txt = f.readlines()
        for w in txt:
            w = w.replace('\n', '')
            data['anno'].append(w)

    ''' for example: '''
    # {"imgid": 0,
    # "filename": "ics_26_4.jpg",
    # "split": "val",
    # "source": "textual",
    # "shape": "distorted",
    # "anno": ["0 0.5450496453900708 0.6752553191489361 0.7390070921985813 0.18829787234042555"]}
    return data


def writein(setype, img_list):  # for example: 'train', train_list
    # separately generate NTable-ori and NTable-cam and their corresponding txt, json annotations
    # NTable-ori
    fori = open('./NTable-ori/' + setype + '.txt', "a")
    dataori = []
    # NTable-cam
    fcam = open('./NTable-cam/' + setype + '.txt', "a")
    datacam = []
    cnt = 0
    cnt1 = 0

    for name in img_list:  # name is get from ./midata/ori, so its formation is xxxxxxxxx.jpg (without _x)
        # NTable-ori
        shutil.copyfile('./midata/ori/' + name, './NTable-ori/' + setype + '/' + name)
        shutil.copyfile('./midata/ori_annotations/' + name[0:-3] + 'txt',
                        './NTable-ori/annotation/' + setype + '/' + name[0:-3] + 'txt')
        data = json_data(name, cnt, setype)
        dataori.append(data)
        cnt = cnt + 1
        fori.write(name)
        fori.write('\r\n')

        # NTable-cam
        inds = ['_0', '_1', '_2', '_3', '_4', '_5', '_6', '_7']
        for ind in inds:
            n = name[0:-4] + ind
            shutil.copyfile('./midata/cam/' + n + '.jpg', './NTable-cam/' + setype + '/' + n + '.jpg')
            shutil.copyfile('./midata/cam_annotations/' + n + '.txt',
                            './NTable-ori/annotation/' + setype + '/' + n + '.txt')
            data2 = data.copy()  # only need to change data[anno]
            data2['filename'] = n + '.jpg'
            data2['anno'] = []
            data2['imgid'] = cnt1
            with open('./midata/cam_annotations/' + n + '.txt', "r") as f:
                txt = f.readlines()
                for w in txt:
                    w = w.replace('\n', '')
                    data2['anno'].append(w)
            datacam.append(data2)
            cnt1 = cnt1 + 1
            fcam.write(n + '.jpg')
            fcam.write('\r\n')

    # write in the json file:
    with open('./NTable-ori/' + setype + '.json', 'r') as json1:
        load_dict = json.load(json1)
        load_dict['information'] = load_dict['information'] + dataori
        json2 = open('./NTable-ori/' + setype + '_new.json', 'w')
        json.dump(load_dict, json2)
        os.remove('./NTable-ori/' + setype + '.json')
        os.rename('./NTable-ori/' + setype + '_new.json', './NTable-ori/' + setype + '.json')

    with open('./NTable-cam/' + setype + '.json', 'r') as json1:
        load_dict = json.load(json1)
        load_dict['information'] = load_dict['information'] + datacam
        json2 = open('./NTable-cam/' + setype + '_new.json', 'w')
        json.dump(load_dict, json2)
        os.remove('./NTable-cam/' + setype + '.json')
        os.rename('./NTable-cam/' + setype + '_new.json', './NTable-cam/' + setype + '.json')


def sampling():
    train_list, test_list, val_list = data_split(oridir='./midata/ori')  # get the image lists
    writein('train', train_list)
    writein('test', test_list)
    writein('val', val_list)


def main():
    sampling()


if __name__ == "__main__":
    # execute only if run as a script
    main()
