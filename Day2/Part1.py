file_path = "input.txt"

reports = []

with open(file_path, "r") as file:
    for line in file:
        reports.append(line.split())

print(reports)

