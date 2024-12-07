file_path = "input.txt"

list1 = []
list2 = []
final_list = []

with open(file_path, "r") as file:
    for line in file:
        parts = line.split()
        list1.append(parts[0])
        list2.append(parts[1])

for i in range(len(list1)):
    if list2.count(list1[i]) > 0:
        value = (list2.count(list1[i]))
        final_list.append(value * int(list1[i]))

print(sum(final_list))

    

