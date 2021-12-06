file = open('input.txt', "r")
lines = file.readlines()
file.close()

x = 0
depth = 0

for line in lines:
    instruction = line.split()
    if instruction[0] == "forward":
        x += int(instruction[1])
    if instruction[0] == "down":
        depth += int(instruction[1])
    if instruction[0] == "up":
        depth -= int(instruction[1])

print(f'{x}, {depth}')
print(f'Answer : {x*depth}')
