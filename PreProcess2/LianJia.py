import pandas as pd

if __name__ == '__main__':
    fileNameStr = 'lianjia2.csv'
    df = pd.read_csv(fileNameStr, encoding='utf-8', usecols=(0, 1, 2, 3, 4, 5, 6, 7))
    df.dropna(axis=0, how="any", inplace=True)
    total_price_mean = df['total_price'].mean()
    total_price_std = df['total_price'].std()
    print(total_price_mean - 3 * total_price_std, total_price_mean + 3 *
          total_price_std)
    index_list = df[df['total_price'] > total_price_mean + 3 * total_price_std].index.tolist()
    value_list = df[df['total_price'] > total_price_mean + 3 * total_price_std]
    print("there are {} items:".format(len(index_list)))
    print(index_list)
    print(value_list)
    value_list.to_csv("zz.csv", index=None)
