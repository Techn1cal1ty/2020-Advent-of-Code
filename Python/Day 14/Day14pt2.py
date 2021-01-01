import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            records.append(line)
    return records

def setAddresses(addresses, val, new, xCounter):
    locs = []
    newLocs = []
    for i in range(2**xCounter):
        locs.append(new)
    counter = 0
    for i in locs:
        temp = bin(counter)[2:]
        for j in range(xCounter - len(temp)):
            temp = '0' + temp
        while i.find('X') > -1:
            i = i[0:i.index('X')] + temp[0] + i[i.index('X') + 1:]
            if len(temp) > 1:
                temp = temp[1:]
        counter += 1
        newLocs.append(i)
    for i in newLocs:
        addresses[i] = val
    return addresses

def main(fileName):
    records = readFile(fileName)
    mask = records[0]
    addresses = {}
    sum = 0
    for record in records:
        if record[0:4] == 'mask':
            mask = record[7:]
        else:
            temp = int(record[4:record.index(']')])
            temp = bin(temp)
            temp = temp[2:]
            temp = str(temp)
            for i in range(36 - len(temp)):
                temp = '0' + temp
            new = ''
            xCounter = 0
            for i in range(len(mask)):
                if mask[i] != '0':
                    new += mask[i]
                else:
                    new += temp[i]
                if mask[i] == 'X':
                    xCounter += 1
            addresses = setAddresses(addresses, record[(record.index('=')) + 2:], new, xCounter)
    for entry in addresses:
        sum += int(addresses[entry])
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day14data'
    else:
        fileName = sys.argv[1]
    main(fileName)
