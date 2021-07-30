# -*- coding: UTF-8 -*-
import shutil
import os


def move_ori(srcdir='./midata/ori', desdir='./midata/cam'):
    subdir = ['/', '_annotations/']
    items = os.listdir(srcdir)  # get the image list
    for item in items:
        shutil.copyfile(srcdir + subdir[0] + item, desdir+subdir[0]+item[0:-4]+'_0.jpg')
        shutil.copyfile(srcdir + subdir[1] + item[0:-3]+'txt', desdir+subdir[1]+item[0:-4]+'_0.txt')
