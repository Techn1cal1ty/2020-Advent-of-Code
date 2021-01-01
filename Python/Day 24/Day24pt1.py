import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = str(line.strip())
            line = re.findall(r'[ns]*[we]', line)
            records.append(line)
    return records

def main(fileName):
    records = readFile(fileName)
    flipped = {}
    for record in records:
        x = 0
        y = 0
        for i in record:
            if i == 'ne':
                x += 1
                y += 1
            elif i == 'e':
                x += 2
            elif i == 'se':
                x += 1
                y -= 1
            elif i == 'nw':
                x -= 1
                y += 1
            elif i == 'w':
                x -= 2
            elif i == 'sw':
                x -= 1
                y -= 1
        key = str(x) + ',' + str(y)
        if key not in flipped.keys():
            flipped[key] = True
        else:
            flipped[key] *= -1
    count = 0
    for i in flipped.keys():
        if flipped[i] == True:
            count += 1
    print(count)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day24data'
    else:
        fileName = sys.argv[1]
    main(fileName)
