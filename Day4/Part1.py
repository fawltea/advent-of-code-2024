def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0
    
    # Helper function to check in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # All 8 directions: (row step, col step)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

# Load the grid from a text file
file_path = "input.txt"  # Replace with the path to your file

# Read the file and process it into a grid
with open(file_path, "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Count the occurrences of "XMAS"
total_count = count_xmas(grid)
print(f"Total occurrences of 'XMAS': {total_count}")
