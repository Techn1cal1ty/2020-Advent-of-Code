import sys
import re
import copy

def main(fileName):
    inpt = 389125467
    cups = []
    while inpt > 0:
        cups.append(inpt % 10)
        inpt = int(inpt / 10)
    cups.reverse()
    n = 0
    for i in range(100):
        curCup = cups[n]
        if cups[n] == 1:
            target = 9
        else:
            target = cups[n] - 1
        move = []
        if n < 6:
            move.append(cups.pop(n + 1))
            move.append(cups.pop(n + 1))
            move.append(cups.pop(n + 1))
        elif n == 6:
            move.append(cups.pop(7))
            move.append(cups.pop(7))
            move.append(cups.pop(0))
        elif n == 7:
            move.append(cups.pop(8))
            move.append(cups.pop(0))
            move.append(cups.pop(0))
        else:
            move.append(cups.pop(0))
            move.append(cups.pop(0))
            move.append(cups.pop(0))
        while target in move:
            if target == 1:
                target = 9
            else:
                target -= 1
        loc = cups.index(target)
        temp = copy.deepcopy(cups[0:loc + 1])
        temp.extend(move)
        for j in cups[loc + 1:]:
            temp.append(j)
        cups = temp
        n = (cups.index(curCup) + 1) % 9
    start = cups.index(1) + 1
    ret = ''
    for i in range(8):
        ret += str(cups[(i + start) % 9])
    print(ret)
        



if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'dataFile'
    else:
        fileName = sys.argv[1]
    main(fileName)
