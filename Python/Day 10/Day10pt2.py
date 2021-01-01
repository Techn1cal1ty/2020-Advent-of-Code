import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = int(line.strip())
            records.append(line)
    return records

def main(fileName):
    records = [0]
    add = readFile(fileName)
    for i in add:
        records.append(i)
    records.sort(reverse = True)
    newRecords = {}
    for record in records:
        tempSum = 0
        for i in range(3):
            if record + i + 1 in records:
                tempSum += newRecords[record + i + 1]
        if tempSum == 0:
            tempSum = 1
        newRecords[record] = tempSum
    print(newRecords[0])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day10data'
    else:
        fileName = sys.argv[1]
    main(fileName)
