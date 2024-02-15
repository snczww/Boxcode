#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Victor
@software: PyCharm
@file: mergeip.py
@time: 2024/2/15 13:48
"""
import json
channel_mapping = {
    "CCTV-1": "CCTV-1 综合",
    "CCTV-2": "CCTV-2 财经",
    "CCTV-3": "CCTV-3 综艺",
    "CCTV-4": "CCTV-4 中文国际",
    "CCTV-5": "CCTV-5 体育",
    "CCTV-5+": "CCTV-5+ 体育赛事",
    "CCTV-6": "CCTV-6 电影",
    "CCTV-7": "CCTV-7 国防军事",
    "CCTV-8": "CCTV-8 电视剧",
    "CCTV-9": "CCTV-9 纪录",
    "CCTV-10": "CCTV-10 科教",
    "CCTV-11": "CCTV-11 戏曲",
    "CCTV-12": "CCTV-12 社会与法",
    "CCTV-13": "CCTV-13 新闻",
    "CCTV-14": "CCTV-14 少儿",
    "CCTV-15": "CCTV-15 音乐",
    "CCTV-16": "CCTV-16 奥林匹克",
    "CCTV-17": "CCTV-17 农业农村",
    "CCTV-4K": "CCTV-4K 超高清",
    "CCTV-8K": "CCTV-8K 超高清",
    "CCTV1": "CCTV-1 综合",
    "CCTV2": "CCTV-2 财经",
    "CCTV3": "CCTV-3 综艺",
    "CCTV4": "CCTV-4 中文国际",
    "CCTV5": "CCTV-5+ 体育赛事",
    "CCTV6": "CCTV-6 电影",
    "CCTV7": "CCTV-7 国防军事",
    "CCTV8": "CCTV-8 电视剧",
    "CCTV9": "CCTV-9 纪录",
    "CCTV10": "CCTV-10 科教",
    "CCTV11": "CCTV-11 戏曲",
    "CCTV12": "CCTV-12 社会与法",
    "CCTV13": "CCTV-13 新闻",
    "CCTV14": "CCTV-14 少儿",
    "CCTV15": "CCTV-15 音乐",
    "CCTV16": "CCTV-16 奥林匹克",
    "CCTV17": "CCTV-17 农业农村",
    "CCTV4K": "CCTV-4K 超高清",
    "CCTV8K": "CCTV-8K 超高清"
}

# with open('channel_mapping.json', 'r') as json_file:
#     channel_mapping = json.load(json_file)
channels = {}


with open('output/ip6live.txt', 'r') as file:
    for line in file:
        if '#genre#'  in line:
            continue
        channel, urls = line.strip().split(',', 1)  # Split only once to separate channel from URLs
        # print(channel, urls)
        # print(channel.strip())
        channel = channel_mapping.get(channel.strip(), channel.strip())
        urls = urls.split(',')  # Split URLs by comma

        if  channel not in channels :
            channels[channel] = []
        channels[channel].extend(urls)  # Extend the list with URLs



# # Writing merged channels to a file
with open('output/ip6live.txt', 'w') as output_file:
    for channel, urls in channels.items():
        for url in urls:
            # print(f"{channel}, {url}\n")
            output_file.write(f"{channel}, {url}\n")

