#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 00:14:48 2017

@author: passionlk
"""


import json

path = '/Users/passionlk/Documents/MSBA/MyCode/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line.strip()) for line in open(path, encoding="utf-8")]      #将JSON字符串转换成Python 字典对象,注意，此处txt文件中含有非ASCII字符，所以要设置encoding=utf-8
records[0]
records[0]['tz']
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

#使用标准Python 库，在遍历失去的过程中计数
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts



#使用Python标准库 
from collections import defaultdict
from collections import Counter

def get_counts2(sequence):
    counts = defaultdict(int) #所有的值均会被初始化为0
    for x in sequence:
        counts[x] += 1
    return counts 

counts = get_counts(time_zones)
counts['America/New_York']
len(time_zones)


counts = Counter(time_zones)
counts.most_common(10)

from pandas import DataFrame, Series 
import numpy as np; import pandas as pd

frame = DataFrame(records)
frame
frame['tz'][:10]



































































