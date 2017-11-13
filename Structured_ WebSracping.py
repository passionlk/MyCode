#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:37:55 2017

@author: passionlk
"""

from urllib import request
from bs4 import BeautifulSoup
 
if __name__ == '__main__':
    # 第8章的网址
    url = 'http://www.136book.com/huaqiangu/ebxeew/'
    head = {}
    # 使用代理
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    # 创建request对象
    soup = BeautifulSoup(html, 'lxml')
    # 找出div中的内容
    soup_text = soup.find('div', id = 'content')
    # 输出其中的文本
    print(soup_text.text)
    


from urllib import request
from bs4 import BeautifulSoup
 
if __name__ == '__main__':
    # 目录页
    url = 'http://www.136book.com/huaqiangu/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    # 解析目录页
    soup = BeautifulSoup(html, 'lxml')
    # find_next找到第二个<div>
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    # 遍历ol的子节点，打印出章节标题和对应的链接地址
    for link in soup_texts.ol.children:
        if link != '\n':
            print(link.text + ':  ', link.a.get('href'))
            
            
from urllib import request
from bs4 import BeautifulSoup
 
if __name__ == '__main__':
    url = 'http://www.136book.com/huaqiangu/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    # 打开文件
    f = open('/Users/passionlk/Desktop/huaqiangu.txt','w')
    # 循环解析链接地址
    for link in soup_texts.ol.children:
        if link != '\n':
            download_url = link.a.get('href')
            download_req = request.Request(download_url, headers = head)
            download_response = request.urlopen(download_req)
            download_html = download_response.read()
            download_soup = BeautifulSoup(download_html, 'lxml')
            download_soup_texts = download_soup.find('div', id = 'content')
            # 抓取其中文本
            download_soup_texts = download_soup_texts.text
            # 写入章节标题
            f.write(link.text + '\n\n')
            # 写入章节内容
            f.write(download_soup_texts)
            f.write('\n\n')
    f.close()
            
            
