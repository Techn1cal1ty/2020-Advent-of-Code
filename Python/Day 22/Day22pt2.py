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

def game(p1, p2):
    old1 = []
    old2 = []
    while len(p1) > 0 and len(p2) > 0:
        temp1 = []
        temp2 = []
        state = False #false = p1 win
        if p1 in old1 or p2 in old2:
            state = False
            return p1, p2, state
        if len(p1) > p1[0] and len(p2) > p2[0]:
            throwaway1, throwaway2, state = game(p1[1:p1[0] + 1], p2[1:p2[0] + 1])  
        elif p1[0] < p2[0]:
            state = True
        if state == False:
            temp1 = p1[1:]
            temp2 = p2[1:]
            temp1.append(p1[0])
            temp1.append(p2[0])
        else:
            temp2 = p2[1:]
            temp1 = p1[1:]
            temp2.append(p2[0])
            temp2.append(p1[0])
        old1.append(p1)
        old2.append(p2)
        p1 = temp1
        p2 = temp2
    return p1, p2, state

def main(fileName):
    p1, p2 = readFile(fileName)
    p1, p2, state = game(p1, p2)
    sum = 0
    p1.reverse()
    p2.reverse()
    if state:
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
