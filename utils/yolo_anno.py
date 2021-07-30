# -*- coding: UTF-8 -*-
import json
import cv2
import shutil
import os


def move_files(srcdir, desdir):
    """move images and annotations(in json) separately"""
    filelist = os.listdir(srcdir)
    for filename in filelist:
        path1 = os.path.join(srcdir, filename)
        if filename.find('.json') != -1:
            path2 = os.path.join(desdir, 'ori_annotations/', filename)
            shutil.copyfile(path1, path2)
            # shutil.move(path1, path2)
        else:
            path2 = os.path.join(desdir, 'ori/', filename)
            shutil.copyfile(path1, path2)
            # shutil.move(path1, path2)


def json_anno(json_dir='./midata/ori_annotations/', image_dir='./midata/ori/'):
    """ generate yolo version annotations from json version
        A JSON-formatted annotation with complete information is also generated """
    json_list = os.listdir(json_dir)  # get the json list
    # print(json_list)

    for i in range(len(json_list)):
        json_file = json_list[i]

        f = open(json_dir + json_file[0:-5] + ".txt", "a")  # so txt and json are all in ori_annotations
        img = cv2.imread(image_dir + json_file[0:-5] + ".jpg")
        try:
            y, x = img.shape[0:2]
        except AttributeError:
            print(json_file)
            exit(0)
        # y, x = img.shape[0:2]

        json_f = open(json_dir + json_file, 'r')
        load_dict = json.load(json_f)
        tables = load_dict['shapes']
        for table in tables:
            # every time a table
            points = table['points']

            x0 = points[0][0]
            y0 = points[0][1]
            x1 = points[1][0]
            y1 = points[1][1]

            mid_x = (float(x0) + float(x1)) / 2 / x
            mid_y = (float(y0) + float(y1)) / 2 / y
            width = (float(x1) - float(x0)) / x
            height = (float(y1) - float(y0)) / y

            f.write('0 ' + str(mid_x) + ' ' + str(mid_y) + ' ' + str(width) + ' ' + str(height))
            f.write('\r\n')
        # delete the original json files
        # os.remove(json_dir + json_file)


def main():
    print('part the "orimage" file into "images" and "annotations"')
    move_files('./orimage/', './midata/')

    print('generate json to YOLO')
    json_anno('./midata/ori_annotations/', './midata/ori/')


if __name__ == "__main__":
    # execute only if run as a script
    main()
