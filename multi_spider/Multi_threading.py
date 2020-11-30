#-*- codeing = utf-8 -*-
#@Time : 2020/11/27/0027 18:45
#@Author : LUyc
#@File : Multi_threading.py
#@Software : PyCharm
import re
import threading
import time

import requests
import bs4

urls=[
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1,10)
     ]

def spider(url):
    '''爬取目标网址'''
    text=requests.get(url).text
    # text_len=len(text)
    # print(url,text_len)
    return text


def data_parse(text):
    '''通过正则解析到有用的数据'''
    jiexi=re.compile('<a class="post-item-title" href=.*? target="_blank">(.*?)</a>')
    data=jiexi.findall(text)
    return data


thread_list=[]
def multi_spider(urls):
    '''简易多线程爬虫'''
    for i in urls:
        thread_list.append(
            threading.Thread(target=spider,args=(i,))
                        )

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


if __name__ == '__main__':
    # start=time.time()
    # multi_spider(urls)
    # end=time.time()
    # print('爬取成功，使用时间%0.2f秒'%(end-start))
    # print(round((end - start),2))


    a=spider(urls[0])

    b=data_parse(a)

    print(b)


















