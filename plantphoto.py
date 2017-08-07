# -*- coding:utf-8 -*-
import urllib.request
import datetime  
import os
import random
import re
import urllib
import time
from bs4 import BeautifulSoup
from urllib.error import URLError
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    req.add_header('Referer','http://www.85814.com/zhiwu/')
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

def get_soup(url):
    html=url_open(url)
    soup=BeautifulSoup(html,'html.parser')
    return soup 

def get_cat_url(url):#获取每类的地址
    soup=get_soup(url)
    site='http://www.85814.com'
    for each in soup.find(id='q').i.find_all('a'):
        dirname=each.string
        try:
            os.makedirs('F:\\images\\'+dirname)
        except FileExistsError as e:
            pass
        os.chdir('F:\\images\\'+dirname)
        cat_url=site+each['href']#每一类首页的地址
        all_urls=get_all_page_url(cat_url)#每一类每一页的地址
        for content_url in all_urls:
            get_imgs(content_url)
    os.chdir(os.pardir)    
def get_all_page_url(url):
    soup=get_soup(url)
    page_urls=[]
    page_urls.append(url)
    btn=soup.find('a',string=re.compile('尾页'))
    if btn is not None:
        page_num=btn['href'].split(sep='_')[1]#得到，例如：玫瑰花返回12
        for i in range(1,int(page_num)+1):
           page_urls.append(url+'_'+str(i)) 
    return page_urls
           
def get_imgs(url):#保存每一页的简介图片
    soup=get_soup(url)
    for content in soup.find(id='l').find_all('a'):
        #filename=content.img['alt']
        img=content.img['src']
        img=urllib.parse.quote(img,safe='/:?=&')
        img=url_open(img)
        with open('IMG_'+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+'.jpg','wb') as f:
            f.write(img)
            time.sleep(1)
'''
def get_content(url):#返回每一页的每张图片的详情地址，这个不好实现，弃了
    soup=get_soup(url)
    site='http://www.85814.com'
    contents=[]
    for content in soup.find(id='l').find_all('a'):
        contents.append(site+content['href'])
    return contents
''' 
  
def download():
    print("下载中...")
    site='http://www.85814.com/zhiwu/'
    get_cat_url(site)
    print("下载完成^-^")
    
if __name__=='__main__':
    download()
    
