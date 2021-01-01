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

def runner(records):
    preamble = records[0:25]
    location = 0
    for record in records:
        if record not in preamble:
            isOk = isWrong(records, location)
            if isOk:
                return records[location]
        location += 1
    return -1
    
def search(records, target):
    for record in records:
        location = records.index(record)
        run = [record]
        sum = record
        while sum < target:
            sum += records[location+1]
            run.append(records[location+1])
            location += 1
        if sum == target:
            return run

def main(fileName):
    records = readFile(fileName)
    run = search(records, runner(records))
    weakLow = run[0]
    weakHigh = run[0]
    for i in run:
        if i < weakLow:
            weakLow = i
        elif i > weakHigh:
            weakHigh = i
    print(weakHigh + weakLow)
    



    






if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day9data'
    else:
        fileName = sys.argv[1]
    main(fileName)
