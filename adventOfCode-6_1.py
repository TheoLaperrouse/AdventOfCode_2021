file = open('input.txt', "r")
lines = file.readlines()
file.close()

fishs = [int(line) for line in lines[0].split(',')]
day=0
while day < 80:
    fishs_of_the_day = fishs
    for index,fish in enumerate(fishs_of_the_day):
        if fish == 0:
            fishs[index] = 6
            fishs.append(9)
        else:
            fishs[index] -= 1
    day += 1
print(len(fishs))