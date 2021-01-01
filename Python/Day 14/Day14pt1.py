import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            records.append(line)
    return records

def main(fileName):
    records = readFile(fileName)
    mask = records[0]
    addresses = {}
    sum = 0
    for record in records:
        if record[0:4] == 'mask':
            mask = record[7:]
        else:
            temp = int(record[(record.index('=')) + 1:])
            temp = bin(temp)
            temp = temp[2:]
            temp = str(temp)
            for i in range(36 - len(temp)):
                temp = '0' + temp
            new = ''
            for i in range(len(mask)):
                if mask[i] != 'X':
                    new += mask[i]
                else:
                    new += temp[i]
            addresses[record[4:record.index(']')]] = new
    for entry in addresses:
        temp = 0
        for i in range(36):
            if addresses[entry][0 - i - 1] == '1':
                temp += 2**i
        sum += temp
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day14data'
    else:
        fileName = sys.argv[1]
    main(fileName)
