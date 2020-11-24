def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


if __name__ == '__main__':
    lz = []
    with open("PPLianJia.json", "r", encoding="utf-8") as f:
        # lz.append(f.readlines())
        suitePrice = []
        unitPrice = []
        result = []
        source = f.readlines()
        for i in range(0, len(source)):
            # lz = source[i][1:-3].split(", ")
            lz = source[i][1:-3].split(": ")
            lz = lz[1:]
            lz[0] = lz[0][2:-22]
            lz[1] = lz[1][2:-19]
            lz[2] = lz[2][2:-18]
            lz[3] = lz[3][2:-9]
            lz[4] = lz[4][2:-14]
            lz[5] = lz[5][5:-18].split("-")[0]
            lz[6] = str(get_num(lz[6])/10000)
            lz[7] = str(get_num(lz[7]))

            unitPrice.append(float(lz[6]))
            suitePrice.append(int(lz[7]))
            result.append(lz)
        print(source)