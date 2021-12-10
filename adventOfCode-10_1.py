from collections import Counter
file = open('input.txt', "r")
lines = file.readlines()
file.close()
lines = [list(line.strip()) for line in lines]

tab_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
closes = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

opens = []
invalid_carac = []

for line in lines:
    find_first_invalid = False
    for carac in line:
        if carac in ['(', '<', '{', '[']:
            opens.append(carac)
        elif carac == closes[opens[-1]]:
            del opens[-1]
        elif not find_first_invalid:
            invalid_carac.append(carac)
            find_first_invalid = True

counter = Counter(invalid_carac).most_common()
res = sum([tab_points[close[0]]*close[1] for close in counter])
print(f'Résultat : {res}')
