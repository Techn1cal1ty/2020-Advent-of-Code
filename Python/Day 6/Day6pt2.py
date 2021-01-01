import sys
import re

def CreateRecord(inStr):
    return inStr

def readFile(fileName):
    records = []
    with open(fileName) as file:
        inStr = ""
        for line in file:
            line = line.strip()
            if line == "":
                records.append(CreateRecord(inStr.strip()))
                inStr = ""
            else:
                inStr += " " + line.strip()

        records.append(inStr.strip())

    return records

def main(fileName):
    data = readFile(fileName)
    sum = 0
    for d in data:
        count = {}
        for word in d.split():
            for c in word:
                if c in count.keys():
                    count[c] += 1
                else:
                    count[c] = 1
        peopleCount = len(d.split())
        for k in count.keys():
            if count[k] == peopleCount:
                sum += 1
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'dataFile'
    else:
        fileName = sys.argv[1]
    main(fileName)
