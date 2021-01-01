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
    aCounter = {}
    ingredients = []
    q = {}
    e = []
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
    for i in allergens.keys():
        for j in allergens[i].keys():
            if allergens[i][j] == aCounter[i]:
                if j not in q:
                    if i not in q.keys():
                        q[i] = [j]
                    else:
                        q[i].append(j)
                if i not in e:
                    e.append(i)
    for zzzz in range(5):
        for i in q.keys():
            if len(q[i]) == 1:
                for j in q.keys():
                    if j != i:
                        if q[i][0] in q[j]:
                            q[j].remove(q[i][0])
    e.sort()
    s = ''
    for entry in e:
        s += q[entry][0] + ','
    print(s[:-1])
        
            

if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'day21data'
    else:
        fileName = sys.argv[1]
    main(fileName)
