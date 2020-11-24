import pandas as pd

# open file
FileNameStr = './pm25-data-for-five-chinese-cities/BeijingPM20100101_20151231.csv'
df = pd.read_csv(FileNameStr, encoding='utf-8', usecols=[1, 2, 6, 7, 8, 9])

# create avg row
# mean(axis=1) to get avg row
df['PM_avg'] = df.iloc[:, 2:6].mean(axis=1)
# group by year, calculate average of PM. output to file
df.groupby(['year', 'month'])['PM_avg'].mean().to_csv("month_avg.csv")
# output to console
print(df.groupby(['year', 'month'])['PM_avg'].mean())
