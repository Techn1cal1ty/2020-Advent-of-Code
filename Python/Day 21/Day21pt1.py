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
    allergens = {}
    totalList = []
    aCounter = {}
    ingredients = []
    for i in records:
        contains = i[i.index('contains ') + 9:-1]
        contains = contains.replace(',', '')
        contains = contains.split()
        ing = i[:i.index('contains ') - 2]
        ing = ing.split()
        for j in contains:
            if j not in allergens.keys():
                allergens[j] = {}
            for k in ing:
                if k in allergens[j]:
                    allergens[j][k] += 1
                else:
                    allergens[j][k] = 1
                if k not in ingredients:
                    ingredients.append(k)
            if j not in aCounter.keys():
                aCounter[j] = 1
            else:
                aCounter[j] += 1
        for z in ing:
            totalList.append(z)
    for i in allergens.keys():
        for j in allergens[i].keys():
            if allergens[i][j] == aCounter[i]:
                if j in ingredients:
                    ingredients.remove(j)
    count = 0
    for i in totalList:
        for j in ingredients:
            if j == i:
                count += 1
    print(count)
    print(ingredients)
        
            

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day21data'
    else:
        fileName = sys.argv[1]
    main(fileName)
