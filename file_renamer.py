#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 22:09:50
# @Author  : 酸饺子 (changzheng300@foxmail.com)
# @Link    : http://bbs.fishc.com/space-uid-437297.html
# @Version : $Id$

import os

path = 'E:\\程序代码\\数据结构-浙江大学-陈越、何钦铭\\课程示例代码\\'


def re_name(path):
    os.chdir(path)
    file_list = os.listdir(os.curdir)
    for each_file in file_list:
        if os.path.isdir(each_file):
            re_name(os.path.join(path, each_file))
            os.chdir(os.pardir)
        elif os.path.splitext(each_file)[1] == '.c':
            old_name = each_file
            new_name = os.path.splitext(each_file)[0].replace('.', '') + '.h'
            os.rename(old_name, new_name)


re_name(path)


