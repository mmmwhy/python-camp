#coding: utf-8
import re, os
from collections import Counter
# 目标文件所在目录
PATH = 'D:'
def getCounter(source):
    #输入一个英文的纯文本文件，统计其中的单词出现的个数
    with open(source) as f:
        data = f.read()
    data = data.lower()#字母全部小写
    datalist = re.split(r'[\s]+', data)#根据空白字符，将data进行划分
    return Counter(datalist)
def run(PATH):
    # 切换到目标文件所在目录
    os.chdir(PATH)
    # 遍历该目录下的txt文件
    total_counter = Counter() # 生成Counter()对象
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.txt':#分离扩展名
            total_counter += getCounter(i)# 多个Counter()叠加
    return total_counter.most_common()#Counter对象转化为list格式
if __name__ == '__main__':
    dic = run(PATH)
    for i  in range(len(dic)):
        print('%15s  ---->   %3s' % (dic[i][0],dic[i][1]))
