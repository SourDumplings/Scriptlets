'''
Author: SourDumplings
Date: 2021-08-22 21:31:15
Link: https://github.com/SourDumplings/
Email: changzheng300@foxmail.com
Description: 
'''

import os

def process_file(inputDir, inputFile, outputDir):
    fin = open(os.path.join(inputDir, inputFile), "r")
    fout = open(os.path.join(outputDir, inputFile), "w+")
    
    inputLines = fin.readlines()
    outputLines = ""
    if len(inputLines) > 2 and inputLines[0] == '/*' and lines[4] == '*/':
        outputLines = inputLines[5:]
    else:
        outputLines = inputLines
    
    fout.writelines(outputLines)


def process(inputDir, outputDir):
    fileOrDirs = os.listdir(inputDir)
    os.mkdir(outputDir)
    for fileOrDir in fileOrDirs:
        temp = os.path.join(inputDir, fileOrDir)
        if os.path.isdir(temp):
            process(temp, os.path.join(outputDir, fileOrDir))
        else:
            process_file(inputDir, fileOrDir, outputDir)


def main():
    inputPath = "./src"
    outputPath = "./srcOut"

    print("---------开始处理：%s ---------" % os.path.abspath(inputPath))
    process(inputPath, outputPath)
    print("---------处理完毕，输出路径为：%s ---------" % os.path.abspath(outputPath))


if __name__ == '__main__':
    main()