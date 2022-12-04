def getCharValue(c):
    o = ord(c)
    if o >= 97:
        return o - 96
    elif o >= 65:
        return o - 64 + 26

def compare(l1, l2, l3):
    sames = []
    for a in l1:
        if l2.find(a) != -1:
            sames.append(a)

    for s in sames:
        if s != '\n' and l3.find(s) != -1:
            return s

f = open("input.txt", "r")
l = f.readlines()

numbers = 0

for x in range(int(len(l) / 3)):
    l1 = l[3*x]
    l2 = l[3*x + 1]
    l3 = l[3*x +  2]

    s = compare(l1, l2, l3)

    numbers += getCharValue(s)

print(numbers)