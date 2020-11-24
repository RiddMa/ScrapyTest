import time

import pandas as pd

# 1.打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr, encoding='utf-8')  # 不加dtype=str
df.drop(df.columns[[range(10, 13)]], axis=1, inplace=True)
df.drop(df.columns[[range(11, 15)]], axis=1, inplace=True)

df.dropna(axis=0, how='all', subset=['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'], inplace=True)

df.to_csv("beijing.csv")

# 4.计算平均值
start = time.time()
df['sum'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].sum(axis=1)
df['count'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].count(axis=1)
df['ave'] = round(df['sum'] / df['count'], 2)
end = time.time()

# 5.输出到文件
df.to_csv("beijing_ave.csv")

# 6.按照年做汇总，查看年的平均值
print(df[['month', 'year', 'TEMP', 'ave']].groupby("year").mean())
print(df[['month', 'year', 'TEMP', 'ave']].groupby('month').mean())
for y in range(2010, 2016):
    print("year:" + str(y) + "月平均pm和气温")
    print(df.query('year=={}'.format(y)).groupby('month').mean())
    print(df[['year', 'TEMP', 'month']].query('year=={}'.format(y)).groupby('month').mean())
