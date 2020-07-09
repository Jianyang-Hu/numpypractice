# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/13 15:17
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : numpy_0413.py
# @Software: PyCharm
"""

    1. 爬取58同城的手机号类目下，所有帖子的标题和链接，存在数据库中
    2.设计爬取详细信息的爬虫2，将手机号卖家信息存入数据库
    3.使用技能：定位网页元素，存储数据库，读取数据库

"""

from bs4 import BeautifulSoup
import requests
import time
import pymongo

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

client = pymongo.MongoClient('localhost', 27017)
test_58 = client['test_58']
url_list_phone_number = test_58['url_list_phone_number']
item_info_phone_number = test_58['item_info_phone_number']
channel = 'http://www.chahaoyi.com/mobile/hangzhou_1515713.html'


# spider 1
def get_links_from(channel, pages):
    list_view = '{}pn{}/'.format(channel, str(pages))
    web_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    for link in soup.select('div.boxlist a.t'):
        item_link = link.get('href')
        item_title = link.strong.get_text()
        url_list_phone_number.insert_one({'title': item_title, 'url': item_link})


# spider 2
def get_item_info(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.title.text
    if title[0] != '1':
        pass
    else:
        phone_number = soup.title.text[0:10]
        # price = soup.select('span.price')
        area = soup.select('div.su_con > a')
        contact = soup.select('span.f20')
        seller = soup.select('ul > ul > li > a')[0].get_text()
        if area:
            area = soup.select('div.su_con > a')[0].get_text()
        else:
            pass
        if contact:
            contact = soup.select('span.f20')[0].get_text().strip()
        else:
            pass
        item_info_phone_number.insert_one({'title': title, 'contact': contact, 'area': area, 'seller': seller})


# 爬取20页在售手机号列表
for i in range(1, 20, 1):
    get_links_from(channel, i)
    print('Page ', i, ' has been crawled.')

# 爬取库中所有手机号的卖家信息
n = 0
for item in url_list_phone_number.find():
    get_item_info(item['url'])
    n += 1
    print('Item ', n, ' has been processed')
    time.sleep(1)
