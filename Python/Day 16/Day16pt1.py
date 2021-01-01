import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        lineNum = 1
        for line in file:
            line = line.strip()
            if line != '':
                if lineNum < 21:
                    records.append(line)
                else:
                    newLine = line.split(',')
                    if lineNum > 24:
                        for obj in newLine:
                            records.append(int(obj))
                lineNum += 1
    return records

def main(fileName):
    records = readFile(fileName)
    ok = []
    sum = 0
    for i in range(20):
        low = int(records[i][records[i].index(':') + 1:records[i].index('-')])
        lowHi = int(records[i][records[i].index('-') + 1:records[i].index(' or ')])
        temp = records[i][records[i].index(' or ') + 4:]
        hi = int(temp[0:temp.index('-')])
        hiHi = int(temp[temp.index('-') + 1:])
        for i in range(low, lowHi + 1):
            if i not in ok:
                ok.append(i)
        for i in range(hi, hiHi + 1):
            if i not in ok:
                ok.append(i)
    for i in range(42, len(records)):
        if records[i] not in ok:
            sum += records[i]
    print(sum)
    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day16data'
    else:
        fileName = sys.argv[1]
    main(fileName)
