from collections import Counter

file = open('input.txt', "r")
lines = file.readlines()
file.close()

oxygen_generator_rating = ''
co2_scrubber_rating = ''
number_bits = len(lines[0])


def find_line(most_common=True):
    filtered_result = lines
    for bit in range(0, number_bits - 1):
        tab_bit = [line[bit] for line in filtered_result]
        counter = Counter(tab_bit).most_common()
        if len(counter) == 2:
            bit_criteria = counter[0 if most_common else 1][0] if counter[0][1] != counter[1][1] else (
                '1' if most_common else '0')
        elif len(counter) == 1:
            bit_criteria = counter[0][0]
        filtered_result = [
            line for line in filtered_result if line[bit] == bit_criteria]
    return filtered_result[0]


oxygen_generator_rating = find_line().strip()
co2_scrubber_rating = find_line(most_common=False).strip()

oxygen_generator_rating_int = int(oxygen_generator_rating, 2)
co2_scrubber_rating_int = int(co2_scrubber_rating, 2)


print(
    f'Oxygen Generator Rating: {oxygen_generator_rating}(base2) = {oxygen_generator_rating_int}(base10)')
print(
    f'CO2 Scrubber Rating: {co2_scrubber_rating}(base2) = {co2_scrubber_rating_int}(base10)')
print(f'Answer : {oxygen_generator_rating_int*co2_scrubber_rating_int}')
