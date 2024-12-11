import re

with open('input.txt', 'r') as file:
    input_string = file.read()

import re

corrupted_memory = input_string

pattern = r"\b(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"


matches = re.findall(pattern, corrupted_memory)

mul_enabled = True 
result_sum = 0

for match in matches:
    instruction = match[0]

    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False 
    else: 
        if mul_enabled:
            x, y = int(match[1]), int(match[2])
            result_sum += x * y

print(f"The sum of all enabled 'mul(X, Y)' results is: {result_sum}")



