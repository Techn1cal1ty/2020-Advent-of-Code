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
    for i in records:
        temp = int(i, 2)
        if temp > high:
            high = temp
    print(high)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day5data'
    else:
        fileName = sys.argv[1]
    main(fileName)
