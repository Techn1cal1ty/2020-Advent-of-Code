import sys
import re

def main(fileName):
    inpt = 653427918
    tempCups = []
    cups = {}
    while inpt > 0:
        tempCups.append(inpt % 10)
        inpt = int(inpt / 10)
    tempCups.reverse()
    prev = 1000000
    nxt = tempCups[1]
    count = 1
    for i in tempCups:
        cups[i] = [prev, nxt]
        prev = i
        if count < 8:
            nxt = tempCups[count + 1]
        else:
            nxt = count + 2
        count += 1
    for i in range(10, 1000001):
        cups[i] = [prev, nxt]
        prev = i
        nxt = i + 2
    cups[1000000][1] = tempCups[0]
    n = tempCups[0]
    for i in range(10000000):
        ahead = cups[cups[cups[cups[n][1]][1]][1]][1]
        start = cups[n][1]
        end = cups[ahead][0]
        cups[start][0] = 'start'
        cups[end][1] = 'end'
        cups[n][1] = ahead
        cups[ahead][0] = n
        target = n - 1
        while target == start or target == end or target == cups[start][1]:
            target -= 1
        if target == 0:
            target = 1000000
            while target == start or target == end or target == cups[start][1]:
                target -= 1
        temp = cups[target][1]
        cups[target][1] = start
        cups[start][0] = target
        cups[end][1] = temp
        cups[temp][0] = end
        n = cups[n][1]
    a = cups[1][1]
    b = cups[cups[1][1]][1]
    print("{} {} {}".format(a, b, a * b))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'dataFile'
    else:
        fileName = sys.argv[1]
    main(fileName)
