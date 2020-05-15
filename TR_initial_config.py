# -*- coding: utf-8 -*-
import configparser
import os
def inic():
    cf = configparser.ConfigParser()
    cf['路径设置'] = {
        '待处理文件路径(逗号隔开)': ''
    }
    cf['程序设置'] = {
        '是否考虑以前汉化标识': '是',
        '程序使用数据库路径':r'./98_Data/Csv_data/98CTest.csv',
        '是否更改上一层文件目录名字(需要保证一个文件夹下一个视频)':'否'
    }
    f = open('TR_config.ini', 'w', encoding='utf-8')
    cf.write(f)
    f.close()
if __name__=="__main__":
    inic()
