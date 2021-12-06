
file = open('input.txt', "r")
lines = file.readlines()
file.close()
compteur = 0
sum_lines_prec = -1
for index, line in enumerate(lines):
    if index + 2 < len(lines):
        sum_lines = int(line) + int(lines[index+1]) + int(lines[index+2])
        if sum_lines_prec < sum_lines:
            compteur += 1
        sum_lines_prec = sum_lines
print(compteur - 1)
