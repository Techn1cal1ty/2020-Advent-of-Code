import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            split = []
            split.append(line[0:1])
            num = line[1:]
            split.append(int(num))
            records.append(split)
    return records

def main(fileName):
    directions = readFile(fileName)
    x = 0
    y = 0
    heading = 1
    for line in directions:
        if line[0] == 'N':
            y += line[1]
        elif line[0] == 'S':
            y -= line[1]
        elif line[0] == 'E':
            x += line[1]
        elif line[0] == 'W':
            x -= line[1]
        elif line[0] == 'R':
            heading = (heading + line[1]/90)%4
        elif line[0] == 'L':
            heading = (heading - line[1]/90)%4
        else:
            if heading == 0:
                y += line[1]
            elif heading == 2:
                y -= line[1]
            elif heading == 1:
                x += line[1]
            else:
                x -= line[1]
    print(abs(x) + abs(y))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day12data'
    else:
        fileName = sys.argv[1]
    main(fileName)
