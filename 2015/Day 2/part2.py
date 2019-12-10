feet = 0
with open("/Users/kevinbowers/google_drive/coding/Advent-of-Code/2015/Day 2/input.txt") as file:
    for line in file:
        tuple = list(map(int, line.split("x")))
        volume = 1
        for num in tuple: volume *= num
        tuple.remove(max(tuple))
        dimenfeet = tuple[0]*2 + tuple[1]*2
        feet += dimenfeet + volume
    print(feet)
