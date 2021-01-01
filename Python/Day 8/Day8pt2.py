import sys
import re

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            records.append(line)

    return records

def main(fileName):
    records = readFile(fileName)
    counter = 0
    acc = 0
    for record in records:
        temp = records.copy()
        storage = record[3:]
        if record[0:3] == 'nop':
            temp[counter] = 'jmp' + storage
            if runner(temp) != -1:
                acc = runner(temp)
        elif record[0:3] == 'jmp':
            temp[counter] = 'nop' + storage
            if runner(temp) != -1:
                acc = runner(temp)
        counter += 1
    print(acc)
            

def runner(records):
    sum = 0
    line = 0
    visited = []
    while line < len(records):
        if line in visited:
            return -1
        else:
            visited.append(line)
            record = records[line]
            if record[0:3] == 'acc':
                if record[4] == '+':
                    sum += int(record[5:])
                else:
                    sum -= int(record[5:])
            elif record[0:3] == 'jmp':
                if record[4] == '+':
                    line += int(record[5:]) -1
                else:
                    line -= int(record[5:]) +1
            line += 1
    return(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day8data'
    else:
        fileName = sys.argv[1]
    main(fileName)
