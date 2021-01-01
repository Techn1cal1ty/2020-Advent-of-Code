import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        firstline = True
        for line in file:
            line = line.strip()
            if firstline:
                records.append(int(line))
                firstline = False
            else:
                newLine = line.split(',')
                for obj in newLine:
                    if obj != 'x':
                        records.append(int(obj))
    return records

def main(fileName):
    records = readFile(fileName)
    arrival = records[0]
    bus = records[1]
    wait = bus - arrival%bus
    for i in range(2, len(records)):
        if records[i] != 'x':
            tempBus = records[i]
            if tempBus - arrival%tempBus < wait:
                wait = tempBus - arrival%tempBus
                bus = records[i]
    print(bus)
    print(wait)
    print(bus*wait)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day13data'
    else:
        fileName = sys.argv[1]
    main(fileName)
