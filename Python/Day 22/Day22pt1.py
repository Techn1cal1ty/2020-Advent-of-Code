import sys
import re

def readFile(fileName):
    p1 = []
    p2 = []
    found = False
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            if line != '':
                if line[0] != 'P':
                    if found:
                        p2.append(int(line))
                    else:
                        p1.append(int(line))
            else:
                found = True
    return p1, p2

def main(fileName):
    p1, p2 = readFile(fileName)
    while len(p1) > 0 and len(p2) > 0:
        temp1 = []
        temp2 = []
        if p1[0] > p2[0]:
            temp1 = p1[1:]
            temp2 = p2[1:]
            temp1.append(p1[0])
            temp1.append(p2[0])
        else:
            temp2 = p2[1:]
            temp1 = p1[1:]
            temp2.append(p2[0])
            temp2.append(p1[0])
        p1 = temp1
        p2 = temp2
    sum = 0
    p1.reverse()
    p2.reverse()
    if len(p1) == 0:
        for i in range(len(p2)):
            sum += p2[i]*(i+1)
    else:
        for i in range(len(p1)):
            sum += p1[i]*(i+1)
    print(sum)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day22data'
    else:
        fileName = sys.argv[1]
    main(fileName)
