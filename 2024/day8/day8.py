# part 1
def read_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_positions(grid):
    positions = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                char = grid[y][x]
                if char not in positions:
                    positions[char] = []
                positions[char].append((x, y))
    return positions

def get_opposite_point(p1, p2):
    # The opposite point is the point that completes the parallelogram
    # If we have points A(x1,y1) and B(x2,y2), the opposite of A relative to B is (2*x2-x1, 2*y2-y1)
    x1, y1 = p1
    x2, y2 = p2
    return (2*x2-x1, 2*y2-y1)

def is_within_grid(point, grid):
    x, y = point
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def get_line_points(p1, p2, grid_size):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate maximum range based on grid dimensions
    max_height, max_width = grid_size
    max_range = max(max_height, max_width) + 1
    
    points = []
    # Extend the line in both directions using grid size
    for t in range(-max_range, max_range + 1):
        x = x1 + dx * t
        y = y1 + dy * t
        # Only add if it's an integer point
        if x.is_integer() and y.is_integer():
            points.append((int(x), int(y)))
    return points

def find_opposites(filename):
    grid = read_map(filename)
    grid_size = (len(grid), len(grid[0]))  # (height, width)
    positions = find_positions(grid)
    valid_opposites = []
    seen_opposites = set()
    total = 0

    # For each character and its positions
    for char, points in positions.items():
        # For each pair of points with the same character
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                
                # Get all points along the line using grid size
                line_points = get_line_points(p1, p2, grid_size)
                
                # Check each point on the line
                for point in line_points:
                    # Check if point is within grid and hasn't been seen
                    if is_within_grid(point, grid) and point not in seen_opposites:
                        valid_opposites.append((point, char, p1, p2))
                        seen_opposites.add(point)
                        total += 1

    # Print results
    print(f"\nValid line points found:")
    for point, char, p1, p2 in valid_opposites:
        print(f"Character '{char}': Points {p1} and {p2} create line point at {point}")
    print(f"\nTotal unique line points found: {total}")

    return valid_opposites, total

# Run the analysis
if __name__ == "__main__":
    find_opposites("input8.txt")