import matplotlib.pyplot as plt
import random as rd
import csv


def main():
    with open("datac.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sem', 'student_id', 'rank'])
        lz = [x for x in range(1, 11)]
        for sem in range(1, 4):
            rd.shuffle(lz)
            for i in range(1, len(lz) + 1):
                writer.writerow([sem, lz[i - 1], i])


if __name__ == '__main__':
    main()
