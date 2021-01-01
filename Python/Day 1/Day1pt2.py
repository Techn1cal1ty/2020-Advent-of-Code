import sys
import re

def CreateRecord(inStr):
    return inStr

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = int(line.strip())
            records.append(line)

    return records

def main(fileName):
    records = readFile(fileName)
    sum = -1
    for i in records:
        for j in records:
            for k in records:
                if i + j + k == 2020:
                    sum = i*j*k
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day1data'
    else:
        fileName = sys.argv[1]
    main(fileName)
