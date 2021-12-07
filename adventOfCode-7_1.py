from collections import Counter
import copy

file = open('input.txt', "r")
lines = file.readlines()
file.close()

allFuels = []

horizontal_positions = [int(line) for line in lines[0].split(',')]
maxPos = max(horizontal_positions)
for dest in range(maxPos):
    allFuel = 0
    for horizontal_pos in horizontal_positions:
        if dest > horizontal_pos:
            allFuel += dest - horizontal_pos
        elif dest < horizontal_pos :
            allFuel +=  horizontal_pos - dest
    allFuels.append([dest,allFuel])

allFuels.sort(key = lambda x: x[1], reverse=True)
print(allFuels)