file_path = "input.txt"

list1 = []
list2 = []
final_list = []

with open(file_path, "r") as file:
    for line in file:
        parts = line.split()
        list1.append(parts[0])
        list2.append(parts[1])

list1.sort()
list2.sort()

for i in range(len(list1)):
    value = (int(list1[i]) - int(list2[i]))
    if value <= 0:
        value = abs(value)
    else:
        pass
    final_list.append(value)

print(sum(final_list))


