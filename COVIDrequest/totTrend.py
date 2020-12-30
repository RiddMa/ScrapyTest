import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    addr = 'G:/Courseware/Python/ScrapyTest/COVIDrequest/data'
    data = pd.DataFrame()
    for root, directories, filenames in os.walk(addr):
        for filename in filenames:
            data_tmp = pd.read_csv(os.path.join(addr, filename))
            data = data.append(data_tmp, ignore_index=True)
    data = data.drop('#', axis=1)
    world = data[data['Country, Other'] == 'world']
    day = np.array(range(1, 16))

    plt.plot(day, pd.to_numeric(world['Total Cases'][1:16], errors='ignore'), linewidth=1, linesytle='-', marker='o')
    plt.legend()
    plt.ylim()
    plt.title("Total Trend")
    plt.show()




main()
