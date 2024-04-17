def min_parking_space(grid) -> int:
    count = 0
    grid = sorted(grid)

    rows = len(grid)
    parkings = [grid[0][1]]

    for row in range(rows):
        if grid[row][0] < min(parkings):
            count += 1
        else:
            parkings.append(grid[row][1])

    print(count)
    return count


arr = [5, 10, 0, 15, 25, 40, 35, 45]
total = 4
grid = []

for i in range(total):
    grid.append([arr[i * 2], arr[i * 2 + 1]])

print(sorted(grid))
min_parking_space(grid)
