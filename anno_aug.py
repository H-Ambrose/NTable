# -*- coding: UTF-8 -*-
import shutil
import os
import utils.yolo_anno as yolo_anno
import utils.gadget as gadget
import utils.rotate as rotate
import utils.brightness as brightness
import utils.contrast as contrast
import utils.sampling as sampling


def main():
    """
    RULES of augmentation:
    original 0
    rotate 1
    brightness 2
    contrast 3
    contrast & brightness 4
    rotate & brightness 5
    rotate & contrast 6
    rotate & contrast & brightness 7
    """
    """
    print('part the "orimage" file into "images" and "annotations"')
    yolo_anno.move_files('./orimage', './midata/')

    print('generate json to YOLO')
    yolo_anno.json_anno('./midata/ori_annotations/', './midata/ori/')

    # begin augmentation
    # rotate/brightness/contrast use different Library
    print('NTable-cam original 0')
    gadget.move_ori(srcdir='./midata/ori', desdir='./midata/cam')
    """
    print('NTable-cam rotate 1')
    rotate.rotate(imgdir1='./midata/ori/', imgdir2='./midata/cam/', pad='_1')
    print('NTable-cam brightness 2')
    brightness.brightness(imgdir1='./midata/ori/', anodir1='./midata/ori_annotations/', pad='_2')
    print('NTable-cam contrast 3')
    contrast.contrast(imgdir1='./midata/ori/', anodir1='./midata/ori_annotations/', pad='_3')

    print('NTable-cam contrast & brightness 4')
    os.mkdir('./midata/temp_annotations')
    os.mkdir('./midata/temp')
    contrast.contrast(imgdir1='./midata/ori/', imgdir2='./midata/temp/',
                      anodir1='./midata/ori_annotations/', anodir2='./midata/temp_annotations/', pad='')
    brightness.brightness(imgdir1='./midata/temp/', imgdir2='./midata/cam/',
                          anodir1='./midata/temp_annotations/', anodir2='./midata/cam_annotations/', pad='_4')
    shutil.rmtree('./midata/temp_annotations')
    shutil.rmtree('./midata/temp')
    os.mkdir('./midata/temp_annotations')
    os.mkdir('./midata/temp')

    print('NTable-cam rotate & brightness 5')
    rotate.rotate(imgdir1='./midata/ori/', imgdir2='./midata/temp/',
                  anodir1='./midata/ori_annotations/', anodir2='./midata/temp_annotations/', pad='')
    brightness.brightness(imgdir1='./midata/temp/', imgdir2='./midata/cam/',
                          anodir1='./midata/temp_annotations/', anodir2='./midata/cam_annotations/', pad='_5')
    shutil.rmtree('./midata/temp_annotations')
    shutil.rmtree('./midata/temp')
    os.mkdir('./midata/temp_annotations')
    os.mkdir('./midata/temp')

    print('NTable-cam rotate & contrast 6')
    rotate.rotate(imgdir1='./midata/ori/', imgdir2='./midata/temp/',
                  anodir1='./midata/ori_annotations/', anodir2='./midata/temp_annotations/', pad='')
    contrast.contrast(imgdir1='./midata/temp/', imgdir2='./midata/cam/',
                      anodir1='./midata/temp_annotations/', anodir2='./midata/cam_annotations/', pad='_6')
    shutil.rmtree('./midata/temp_annotations')
    shutil.rmtree('./midata/temp')
    os.mkdir('./midata/temp_annotations')
    os.mkdir('./midata/temp')

    print('NTable-cam rotate & contrast & brightness 7')
    os.mkdir('./midata/temp2_annotations')
    os.mkdir('./midata/temp2')
    rotate.rotate(imgdir1='./midata/ori/', imgdir2='./midata/temp/',
                  anodir1='./midata/ori_annotations/', anodir2='./midata/temp_annotations/', pad='')
    contrast.contrast(imgdir1='./midata/temp/', imgdir2='./midata/temp2/',
                      anodir1='./midata/temp_annotations/', anodir2='./midata/temp2_annotations/', pad='')
    brightness.brightness(imgdir1='./midata/temp2/', imgdir2='./midata/cam/',
                          anodir1='./midata/temp2_annotations/', anodir2='./midata/cam_annotations/', pad='_7')
    shutil.rmtree('./midata/temp_annotations')
    shutil.rmtree('./midata/temp')
    shutil.rmtree('./midata/temp2_annotations')
    shutil.rmtree('./midata/temp2')

    print('augmentation end.')
    # now in cam & cam_annotations, every original image is augmented
    # into a group of eight, with subscripts from 0 to 7
    print('sampling begins')
    sampling.sampling()
    print('success.')


if __name__ == "__main__":
    # execute only if run as a script
    main()
