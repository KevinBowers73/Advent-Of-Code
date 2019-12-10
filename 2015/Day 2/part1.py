sqftg = 0
with open("/Users/kevinbowers/google_drive/coding/Advent-of-Code/2015/Day 2/input.txt") as file:
    for line in file:
        tuple = list(map(int, line.split("x")))
        area = tuple[0]*tuple[1]*2 + tuple[0]*tuple[2]*2 + tuple[1]*tuple[2]*2
        tuple.remove(max(tuple))
        extra = tuple[0]*tuple[1]
        this = area + extra
        sqftg += this
    print(sqftg)
