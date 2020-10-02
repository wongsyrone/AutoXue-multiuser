#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project: AutoXue-multiuser
@file: __main__.py
@time: 2020年9月29日10:55:28
@Copyright © 2020. All rights reserved.
"""
import json
import requests
from xuexi.unit import cfg, logger
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Bank(Structure):
    _fields = ['id', 'category', 'content', 'options', 'answer', 'excludes', 'description']

    def __repr__(self):
        return f'{self.content}'

    def to_json(self):
        pass

    @classmethod
    def from_json(self, data):
        pass


class TikuQuery:
    def __init__(self):
        self.dataKu = cfg.get('api', 'datajson')
        with open(self.dataKu, 'r', encoding='utf8') as f:
            self.dataKu = json.load(f)

        with open('./data_back.json', 'r', encoding='utf8') as f:
            self.dataKu_test = json.load(f)

    def post(self, contentstr, options):

        logger.info("开始比较题库")
        for dataKuItem in self.dataKu:
            # if dataKuItem['content'] == contentstr:
            ratioscore = fuzz.ratio(dataKuItem['content'], contentstr)
            if ratioscore > 60:
                # logger.info(dataKuItem['content'] + "  比较  " + contentstr + "得分：")
                if options == dataKuItem['options']:
                    logger.info(f"匹配到题目，得分：{ratioscore}")
                    return dataKuItem['answer']
                elif fuzz.ratio(options, dataKuItem['options']) > 65:
                    logger.info(f"匹配到题目，得分：{ratioscore}")
                    logger.info(fuzz.ratio(options, dataKuItem['options']))
                    return dataKuItem['answer']

            else:
                continue

    def post_2(self, item):
        # logger.debug(f'POST {item["content"]} {item["options"]} {item["answer"]} {item["excludes"]}...')
        if "" == item["content"]:
            logger.debug(f'content is empty')
            return None
        logger.debug(f'GET {item["content"]}...')
        for dataKuItem_test in self.dataKu_test:
            if dataKuItem_test['category'] == item["category"] and dataKuItem_test['content'] == item["content"] and \
                    dataKuItem_test[
                        'options'] == item["options"]:
                return dataKuItem_test
            else:
                continue
        for dataKuItem in self.dataKu:
            if dataKuItem['category'] == item["category"] and fuzz.ratio(dataKuItem['content'],
                                                                         item["content"]) > 60 and fuzz.ratio(
                dataKuItem['options'], item["options"]) > 65:
                return dataKuItem
            else:
                continue
        return None

    def post_1(self, item):
        # logger.debug(f'POST {item["content"]} {item["options"]} {item["answer"]} {item["excludes"]}...')
        if "" == item["content"]:
            logger.debug(f'content is empty')
            return None
        logger.debug(f'GET {item["content"]}...')
        for dataKuItem in self.dataKu_test:
            if dataKuItem['category'] == item["category"] and dataKuItem['content'] == item["content"] and dataKuItem[
                'options'] == item["options"]:
                return dataKuItem
            else:
                continue
        return None

    def put(self, item):
        if "" == item["content"]:
            logger.debug(f'content is empty')
            return False
        logger.debug(f'PUT {item["content"]} {item["options"]} {item["answer"]} {item["excludes"]}...')
        try:
            out_file = open("./data_back.json", "w", encoding='utf8')
            self.dataKu_test.append(item)
            json.dump(self.dataKu_test, out_file, indent=6, ensure_ascii=False)
            out_file.close()
            return True
        except Exception as ex:
            logger.info(ex)
            return False

    def get(self, item):

        if "" == item["content"]:
            logger.debug(f'content is empty')
            return False
            # logger.debug(f'POST {item["content"]} {item["options"]} {item["answer"]} {item["excludes"]}...')
        if "" == item["content"]:
            logger.debug(f'content is empty')
            return None
        logger.debug(f'GET {item["content"]}...')
        for dataKuItem in self.dataKu_test:
            if dataKuItem['category'] == item["category"] and dataKuItem['content'] == item["content"] and dataKuItem[
                'options'] == item["options"]:
                return dataKuItem['answer']
            else:
                continue
        return None
