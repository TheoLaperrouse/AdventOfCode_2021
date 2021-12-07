from collections import Counter
import copy

file = open('input.txt', "r")
lines = file.readlines()
file.close()

day=0
fishs = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
first_fishs = [int(line) for line in lines[0].split(',')]
counter = Counter(first_fishs).most_common()

#Initialize
for count_fish in counter:
    fishs[f'{count_fish[0]}'] += count_fish[1]
    
while day < 256:
    prev_fishs = copy.copy(fishs)
    for key in fishs.keys():
        if key == '8':
            # new_born
            fishs['8'] = prev_fishs['0']
        elif key == '6':
            # almost_new_born + parents 
            fishs['6'] = prev_fishs['7'] + prev_fishs['0']
        else:
            fishs[key] = prev_fishs[f'{int(key)+1}']
    day += 1

print(sum([fishs[key] for key in fishs.keys()]))
