
file = open('input.txt', "r")
lines = file.readlines()
file.close()
compteur = 0
line_prec = 0
for index, line in enumerate(lines):
    intLine = int(line)
    if line_prec < intLine:
        compteur += 1
    line_prec = intLine
print(compteur - 1)
