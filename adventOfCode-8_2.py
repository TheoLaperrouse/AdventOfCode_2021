from collections import Counter

file = open('input.txt', "r")
lines = file.readlines()
file.close()

easy_digits = {2: 1, 3: 7, 4: 4, 7: 8}
decoded_digits = []
res = []
input_segments = []


def get_digits(tab_pattern):
    res = {}
    for pattern in tab_pattern:
        if len(pattern) == 4:
            carac_four = pattern
    for pattern in tab_pattern:
        if len(pattern) == 2:
            right = pattern
    for pattern in tab_pattern:
        if len(pattern) == 7:
            top_bottom_bot_left = pattern
            for digit in carac_four:
                top_bottom_bot_left = top_bottom_bot_left.replace(digit, '')
    for pattern in tab_pattern:
        if len(pattern) == 2:
            middle_top_left = carac_four
            for digit in pattern:
                middle_top_left = middle_top_left.replace(digit, '')

    for pattern in tab_pattern:
        if len(pattern) in [2, 3, 4, 7]:
            res[pattern] = easy_digits[len(pattern)]
        elif len(pattern) == 5:
            if all(digit in pattern for digit in middle_top_left):
                res[pattern] = 5
            elif all(digit in pattern for digit in top_bottom_bot_left):
                res[pattern] = 2
            else:
                res[pattern] = 3
        elif len(pattern) == 6:
            if all(digit in pattern for digit in right):
                if all(digit in pattern for digit in top_bottom_bot_left):
                    res[pattern] = 0
                else:
                    res[pattern] = 9
            elif all(digit in pattern for digit in top_bottom_bot_left):
                res[pattern] = 6
    return res


for line in lines:
    input_segments = line.split('|')[0].split()
    output_segments = line.split('|')[1].split()
    patterns = get_digits(input_segments)
    string_decode = ""
    for segment in output_segments:
        for pattern in patterns:
            if sorted(segment) == sorted(pattern):
                string_decode += str(patterns[pattern])
    res.append(int(string_decode))

print(f'Résultat : {sum(res)}')
