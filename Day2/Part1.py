file_path = "input.txt"

reports = []
with open(file_path, "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False
    
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    
    return is_increasing or is_decreasing

safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1

print(f"Number of safe reports: {safe_count}")
