import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
            records.append(line)
    return records

def main(fileName):
    records = readFile(fileName)
    high = 0
    seats = []
    for i in records:
        seats.append(int(i, 2))
    for i in range(1000):
        if i - 1 in seats and i + 1 in seats and i not in seats:
            print(i)
            break


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day5data'
    else:
        fileName = sys.argv[1]
    main(fileName)
