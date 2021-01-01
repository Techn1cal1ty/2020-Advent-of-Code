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
            records.append(line)
    return records

def main(fileName):
    holders = ['shiny gold bag']
    records = readFile(fileName)
    for i in range(20):
        for color in holders:
            holders, records = findHolders(color, holders, records)
    print(len(holders)-2)

def findHolders(color, holders, records):
    for rule in records:
        if color in rule:
            bagColor = rule[0: rule.index('bag')]
            if bagColor not in holders:
                holders.append(bagColor)
    return holders, records

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day7data'
    else:
        fileName = sys.argv[1]
    main(fileName)
