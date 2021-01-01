import sys
import re

def main(fileName):
    input = [7,14,0,17,11,1,2]
    prev = {}
    pn = 0
    counter = 1
    for i in input:
        prev[i] = counter
        counter += 1
    while counter < 2020:
        if pn in prev.keys():
            temp = counter - prev[pn]
            prev[pn] = counter
            pn = temp
        else:
            prev[pn] = counter
            pn = 0
        counter += 1
    print(pn)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day15data'
    else:
        fileName = sys.argv[1]
    main(fileName)
