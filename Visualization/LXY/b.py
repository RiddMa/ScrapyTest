import matplotlib.pyplot as plt


#  用于将csv中的每行的数据统计，return字典
def convert(lz: list) -> dict:
    dic = {}
    for element in lz:
        x = float(element)
        r = int(x // 5)
        if r not in dic:
            dic[r] = 1
        else:
            dic[r] += 1
    return dic


def main():
    dic = {}
    lz = []
    with open("data1402.csv", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        dic = convert(lines)
    for i in dic:
        s = str(i * 5) + '~' + str(i * 5 + 5)
        lz.append((i, s, dic[i]))
    lz.sort(key=lambda xx: xx[0])
    x = [i[1] for i in lz]
    y = [i[2] for i in lz]
    plt.bar(x, y)
    for a, b in zip(x, y):
        plt.text(a, b, '%d' % b, ha='center')
    plt.show()


if __name__ == '__main__':
    main()
