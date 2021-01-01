import sys
import re

def CreateRecord(inStr):
    # print("Creating a Record from: {}".format(inStr))
    return inStr

def readFile(fileName):
    records = []
    with open(fileName) as file:
        inStr = ""
        for line in file:
            line = line.strip()

            # This code processes each line. in the input file.
            #
            # If this is an empty line, it's the end of the record,
            # so create a new record, and reset the input string.
            if line == "":
                records.append(CreateRecord(inStr.strip()))
                inStr = ""
            else:
                # Add this line to the previous line.
                inStr += line.strip()
                #print("===== inStr = {}".format(inStr))

    return records

def main(fileName):
    data = readFile(fileName)
    sum = 0
    for d in data:
        found = [" "]
        for i in d:
            if i not in found:
                 found += i
                 print(found)
        sum += len(found) -1
        print(sum)
    print(sum)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'dataFile'
    else:
        fileName = sys.argv[1]
    main(fileName)
