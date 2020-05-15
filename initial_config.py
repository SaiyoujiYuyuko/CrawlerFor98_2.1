# -*- coding: utf-8 -*-
import configparser
import os
def inic():
    cf = configparser.ConfigParser()
    cf['数据存放文件夹'] = {
        'root': r'./98_Data/',
        'imgdir': r'./98_Data/Img/',
        'csvdir': r'./98_Data/Csv_data/',
        'posterdir': r'./98_Data/Img/Poster/',
        'scshotdir': r'./98_Data/Img/ScreenShot/',
        'date_txt': r'./98_Data/result.txt'
    }
    cf['线程数'] = {
        '图片下载线程': '2',
        '目录爬取线程': '3',
        '爬虫线程': '15'
    }
    cf['爬取设置'] = {
        '开始页面(最小为1)': '1',
        '结束页面': '10',
        '是否下载图片': '是',
        '是否增量下载': '是',
        '是否第一次使用': '否'
    }
    cf['98最新网址'] = {
        '首页网址': 'https://www.98ddt.xyz/forum.php'
    }
    f = open('config.ini', 'w', encoding='utf-8')
    cf.write(f)
    f.close()
if __name__=="__main__":
    inic()
