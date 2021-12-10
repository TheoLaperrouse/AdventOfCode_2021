from collections import Counter
import statistics


def scoreTabOpen(opens):
    res = 0
    for open in opens:
        res = res*5 + tab_points[open]
    return res


file = open('input.txt', "r")
lines = file.readlines()
file.close()
lines = [list(line.strip()) for line in lines]

tab_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
closes = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}
opens = []
incomplete_line = []
list_opens = []
for line in lines:
    find_first_invalid = False
    for carac in line:
        if carac in ['(', '<', '{', '[']:
            opens.append(carac)
        elif carac == closes[opens[-1]]:
            del opens[-1]
        else:
            find_first_invalid = True
    if not find_first_invalid:
        list_opens.append(opens[::-1])
    opens = []
allPoints = []
for tab in list_opens:
    allPoints.append(scoreTabOpen(tab))

print(f'Résultat : {int(statistics.median(allPoints))}')
