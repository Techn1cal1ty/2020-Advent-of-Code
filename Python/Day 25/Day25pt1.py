import sys
import re

def main(fileName):
    c1, c2 = 2069194, 16426071
    c1loop = 0
    c2loop = 0
    temp = 7
    while temp != c1:
        temp *= 7
        temp = temp % 20201227
        c1loop += 1
    temp = 7
    while temp != c2:
        temp *= 7
        temp = temp % 20201227
        c2loop += 1
    print('{} {}'.format(c1loop, c2loop))
    temp = c2
    for i in range(c1loop):
        c2 *= temp
        c2 = c2 % 20201227
    print(c2)
    temp = c1
    for i in range(c2loop):
        c1 *= temp
        c1 = c1 % 20201227
    print(c1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'dataFile'
    else:
        fileName = sys.argv[1]
    main(fileName)
