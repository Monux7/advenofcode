f = open("D:\\Daten\\Development\\Python\\Advent of Code 2022\\1\\input.txt", "r")
l = f.readlines()

ranks = []
current = 0

for x in l:
    if x.strip():
        current += int(x)
    else:
        ranks.append(current)

        current = 0

ranks.sort()
print(ranks[len(ranks) - 1] + ranks[len(ranks) - 2] + ranks[len(ranks) - 3])