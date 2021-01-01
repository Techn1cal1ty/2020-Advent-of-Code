import sys
import re

def readFile(fileName):
    records = []
    personal = []
    with open(fileName) as file:
        lineNum = 1
        for line in file:
            line = line.strip()
            if line != '':
                if lineNum < 21:
                    records.append(line)
                else:
                    newLine = line.split(',')
                    if lineNum == 22:
                        for obj in newLine:
                            personal.append(int(obj)) 
                    if lineNum > 23:
                        for obj in newLine:
                            records.append(int(obj))
                lineNum += 1
    return records, personal

def main(fileName):
    records, personal = readFile(fileName)
    ok = []
    ranges = {}
    order = {}
    for i in range(20):
        temp = []
        for j in range(20):
            temp.append(j)
        order[i] = temp
    for i in range(20):
        otherTemp = []
        low = int(records[i][records[i].index(':') + 1:records[i].index('-')])
        lowHi = int(records[i][records[i].index('-') + 1:records[i].index(' or ')])
        temp = records[i][records[i].index(' or ') + 4:]
        hi = int(temp[0:temp.index('-')])
        hiHi = int(temp[temp.index('-') + 1:])
        for j in range(low, lowHi + 1):
            otherTemp.append(j)
            if j not in ok:
                ok.append(j)
        for j in range(hi, hiHi + 1):
            otherTemp.append(j)
            if j not in ok:
                ok.append(j)
        ranges[i] = otherTemp
    for i in range(20):
        counter = i + 20
        while counter < len(records) and len(order):
            temp = records[counter]
            if temp in ok:
                for j in ranges:
                    if temp not in ranges[j]:
                        order[i].remove(j)
            counter += 20
    for k in range(20):
        for i in range(20):
            if len(order[i]) == 1:
                for j in range(20):
                    if j != i:
                        if order[i][0] in order[j]:
                            order[j].remove(order[i][0]) 
    sum = 1
    for i in order:
        if order[i][0] < 6:
            sum *= personal[i]
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day16data'
    else:
        fileName = sys.argv[1]
    main(fileName)
