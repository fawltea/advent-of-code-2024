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

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False

safe_count_with_dampener = 0
for report in reports:
    if is_safe_with_dampener(report):
        safe_count_with_dampener += 1

print(f"Number of safe reports with Problem Dampener: {safe_count_with_dampener}")

