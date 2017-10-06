# encoding: utf-8
"""
@author: 酸饺子
@contact: changzheng300@foxmail.com
@license: Apache Licence
@file: bizhidownload.py
@time: 2017/8/31 14:40

从http://jj20.com/下载壁纸的爬虫
"""


import requests
import os


def main():
    url0 = 'http://jj20.com/d/cj001.php?p=/up/allimg/911/0GQ6122045/160GQ22045-'
    root = 'E:\\壁纸\\萌宠\\'
    n_ofpic = 8  # 图片集中图片张数
    params = '&w=1366&h=768'  # url额外参数，代表分辨率

    for each in range(n_ofpic):
        url = url0 + (str(each+1) + '.jpg')
        path = root + url.split('/')[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            # 修改headers
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=kv, params=params)
            # 以二进制格式存储图片
            with open(path, 'wb') as f:
                f.write(r.content)
                print('文件保存成功')
        else:
            print('文件已存在')
        url = url0


if __name__ == '__main__':
    main()