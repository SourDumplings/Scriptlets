# encoding: utf-8
"""
@author: 酸饺子
@contact: changzheng300@foxmail.com
@license: Apache Licence
@file: downloadcatpic.py
@time: 2017/7/19 21:05

从小猫的图片网上下载小猫的图片集
"""


import urllib.request as u
import easygui as g
import os
import time


def main(path):
    size = [500, 600]
    for size[0] in range(500, 2001):
        for size[1] in range(600, 2001):
            file_name = os.path.join(path, 'cat_%d_%d.jpg' % (int(size[0]), int(size[1])))

            req = u.Request('http://placekitten.com/%d/%d' % (int(size[0]), int(size[1])))
            response = u.urlopen(req)
            cat_img = response.read()

            with open(file_name, 'wb') as f:
                f.write(cat_img)

            time.sleep(2)


if __name__ == '__main__':
    path = g.diropenbox(msg='请选择存放喵的文件夹')
    main(path)
