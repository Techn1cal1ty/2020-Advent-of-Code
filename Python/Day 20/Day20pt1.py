import sys
import re

def readFile(fileName):
    records = {}
    with open(fileName) as file:
        temp = []
        tile = ''
        for line in file:
            line = line.strip()
            if line != '':
                if line[0] == 'T':
                    tile = line[5:9]
                else:
                    temp.append(line)
            else:
                records[tile] = temp
                temp = []
    return records

def main(fileName):
    records = readFile(fileName)
    edges = {}
    prod = 1
    for key in records.keys():
        temp = []
        l = ''
        r = ''
        tile = records[key]
        for i in tile:
            l += i[0]
        for i in tile:
            r += i[-1]
        temp.append(tile[0])
        temp.append(tile[-1])
        temp.append(r)
        temp.append(l)
        temp.append(r[::-1])
        temp.append(l[::-1])
        temp.append(tile[0][::-1])
        temp.append(tile[-1][::-1])
        edges[key] = temp
    for key in edges.keys():
        check = edges[key]
        found = []
        for otherKey in edges.keys():
            if otherKey != key:
                comp = edges[otherKey]
                for side in check:
                    if side in comp:
                        if side not in found:
                            found.append(side)
        if len(found) == 4:
            prod *= int(key)
    print(prod)
                        





if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day20data'
    else:
        fileName = sys.argv[1]
    main(fileName)
