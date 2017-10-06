#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 22:09:50
# @Author  : 酸饺子 (changzheng300@foxmail.com)
# @Link    : http://bbs.fishc.com/space-uid-437297.html
# @Version : $Id$

import os

path = 'E:\\小甲鱼—《零基础入门学习Python》'


def re_name(path):
    os.chdir(path)
    file_list = os.listdir(os.curdir)
    for each_file in file_list:
        if os.path.isdir(each_file):
            re_name(os.path.join(path, each_file))
            os.chdir(os.pardir)
        elif os.path.splitext(each_file)[1] == '.py':
            old_name = each_file
            new_name = os.path.splitext(each_file)[0].replace('.', '') + '.py'
            os.rename(old_name, new_name)


re_name(path)




