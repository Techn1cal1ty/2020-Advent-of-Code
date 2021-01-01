import sys
import re

def CreateRecord(inStr):
    return inStr

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            records.append(line)

    return records

def main(fileName):
    records = readFile(fileName)
    sum = 0
    line = 0
    visited = []
    while line < len(records):
        if line in visited:
            break
        else:
            visited.append(line)
            record = records[line]
            if record[0:3] == 'acc':
                if record[4] == '+':
                    sum += int(record[5:])
                else:
                    sum -= int(record[5:])
            elif record[0:3] == 'jmp':
                if record[4] == '+':
                    line += int(record[5:]) - 1
                else:
                    line -= int(record[5:]) + 1
            line += 1
    print(sum)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day8data'
    else:
        fileName = sys.argv[1]
    main(fileName)
