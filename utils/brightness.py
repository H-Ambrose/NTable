# -*- coding: UTF-8 -*-
import os
import shutil
import random
from skimage import data, exposure, img_as_float
import skimage.io


def brightness(imgdir1='./midata/ori/', imgdir2='./midata/cam/',
               anodir1='./midata/ori_annotations/', anodir2='./midata/cam_annotations/', pad='_2'):
    img_list = os.listdir(imgdir1)
    for i in range(len(img_list)):
        img = skimage.io.imread(imgdir1 + img_list[i])
        gate = random.random()
        if gate > 0.5:
            # 调暗
            gam = exposure.adjust_gamma(img, random.uniform(1, 1.9))
        else:
            # 调亮
            gam = exposure.adjust_gamma(img, random.uniform(0.45, 1))
        skimage.io.imsave(imgdir2 + img_list[i][0:-4] + pad + '.jpg', gam)  # [0:-4] + '_4.jpg'
        """改变亮度不需要改变annotation"""
        shutil.copyfile(anodir1 + img_list[i][0:-4] + '.txt', anodir2 + img_list[i][0:-4] + pad + '.txt')


def main():
    brightness()


if __name__ == '__main__':
    main()
