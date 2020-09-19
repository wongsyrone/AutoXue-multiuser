#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project: AutoXue-multiuser
@file: updateTiku.py
@author: Yang
@contact: https://github.com/yangzuoming/AutoXue-multiuser
@time: 2020年9月7日
@Copyright © 2020. All rights reserved.
"""
from __future__ import unicode_literals

import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
from xuexi.model_local import TikuQuery


# from unit import cfg, logger


# 创建题库类
class Tiku:
    _fields = ['id', 'category', 'content', 'options', 'answer', 'excludes', 'description']

    def __init__(self):
        # self.url = cfg.get('api', 'url')
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

    # 获取网页数据
    def get_web_tiku(self, url, headers):
        rq = requests.get(url=url)
        if 200 == rq.status_code:
            print(f'GET item success')
            rq.encoding = 'utf-8'
            return rq
        else:
            print(f'GET item failure')
            return None

    # 获取单条数据
    def get_single_item(self):
        return
        # 插入json文件

    def insert_single_item(self, item):
        return True

    # 判断题录
    def istopic(self, tagstr):
        pattern = re.compile('^[0-9]、')
        print(pattern.search(tagstr))
        # if re.match(pattern, tagstr):
        #     return True
        # else:
        #     return False

    # 获取试题
    def get_tiku(self):
        # 打开题库文件
        out_file = open("./data1.json", "w", encoding='utf8')
        out_file.truncate()
        out_file.write("[\n")
        # 判断URL链接
        url = "https://github.com/ztianming/xuexi.cn"
        headers = self.headers
        # 获取整个数据
        html = self.get_web_tiku(url, headers)
        soup = BeautifulSoup(html.text, "lxml")
        articles = soup.article.find_all("p")
        # 清洗数据，只留下题目
        # 创建循环，逐条读出拆分条目，获取单条数据
        item_all = []
        item_tiku = {'category': "挑战题", 'content': "", 'options': "", 'answer': "", 'excludes': "", 'notes': ""}
        for tag in articles:
            # 判断是否为题目
            pattern = re.compile('^[1-9]\\d*、')
            if pattern.search(tag.contents[0]) is not None:
                # 插入题目
                # re.sub("\"", " ", item_tiku['content'])
                item_tiku['content'] = pattern.sub("", tag.contents[0].replace("_", "  "))  # 替换掉标题和下划线
                item_tiku['content'] = re.sub("\"", "", item_tiku['content'])
                item_tiku['content'] = re.sub("（ ）", "        ", item_tiku['content'])
                # print(item_tiku['content'] )
                answeroptions = []
            # 判断adcd选项
            pattern = re.compile('^[A-Z]、')
            if pattern.search(tag.contents[0]) is not None:
                #  插入选项
                strcontents = str(tag.contents[0])
                stranswer = strcontents[2:]
                answeroptions.append(stranswer)
            # 判断答案
            pattern = re.compile('^答案：')
            if pattern.search(tag.contents[0]) is not None:
                #  插入选项
                item_tiku['options'] = answeroptions
                #  插入答案
                strcontents = str(tag.contents[0])
                stranswer = strcontents[3:4]
                item_tiku['answer'] = stranswer
                # 提交题目到json
                # print(item_tiku)
                # item_all.append(item_tiku)
                json.dump(item_tiku, out_file, indent=6, ensure_ascii=False)
                out_file.write(",\n")

        # json.dump(item_all, out_file, indent=6, ensure_ascii=False)
        out_file.write("]\n")
        out_file.close()


if __name__ == "__main__":
    xuexitiaozhan = Tiku()
    xuexitiaozhan.get_tiku()
    # bq = TikuQuery()
    # bq.post("")
