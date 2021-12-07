file = open('input.txt', "r")
lines = file.readlines()
file.close()

minFuel = 10**20

horizontal_positions = [int(line) for line in lines[0].split(',')]
maxPos = max(horizontal_positions)

for dest in range(maxPos):
    allFuel = 0
    for horizontal_pos in horizontal_positions:
        if dest != horizontal_pos:
            allFuel += abs(dest - horizontal_pos) * \
                (dest - horizontal_pos+1) / 2
    if allFuel < minFuel:
        minFuel = allFuel

print(f'Résultat : {minFuel}')
