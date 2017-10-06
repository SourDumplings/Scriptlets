# encoding: utf-8
"""
@author: 酸饺子
@contact: changzheng300@foxmail.com
@license: Apache Licence
@file: spectrumplot.py
@time: 2017/7/27 18:01

根据已有数据绘制出简单谱线
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd


def main():
    # 数据单位
    global unit
    unit = 'dBm'

    # 读取文件数据函数
    def read_data(data_path, file_type, source_filename, normalize):

        # 打开数据目录
        file_list = os.listdir(data_path)
        # 存放正式数据名的列表
        name_list = []

        # 根据数据文件类型选择适当的读取函数并读取出数据
        # csv文件
        if file_type == '.csv':
            # 读取光源数据
            source = pd.read_csv(os.path.join(data_path, source_filename),  # 文件路径
                                 names=['Wavelength/nm', 'Source'],  # 列名
                                 delimiter=';',  # 列分隔符
                                 skiprows=76,  # 忽略前76行
                                 skipfooter=1,  # 忽略倒数第一行
                                 # index_col='Wavelength/nm' # 指定波长为行索引
                                 )
            original_data = source.copy()
            # 读取正式数据
            for each_file in file_list:
                if os.path.splitext(each_file)[1] == file_type:
                    each_name = os.path.splitext(each_file)[0]
                    # 跳过已经读取过的光源文件
                    if each_file == source_filename:
                        continue
                    else:
                        name_list.append(each_name)
                        each_data = pd.read_csv(os.path.join(data_path, each_file),  # 文件路径
                                                names=['Wavelength/nm', each_name],  # 以各文件名作为列名
                                                delimiter=';',  # 列分隔符
                                                skiprows=76,  # 忽略前76行
                                                skipfooter=1,  # 忽略倒数第一行
                                                # index_col='Wavelength/nm' # 指定波长为行索引
                                                )
                        original_data = pd.concat([original_data, each_data[each_name]],
                                                  axis=1)  # 将数据作为新列插入到original_data中
        # txt文件
        elif file_type == '.txt':
            source_path = open(os.path.join(data_path, source_filename))
            # 读取光源数据
            source = pd.read_table(source_path,  # 文件路径
                                   names=['Wavelength/nm', 'Source'],  # 列名
                                   delimiter=' ',  # 列分隔符
                                   skipinitialspace=True,  # 忽略列分隔符之后的空格
                                   # skiprows=76,  # 忽略前76行
                                   # skipfooter=1,  # 忽略倒数第一行
                                   # index_col='Wavelength/nm' # 指定波长为行索引
                                   )
            original_data = source.copy()
            # 读取正式数据
            for each_file in file_list:
                if os.path.splitext(each_file)[1] == file_type:
                    each_name = os.path.splitext(each_file)[0]
                    # 跳过已经读取过的光源文件
                    if each_file == source_filename:
                        continue
                    else:
                        name_list.append(each_name)
                        nonsource_data_path = open(os.path.join(data_path, each_file))
                        each_data = pd.read_table(nonsource_data_path,  # 文件路径
                                                  names=['Wavelength/nm', each_name],  # 以各文件名作为列名
                                                  delimiter=' ',  # 列分隔符
                                                  skipinitialspace=True,  # 忽略列分隔符之后的空格
                                                  # skiprows=76,  # 忽略前76行
                                                  # skipfooter=1,  # 忽略倒数第一行
                                                  # index_col='Wavelength/nm' # 指定波长为行索引
                                                  )
                        original_data = pd.concat([original_data, each_data[each_name]],
                                                  axis=1)  # 将数据作为新列插入到original_data中
        # excel文件
        elif file_type == '.xls':
            pass

        # 选择需要返回的数据是否经过了归一化
        if normalize:
            # 将数据归一化
            normalized_data = pd.DataFrame(original_data['Wavelength/nm'])
            # print(normalized_data)
            for each_column in name_list:
                normalized_data[each_column] = original_data[each_column] - original_data['Source'] + 3  # 相对于光源做归一化
            data = normalized_data  # 返回归一化数据
            global unit
            unit = 'dB'
        else:
            data = original_data  # 返回原始数据

        # 设置波长为行索引
        data = data.set_index('Wavelength/nm')
        return data

    # 数据目录，目录中需包含光源数据
    data_path = r'E:\Research\SOI with chalcogenide cladding\1550\20170428 wg+spiral+ring+slot\20170708 对光测试空气上包层结构\spiralforproploss_aircld'
    source_filename = 'source_2nm.txt'  # 光源数据文件名
    # 数据文件类型
    file_type = '.txt'
    # 读取数据
    data = read_data(data_path, file_type, source_filename, normalize=1)

    # 画出谱线

    # 用pandas库画图，图较简单
    # print(data)
    data.plot(title='spiralforproploss_1550nm',  # 图标题
              xlim=(1520, 1610),  # 横坐标范围
              ylim=(-60, -15),  # 纵坐标范围
              # style='k--' # 曲线类型
              )

    # 用plt画图，可以对每条曲线分别编辑等对图进行更多地编辑
    # wavelength = data.index
    # data1 = data['1'].values
    # data2 = data['2'].values
    # plt.figure()
    # plt.plot(wavelength, data1, 'k--', label='1')
    # # plt.figure()
    # plt.plot(wavelength, data2, 'y-.', label='2')

    plt.ylabel('T/' + unit)  # 纵坐标标注
    plt.show()


if __name__ == '__main__':
    main()
