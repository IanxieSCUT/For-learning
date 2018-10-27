#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import requests
from urllib.request import urlretrieve
import os
import time
import re

def search(keyword,filepath,pagenumber):
    os.makedirs(filepath, exist_ok=True)#这里创建文件夹路径，exist_ok=True 指如果有就不创建
    params = {
        'tn':'baiduimage',
        'catename':'pcindexhot',
        'ipn':'r',
        'ct':201326592,
        'cl':2,
        'lm':-1,
        'st':-1,
        'fm':'result',
        'fr':'',
        'sf':1,
        'fmp':'1497491098685_R',
        'pv':'',
        'ic':0,
        'nc':1,
        'z':'',
        'se':1,
        'showtab':0,
        'fb':0,
        'width':'480',
        'height':'360',
        'face':0,
        'istype':2,
        'ie':'utf-8',
        'ctd':'1497491098685%5E00_1519X735',
        'word':keyword,
        'pn':pagenumber,
        'rn':20
    }
    #params['pn'] = '%d' % pagenumber 
    request(params,filepath)

def request(param,filepath):
    searchurl = 'http://image.baidu.com/search/flip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    response = requests.get(searchurl,params = param,headers=headers) #传入请求参数
    #pics_json = response.json()['imgs']
    response.encoding = 'utf-8'
    html=response.text
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    for i in range(0,len(pic_urls)):
        filename = keyword + str(time.strftime('%H%M%S'))+'.jpg'
        picsdownload(pic_urls[i], filename, filepath)

def picsdownload(url, filename, filepath):
    path = os.path.join(filepath, filename) #这里我们还是采用原来的图片
    try: #有些图片不知道为什么下载不了，所以这里用了try的方式
        urlretrieve(url, path)
        print('Downloading Images From ', url)
    except:
        print('Downloading None Images!')

if __name__ == '__main__':
    filepath = '/Users/ian_xie/Desktop/user_pics'
    keyword = '生活照'
    page = 15
    for i in range(1,page):
        pagenumber = i * 20
        search(keyword,filepath,pagenumber)