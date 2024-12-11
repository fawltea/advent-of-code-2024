import re

with open('input.txt', 'r') as file:
    input_string = file.read()

import re

corrupted_memory = input_string

pattern = r"\bmul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, corrupted_memory)

result_sum = sum(int(x) * int(y) for x, y in matches)


print(result_sum)
