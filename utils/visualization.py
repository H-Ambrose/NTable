# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import os
import random

"""改变HSV不需要改变annotation"""
"""所以对应关系为：
    /home/zhuziyi/subject2020/sceneTable/dataset_augmented/HSV
    /home/zhuziyi/subject2020/sceneTabel/yolo_anno
"""
"""anno_dir = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/annotation/rotate/'
img_dir = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/rotate/'"""
save_dir = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/A_ori/'
img_dir = '/home/zhuziyi/subject2020/sceneTable/dataset/'
anno_dir = '/home/zhuziyi/subject2020/sceneTable/yolo_anno/'


def main():
    img_list = os.listdir(img_dir)
    for i in range(len(img_list)):
        img = cv2.imread(img_dir + img_list[i])
        f = open(anno_dir + img_list[i][0:-4] + '.txt', "r")
        for line in f.readlines():
            point = line.strip('\n').split(' ')
            point = [float(i) for i in point]
            h, w = img.shape[0:2]
            center_x = w * point[1]
            center_y = h * point[2]
            ww = w * point[3]
            hh = h * point[4]
            x1 = int(center_x - ww / 2)
            y1 = int(center_y - hh / 2)
            x4 = int(center_x + ww / 2)
            y4 = int(center_y + hh / 2)
            img = cv2.rectangle(img, (x1, y1), (x4, y4), (0, 0, 255), 2)
        cv2.imwrite(save_dir + img_list[i], img)
        if i == 99:
            break


if __name__ == '__main__':
    main()
