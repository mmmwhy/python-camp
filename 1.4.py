# coding=utf-8
from collections import defaultdict
import re
# 替换除了n't这类连字符外的所有非单词字符和数字字符
def replace(s):
    if s.group(1) == 'n\'t':
        return s.group(1)
    return ' '
def cal(filename='203305485.txt'):
    # 使用lambda来定义简单的函数
    dic = defaultdict(lambda: 0)#dic = defaultdict(int)也可以
    with open(filename, 'r') as f:
        data = f.read()
    # 全部变为小写字母
    data = data.lower()
    # 替换除了n't这类连字符外的所有非单词字符和数字字符
    data = re.sub(r'(n[\']t)|([\W\d])', replace, data)
    datalist = re.split(r'[\s\n]+', data)
    for item in datalist:
        dic[item] += 1
    del dic['']
    return dic
if __name__ == '__main__':
    dic = cal()
    for key, val in dic.items():
        print('%15s  ---->   %3s' % (key,val))
