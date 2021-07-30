# -*- coding: UTF-8 -*-
import os
import shutil
import random
from PIL import Image
from PIL import ImageEnhance

img_dir = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/tmp/'
save_dir = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/temp/'


def contrast(imgdir1='./midata/ori/', imgdir2='./midata/cam/',
             anodir1='./midata/ori_annotations/', anodir2='./midata/cam_annotations/', pad='_3'):
    """改变对比度不需要改变annotation"""
    img_list = os.listdir(imgdir1)
    for i in range(len(img_list)):
        """PIL"""
        img = Image.open(imgdir1 + img_list[i])
        enh_con = ImageEnhance.Contrast(img)
        contrastimg = random.uniform(0.49, 1.51)
        if contrast == 1.0:  # 两次机会(
            contrastimg = random.uniform(0.49, 1.51)
        image_contrasted = enh_con.enhance(contrastimg)
        image_contrasted.save(imgdir2 + img_list[i][0:-4] + pad + '.jpg')
        shutil.copyfile(anodir1 + img_list[i][0:-4] + '.txt', anodir2 + img_list[i][0:-4] + pad + '.txt')


def main():
    contrast()


if __name__ == '__main__':
    main()
