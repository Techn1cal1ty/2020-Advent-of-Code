import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        firstline = True
        for line in file:
            line = line.strip()
            if firstline:
                firstline = False
            else:
                newLine = line.split(',')
                for obj in newLine:
                    records.append(obj)
    return records

def checker(modRecords, t):
    for entry in modRecords:
        if (t + entry[1]) % entry[0] != 0:
            return False
    return True

def main(fileName):
    records = readFile(fileName)
    modRecords = []
    counter = 0
    for i in records:
        if i != 'x':
            temp = [int(i), counter]
            modRecords.append(temp)
        counter += 1
    step = modRecords[0][0]
    t = step * int(100000000000000/step)
    found = [step]
    while checker(modRecords, t) == False:
        for entry in modRecords:
            if (t + entry[1]) % entry[0] != 0:
                break
            if entry[0] not in found:
                step *= entry[0]
                found.append(entry[0])
        t += step
        print(t)
    print(t)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day13data'
    else:
        fileName = sys.argv[1]
    main(fileName)
