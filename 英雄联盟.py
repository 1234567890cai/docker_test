""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/10/19 8:48
file :lx.PY
"""""
from selenium import  webdriver
import requests
import json ,csv
from lxml import html

# 得到所有的英雄
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=53'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'referer': 'https://lol.qq.com/'
}
resp = requests.get(url, headers=header)
a = resp.text
all = json.loads(a)
# print(all)  # 拿到网站所有英雄信息  第一步实现
# # 处理得到的数据
for item in  all['hero']:  # 字典取值           列表
    title = item['name']
    english = item['alias']
    id = item['title']
    print(title,id,english)  # 英文名字 中文名字  名字
    with open('img.csv','a+',newline='') as pic:
        a = csv.writer(pic)
        a.writerow([[title,english,id]])  # 数据写入csv

domin = 'https://lol.qq.com/'

url2 = 'https://lol.qq.com/main.shtml'
resp2 = requests.get(url2)
resp2.encoding='gbk'
# 使用selenium 的方法操作拿图片  不建议   用做测试
# print(resp2.text)
# htm = html.etree.HTML(resp2.text)
# hh = htm.xpath('//li[@class="champion-item"]/img/@scr')
# driber = webdriver.Chrome()
# driber.get(url2)
# new_img = driber.find_elements_by_xpath('//ul[@id="J_championItemContainer"]/li[@class="champion-item"]')
# new_url = 'https://game.gtimg.cn/images/lol/act/img/champion/Vladimir.png'
# domin = 'https://game.gtimg.cn/images/lol/act/img/champion/Singed.png'  # 目标url
# for i in new_img:
#     domin = 'https:'
#     ii = i.find_element_by_xpath('./li[@class="champion-item"]/img/@scr').text
#     new_url = f'{domin}'+ii
#     print(new_url)

