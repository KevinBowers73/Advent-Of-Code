floor = 0
count = 0
with open("/Users/kevinbowers/google_drive/coding/Advent-of-Code/2015/Day 1/input.txt") as file:
    for line in file:
        for ch in line:
            if ch == '(':
                floor += 1
                count += 1
            else:
                floor -= 1
                count += 1
            
            if floor == -1:
                print(count)
                break
