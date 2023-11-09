#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Victor
@software: PyCharm
@file: iptv.py
@time: 2023/4/27 12:43
"""
import requests

url = 'https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u'
response = requests.get(url)
data = response.text
url_txt_1='https://raw.githubusercontent.com/Dong-learn9/TVBox-zyjk/main/TV/tvlive.txt'
url_txt_2='https://gitcode.net/qq523082028/zb/-/raw/master/ZB.txt'
url_txt_lists=[url_txt_1,url_txt_2]

lines = data.split('\n')

group_dict = {}

def txt_r(txt_url):
    response_txt = requests.get(txt_url)
    data_txt = response_txt.text
    return data_txt

with open('output/ip6live.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if line.startswith('#EXTINF:'):
            info = line.split(',')
            group_title = info[0].split('"')[-2]
            name = info[1]
        elif line and not line.startswith('#'):
            if group_title not in group_dict:
                group_dict[group_title] = []
            group_dict[group_title].append({'name': name, 'url': line})

    for group, channels in group_dict.items():
        f.write(group + ', #genre#\n')
        for channel in channels:
            f.write(f"{channel['name']},{channel['url']}\n")
        f.write('\n')
    for url_txt_s in url_txt_lists:
        txt_data=txt_r(url_txt_s)
        f.write(txt_data)

