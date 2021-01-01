import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = int(line.strip())
            records.append(line)
    return records

def isWrong(records, location):
    prev = records[location-25:location]
    for i in prev:
        for j in prev:
            if i + j == records[location]:
                return False
    return True

def main(fileName):
    records = readFile(fileName)
    preamble = records[0:25]
    location = 0
    for record in records:
        if record not in preamble:
            isOk = isWrong(records, location)
            if isOk:
                print(record)
        location += 1
    print('done')




if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day9data'
    else:
        fileName = sys.argv[1]
    main(fileName)
