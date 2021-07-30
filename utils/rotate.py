# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import os
import random
import math
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def rotateAndScale(center, points, k, d_theta):
    """
        center: (x, y), center of rotation
        points: [(x1, y1), ...], points that need to be calculated
        k: factor of scaling
        d_theta: delta angles of rotation (in angle), clockwise: -, anti-clockwise: +
    """
    # r_theta = (d_theta % 360) / 360.0 * (2 * np.pi)
    points = np.array(points, dtype=np.float32)  # k x 2
    center = np.array(center, dtype=np.float32)
    # print(points)
    # print(center)

    # polar
    vec = points - center
    vec[:, 1] *= -1
    flag = np.clip(vec[:, 0] / np.abs(vec[:, 0] + 1e-7), a_min=None, a_max=0)
    rho = np.sqrt(np.sum(vec * vec, axis=1))
    theta = np.arctan(vec[:, 1] / (vec[:, 0] + 1e-7)) + np.pi * flag

    # rotate and scaling
    rho *= k
    theta += d_theta

    # rectangle
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x = rho * cos_theta
    y = rho * sin_theta * -1
    res = np.stack([x, y], axis=1) + center
    res = res.tolist()
    return res


def rotate_single(name, imgdir1='./midata/ori/', imgdir2='./midata/cam/',
                  anodir1='./midata/ori_annotations/', anodir2='./midata/cam_annotations/',
                  pad='_1'):
    """旋转会改变annotation"""
    img = Image.open(imgdir1 + name)
    w0, h0 = img.size
    h = max(w0, h0)
    w = min(w0, h0)
    gate = random.random()
    if gate > 0.5:
        degree = random.randint(1, 5)
    else:
        degree = -random.randint(1, 5)
    im2 = img.rotate(degree, expand=1)
    img2 = cv2.cvtColor(np.array(im2), cv2.COLOR_RGBA2BGRA)

    # 转为弧度值, 计算扩大的倍数k
    degree = degree * math.pi / 180
    a = math.atan(w / h)
    b = math.pi / 2 - degree / 2 - a
    c = math.sqrt((w / 2) * (w / 2) + (h / 2) * (h / 2))
    d = math.sqrt(c * c * 2 - 2 * c * c * math.cos(degree))
    e = math.sin(b) * d
    k = (e + w / 2) / (w / 2)

    y, x = img2.shape[0:2]
    img2 = cv2.resize(img2, (int(x * k), int(y * k)))
    y, x = img2.shape[0:2]
    new_img = img2[int(y / 2 - h0 / 2):int(y / 2 + h0 / 2), int(x / 2 - w0 / 2):int(x / 2 + w0 / 2)]

    # 要传递的参数：(x/2, y/2), k, degree(弧度值), 原始的四点坐标
    with open(anodir1 + name[0:-4] + '.txt', "r") as f:
        for line in f.readlines():
            point = line.strip('\n').split(' ')  # 去掉列表中每一个元素的换行符, 分开成list
            point = [float(i) for i in point]
            center_x = w0 * point[1]
            center_y = h0 * point[2]
            ww = w0 * point[3]
            hh = h0 * point[4]
            x1 = center_x - ww / 2
            y1 = center_y - hh / 2
            x2 = center_x + ww / 2
            y2 = center_y - hh / 2
            x3 = center_x - ww / 2
            y3 = center_y + hh / 2
            x4 = center_x + ww / 2
            y4 = center_y + hh / 2
            # print(name, degree)
            points = rotateAndScale((w0 / 2, h0 / 2), [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], k, degree)
            # npoints = np.reshape(np.array(points).astype(np.int32), (-1, 2))
            # draw_img = cv2.polylines(new_img, [npoints], True, (255, 0, 0), 2)
            # cv2.imwrite(poly_dir + name, draw_img)

            max_x = min(max(x[0] for x in points), w0)
            max_y = min(max(x[1] for x in points), h0)
            min_x = max(min(x[0] for x in points), 0)
            min_y = max(min(x[1] for x in points), 0)

            final = ['0', (max_x + min_x) / 2 / w0, (max_y + min_y) / 2 / h0, (max_x - min_x) / w0,
                     (max_y - min_y) / h0]
            final = [str(i) for i in final]
            ff = open(anodir2 + name[0:-4] + pad + '.txt', "a")
            ff.write(" ".join(final))
            ff.write('\r\n')
    return new_img


def rotate(imgdir1='./midata/ori/', imgdir2='./midata/cam/',
           anodir1='./midata/ori_annotations/', anodir2='./midata/cam_annotations/',
           pad='_1'):
    img_list = os.listdir(imgdir1)
    for i in range(len(img_list)):
        img = rotate_single(img_list[i], anodir1=anodir1, anodir2=anodir2, pad=pad)
        cv2.imwrite(imgdir2 + img_list[i][0:-4] + pad + '.jpg', img)


def main():
    rotate()


if __name__ == '__main__':
    main()
