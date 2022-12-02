def convert(c):
    if c == "A" or c == "X": 
        return 1
    elif c == "B" or c == "Y":
        return 2
    elif c == "C" or c == "Z":
        return 3

def win(c):
    if c == "X": 
        return -1
    elif c == "Y":
        return 0
    elif c == "Z":
        return 1

f = open("D:\\Daten\\Development\\Python\\Advent of Code 2022\\2\\input.txt", "r")

value_1 = 0
value_2 = 0

for l in f.readlines():
    enemy = convert(l[0])

    #1
    self = convert(l[2])
    if (self - 1) == (enemy % 3):   #win
        value_1 += 6
    elif self == enemy:             #draw
        value_1 += 3

    value_1 += self

    #2
    win_ = win(l[2])
    
    self = enemy + win_
    if self == 4: self = 1
    elif self == 0: self = 3

    value_2 += self
    value_2 += win_ * 3 + 3
    

print("1: " + str(value_1))
print("2: " + str(value_2))