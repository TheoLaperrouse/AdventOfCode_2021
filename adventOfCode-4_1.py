file = open('input.txt', "r")
lines = file.readlines()
file.close()

order_results = lines[0].replace('\n','').split(',')
grids = []
grid = []
missing_numbers = []
correct = False
res_bingo = []
index_bingo = 0

def valid_grid(grid,numbers_bingo):
    for line in grid:
        if all(number in numbers_bingo for number in line):
            return True
    for index in range(5):
        if all(array[index] in numbers_bingo for array in grid):
            return True
    return False

for index,line in enumerate(lines[2:]):
    if index+1 == len(lines[2:]):
           numberParser = [number for number in lines[index].replace('\n','').split(' ') if number != '']
           grid.append(numberParser)
    if lines[index+1].strip() != '':
        numberParser = [number for number in lines[index+1].replace('\n','').split(' ') if number != '']
        grid.append(numberParser)
    else:
        grids.append(grid)
        grid=[]

while not correct:
    res_bingo.append(order_results[index_bingo])
    index_bingo += 1
    for grid_index,grid in enumerate(grids[1:]):
        if valid_grid(grid,res_bingo):
            grid_ok = grid
            correct = True

for small_grid in grid_ok:
    missing_numbers = missing_numbers + [int(number) for number in small_grid if number not in res_bingo]
print(f'Résultat : {int(sum(missing_numbers)) * int(order_results[83])}')