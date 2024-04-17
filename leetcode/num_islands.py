"""
# No if island_count
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island_count is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.



"""

from typing import List

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def islands(grid: List[List[str]]) -> int:
    island_count = 0
    visited = set()

    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        if (
            r not in range(rows)
            or c not in range(cols)
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return

        visited.add((r, c))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left right up down

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                island_count += 1
                dfs(r, c)

    print(f"Total islands: {island_count}")
    return island_count


islands(grid=grid)
