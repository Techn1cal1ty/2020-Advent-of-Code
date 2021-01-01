import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            records.append(line)
    return records

def findSurrounding(chart, row, seat):    
    neighbors = 0
    U = True
    D = True
    L = True
    R = True
    if row == 0:
        U = False
    if row == 92: 
        D = False
    if seat == 0:
        L = False
    if seat == 94: 
        R = False
    if U:
        if chart[row - 1][seat] == '#':
            neighbors += 1
    if D:
        if chart[row + 1][seat] == '#':
            neighbors += 1
    if L:
        if chart[row][seat - 1] == '#':
            neighbors += 1
    if R:
        if chart[row][seat + 1] == '#':
            neighbors += 1
    if U and R:
        if chart[row - 1][seat + 1] == '#':
            neighbors += 1
    if U and L:
        if chart[row - 1][seat - 1] == '#':
            neighbors += 1
    if D and R:
        if chart[row + 1][seat + 1] == '#':
            neighbors += 1
    if D and L:
        if chart[row + 1][seat - 1] == '#':
            neighbors += 1
    return neighbors
    
def findNextGen(chart):
    nextGen = []
    for row in range(len(chart)):
        newRow = ''
        for seat in range(len(chart[0])):
            if chart[row][seat] == '.':
                newRow += '.'
            else:
                neighbors = findSurrounding(chart, row, seat)
                if chart[row][seat] == 'L':
                    if neighbors == 0:
                        newRow += '#'
                    else: 
                        newRow += 'L'
                elif neighbors < 4:
                    newRow += '#'
                else:
                    newRow += 'L'
        nextGen.append(newRow)
    return nextGen                    

def main(fileName):
    chart = readFile(fileName)  #current generation
    nextGen = findNextGen(chart)
    sum = 0
    while nextGen != chart:
        chart = nextGen.copy()
        nextGen = findNextGen(chart)
    for row in chart:
        for seat in row:
            if seat == '#':
               sum += 1
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day11data'
    else:
        fileName = sys.argv[1]
    main(fileName)
