import re
data2D = []
while True:
    userInput = input('Input:') # 输入数组，用空格隔开即可
    info = re.split(r'[\D]',userInput)#正则表达式分割
    data = []# 定义一维数组
    try:
        for number in info:
            data+=[int(number)] # 一维数组加入数字
        data2D+=[data] #一维数组加入到二维中去
    except:
        break;
data2D
