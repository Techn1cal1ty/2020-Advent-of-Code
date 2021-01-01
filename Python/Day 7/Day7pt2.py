
import sys
import re

def CreateRecord(inStr):
    return inStr

def readFile(fileName):
    records = {}
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            line = line.split()
            color = line[0] + ' ' + line[1]
            contents = {}
            for i in range(4, len(line), 4):
                count = line[i]
                if count != 'no':
                    contentColor = line[i+1] + " " + line[i+2]
                    contents[contentColor] = int(count)
            records[color] = contents
    return records

def main(fileName):
    records = readFile(fileName)
    print(counter('shiny gold', records) - 1)
    
def counter(color, records):
    sum = 1
    bag = records[color]
    for c in bag.keys():
        sum += counter(c, records) * bag[c]
    return sum


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day7data'
    else:
        fileName = sys.argv[1]
    main(fileName)
