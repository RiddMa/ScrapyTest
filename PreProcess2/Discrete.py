import pandas as pd

if __name__ == '__main__':
    fileNameStr = 'lianjia2.csv'
    df = pd.read_csv(fileNameStr, encoding='utf-8', usecols=(0, 1, 2, 3, 4, 5, 6, 7))
    df.dropna(axis=0, how="any", inplace=True)
    sections = [0, 40000, 50000, 60000, 80000, 140000]
    section_names = ["0-40000", "40001-50000", "50000-60000", "60001-80000", "80001-140000"]
    result = pd.cut(df['unit_price'], sections, labels=section_names)
    print("房屋数量")
    print(pd.value_counts(result))
    print("\n房屋比例")
    print(pd.value_counts(result, normalize=True))