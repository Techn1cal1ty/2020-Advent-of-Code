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

def rotate(x, y, wpX, wpY, direction, deg):
    wpX = wpX + x
    wpY = wpY + y
    xDif = wpX - x
    yDif = wpY - y
    if deg == 180:
        wpX -= xDif*2
        wpY -= yDif*2
    elif (direction == 'L' and deg == 90) or (direction == 'R' and deg == 270):
        wpX = x - yDif
        wpY = y + xDif
    else:
        wpX = x + yDif
        wpY = y - xDif
    return wpX, wpY

def main(fileName):
    directions = readFile(fileName)
    x = 0
    y = 0
    wpX = 10
    wpY = 1
    for line in directions:
        if line[0] == 'N':
            wpY += line[1]
        elif line[0] == 'S':
            wpY -= line[1]
        elif line[0] == 'E':
            wpX += line[1]
        elif line[0] == 'W':
            wpX -= line[1]
        elif line[0] == 'R' or line[0] == 'L':
            wpX, wpY = rotate(x, y, wpX, wpY, line[0], line[1])
            wpX -= x
            wpY -= y
        else:
            x += wpX*line[1]
            y += wpY*line[1]
    print(abs(x) + abs(y))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day12data'
    else:
        fileName = sys.argv[1]
    main(fileName)
