file = open('input.txt', "r")
lines = file.readlines()
file.close()

x = 0
depth = 0
aim = 0

for line in lines:
    instruction = line.split()
    if instruction[0] == "forward":
        x += int(instruction[1])
        depth = depth + aim * int(instruction[1])
    if instruction[0] == "down":
        aim += int(instruction[1])
    if instruction[0] == "up":
        aim -= int(instruction[1])

print(f'{x}, {depth}')
print(f'Answer : {x*depth}')
