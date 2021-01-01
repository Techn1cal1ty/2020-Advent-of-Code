import sys
import re
import copy

def readFile(fileName):
    records = {}
    temp = []
    y = 7
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            x = 0
            for i in line:
                records[(x, y, 0, 0)] = i
                x += 1
            y -= 1
    return records

def main(fileName):
    records = readFile(fileName)
    for a in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 9):
                for x in range(-1, 9):
                    if (x, y, z, a) not in records.keys():
                        records[(x, y, z, a)] = '.'
    for counter in range(6):
        nextGen = {}
        for i in records.keys():
            x = i[0]
            y = i[1]
            z = i[2]
            a = i[3]
            count = 0
            for am in range(-1, 2):
                for zm in range(-1, 2):
                    for ym in range(-1, 2):
                        for xm in range(-1, 2):
                            if zm != 0 or xm != 0 or ym != 0 or am != 0:
                                nk = (x + xm, y + ym, z + zm, a + am)
                                if nk not in records.keys():
                                    nextGen[nk] = '.'
                                else:
                                    if records[nk] == '#':
                                        count += 1
            if records[(x, y, z, a)] == '#':
                if count == 2 or count == 3:
                    nextGen[(x, y, z, a)] = '#'
                else: 
                    nextGen[(x, y, z, a)] = '.'
            elif count == 3:
                nextGen[(x, y, z, a)] = '#'
            else: 
                nextGen[(x, y, z, a)] = '.'
        records = copy.deepcopy(nextGen)
    count = 0
    for i in records.keys():
        if records[i] == '#':
            count += 1
    print(count)



if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day17data'
    else:
        fileName = sys.argv[1]
    main(fileName)
