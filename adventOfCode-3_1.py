from collections import Counter

file = open('input.txt', "r")
lines = file.readlines()
file.close()

gamma_rate = ''
epsilon_rate = ''
number_bits = len(lines[0])

for bit in range(0, number_bits - 1):
    tab_bit = [line[bit] for line in lines]
    most_common_bit = Counter(tab_bit).most_common()[0][0]
    gamma_rate += most_common_bit
    epsilon_rate += "0" if most_common_bit == '1' else "1"

gamma_rate_int = int(gamma_rate, 2)
epsilon_rate_int = int(epsilon_rate, 2)

print(f'Gamma Rate : {gamma_rate}(base2) = {gamma_rate_int}(base10)')
print(f'Epsilon Rate : {epsilon_rate}(base2) = {epsilon_rate_int}(base10)')
print(f'Answer : {gamma_rate_int*epsilon_rate_int}')
