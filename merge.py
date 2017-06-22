# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:03:25 2017

@author: Administrator
"""
import os

def file_merge():
    """
    新建一个文件夹命名为file_merge，把所有txt文件放进去就ok啦！注意路径中‘/’，windows下路径不是这样。
    """
    #获取目标文件夹的路径
    filedir = os.getcwd()+'\\file_merge'
    #获取当前文件夹中的文件名称列表  
    filenames=os.listdir(filedir)
    #打开当前目录下的result.txt文件，如果没有则创建
    f=open('result.txt','w')
    #先遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
        #遍历单个文件，读取行数
        for line in open(filepath):
            f.writelines(line)
    #关闭文件
    f.close()

if __name__=="__main__":
    file_merge()
    
