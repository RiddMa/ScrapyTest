import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.figure(figsize=(6,9)) #调节图形大小
labels = ['XL','L','M','S'] #定义标签
sizes = [461,253,789,660] #每块值
colors = ['red','yellowgreen','cyan','yellow'] #每块颜色定义
explode = (0,0,0,0.1) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
for t in text1:
    t.set_size(20)
plt.title('服装设计',fontsize=30)
plt.axis('equal')
plt.show()
