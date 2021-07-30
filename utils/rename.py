# -*- coding:utf8 -*-

import os


class BatchRename():
    """
    批量重命名文件夹中的图片文件

    """

    def __init__(self):
        self.path = '/home/zhuziyi/subject2020/sceneTable/dataset_augmented/annotation/contrast_brightness/'
        # 表示需要命名处理的文件夹

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)  # 获取文件夹内所有文件个数
        for item in filelist:
            if item.endswith('.txt'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), item[0:-4] + '_4.txt')
                # 处理后的格式也为jpg格式的，当然这里可以改成png格式 dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i),
                # '0>3s') + '.jpg')这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
                try:
                    os.rename(src, dst)
                    # print('converting %s to %s ...' % (src, dst))
                except:
                    continue
        print('total %d to rename' % total_num)


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
