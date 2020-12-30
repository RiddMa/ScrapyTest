import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    d15_addr = 'G:/Courseware/Python/ScrapyTest/COVIDrequest/data/20201215-090001.csv'
    d15 = pd.read_csv(d15_addr)
    d15['Total Cases'] = d15['Total Cases'].str.replace(',', '').astype(int)
    d15 = d15[d15['#'].notna()]
    d15 = d15.sort_values(by='Total Cases', axis=0, ascending=[False])
    loc = d15['Country, Other'][0:20]
    data = pd.to_numeric(d15['Total Cases'][0:20])
    fig, ax = plt.subplots()
    x = np.arange(20) + 1
    plt.bar(x, data)
    plt.xticks(x, loc, rotation=45)
    ax.set_xlabel('Country/Region')
    ax.set_ylabel('Cases')
    for a, b in zip(x, data):
        plt.text(a, b + 1, '%d' % b, ha='center', va='bottom', fontsize=10)
    plt.show()


main()
