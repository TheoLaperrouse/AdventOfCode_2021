from collections import Counter

file = open('input.txt', "r")
lines = file.readlines()
file.close()

output_segment = []

for line in lines:
    output_segment += line.split('|')[1].split()

len_output_segment = list(map(len, output_segment))
counter = Counter(len_output_segment).most_common()
# 8:7 1:2 4:4 7:3
res = sum([count[1] for count in counter if count[0] in [7, 4, 2, 3]])
print(f'Résultats : {res}')
