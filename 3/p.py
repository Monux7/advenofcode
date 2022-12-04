def search(line):
    length = len(line) - 1
    first = line[0 : int(length / 2)]
    second = line[int(length / 2) : length]
    for c in first:
        if second.find(c) != -1:
            return c

def getCharValue(c):
    o = ord(c)
    if o >= 97:
        return o - 96
    elif o >= 65:
        return o - 64 + 26

f = open("input.txt", "r")

s = 0
for line in f.readlines():
    s += getCharValue(search(line))

print(s)