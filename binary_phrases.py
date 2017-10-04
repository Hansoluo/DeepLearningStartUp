# coding:utf-8
# 打开并读取txt文件
# 对文本进行清洗，去掉多余的字符'― ―'（采用re）
# 按照中文符号分割文本
# 按照空格分割单个文本
# 将单个文本连接起来，组成二元词组，并保存到列表单中
# 统计列表中相同二元词组出现的频率
# 输出频率最高的前 10 个「二元词组」

import os
import re
from collections import Counter
from zhon.hanzi import punctuation

basedir = os.path.abspath(os.path.dirname(__file__))
file_dir = os.path.join(basedir, 'happiness_seg.txt')
with open(file_dir, 'r', encoding = 'utf8') as f:
    text = f.read()
line1 = re.sub('― ―', '', text)
line2 = re.split(r'[{}]'.format(punctuation), line1)
a = []
for item in line2:
    phrases = item.split()
    for i in range(len(phrases)-1):
        binary_phrases = phrases[i] + " " + phrases[i+1]
        a.append(binary_phrases)

print(Counter(a).most_common(10))

# 错误的方法——re方法，没办法把"今天 天气 不错"分割成两个二元词组
# words = re.findall(r'\w+\s\w+', open(file_dir, 'r', encoding = 'utf8').read())
# print(Counter(words).most_common(10))
