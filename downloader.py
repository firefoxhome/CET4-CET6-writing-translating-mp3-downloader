#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 四级写作与翻译终极预测20篇 一键下载脚本
# author: pengwk
# email:  pengwk2@gmail.com
__author__ = 'pengwk'


import os

import requests

from bs4 import BeautifulSoup


def download_all():
    # 六级地址 "http://download.dogwood.com.cn/online/6jyc201/"
    base_url = "http://download.dogwood.com.cn/online/4jyc201/"

    index_page = requests.get(os.path.join(base_url, "index.html"))

    index_soup = BeautifulSoup(index_page.content, "html.parser")

    # mp3 only contains in li tags
    for li in index_soup.find_all("li"):
        href = li.a["href"]
        passage_name = li.a.span.text
        mp3_stream = requests.get(href)
        with open(passage_name + ".mp3", "wb") as fd:
            for chunk in mp3_stream.iter_content(chunk_size=128):
                fd.write(chunk)
        print passage_name
    return None

if __name__ == "__main__":
    download_all()
    print u"下载完成"
# change made from Ubuntu
