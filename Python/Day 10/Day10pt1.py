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
    records = readFile(fileName)
    records.sort()
    onediff = 1
    threediff = 1
    for i in range(len(records) - 1):
        if records[i+1] - records[i] == 1:
            onediff += 1
        elif records[i+1] - records[i] == 3:
            threediff += 1
    print(onediff*threediff)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day10data'
    else:
        fileName = sys.argv[1]
    main(fileName)
