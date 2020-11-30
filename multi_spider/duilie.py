#-*- codeing = utf-8 -*-
#@Time : 2020/11/27/0027 21:26
#@Author : LUyc
#@File : duilie.py
#@Software : PyCharm
import random

import Multi_threading as mth
import queue
import threading
import time


#test queue
# q=queue.Queue()
#
# for i in range(5):
#     q.put(i)
# for i in range(5):
#     aaaa=q.get()
#     print(f'拿出了：{aaaa},还剩：{q.qsize()}个')
#     print(f'队列中是不是没有数据{q.empty()}')


def get_text(url_queue:queue.Queue,html_queue:queue.Queue):
    '''获取网页内容'''
    while True:
        url=url_queue.get()
        text=mth.spider(url)
        html_queue.put(text)
        print(f'当前线程号为{threading.current_thread().name},当前爬取页数为：{url[-1]},url队列中还有：{url_queue.qsize()}')
        time.sleep(random.randint(1,2))


def get_parse(html_queue:queue.Queue,file):
    '''解析获取到的内容，并放到文件里'''
    while True:
        html=html_queue.get()
        parse_text=mth.data_parse(html)
        for i in parse_text:
            file.write(str(i)+'\n')
        print(f'当前线程号为{threading.current_thread().name},html队列中还有：{url_queue.qsize()}')
        time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    url_queue=queue.Queue()
    html_queue=queue.Queue()
    for i in mth.urls:
        url_queue.put(i)

    for thread in range(3):
        t=threading.Thread(target=get_text,name=f'huoqu-{thread}',args=(url_queue,html_queue))
        t.start()


    f=open('data1.txt','w',encoding='utf-8')


    for thread in range(2):
        t=threading.Thread(target=get_parse,name=f'jiexi-{thread}',args=(html_queue,f))
        t.start()



