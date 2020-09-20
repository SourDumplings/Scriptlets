# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 11:56
# @Author  : SourDumplings
# @Email   : changzheng300@foxmail.com
# @Link    : https://github.com/SourDumplings/
# @Site    : 
# @File    : watermarker.py

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))  # 宋体


def create_watermark(content, temp_pdf_file):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    c = canvas.Canvas(temp_pdf_file, pagesize=(30 * cm, 30 * cm))
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate(0, 0)

    # 设置字体
    c.setFont("song", 30)
    # 指定描边的颜色
    c.setStrokeColorRGB(0, 1, 0)
    # 指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    # 旋转30度,坐标系被旋转
    c.rotate(-30)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0, 0.1)
    # 设置透明度,1为不透明
    # c.setFillAlpha(0.1)
    c.setFillAlpha(0.4)
    # 画几个文本,注意坐标系旋转的影响
    for dr in range(-100, 100, 18):
        for dc in range(-100, 100, 3):
            c.drawString(dr * cm, dc * cm, content)
    # 关闭并保存pdf文件
    c.save()


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


if __name__ == '__main__':
    base_path = "C:\\Users\\sourd\\备份数据\\jobs\\各种材料\\浙商银行"
    pdf_file_in = base_path + "\\1.pdf"
    pdf_file_out = base_path + "\\2.pdf"
    temp_pdf_file = base_path + "\\mark.pdf"
    create_watermark('仅供浙商银行应聘使用，它用无效！', temp_pdf_file)
    add_watermark(pdf_file_in, temp_pdf_file, pdf_file_out)
