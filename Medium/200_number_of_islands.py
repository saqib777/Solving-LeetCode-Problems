"""
LeetCode #200 — Number of Islands
Difficulty: Medium
Pattern: DFS Flood Fill on 2D Grid
Time: O(m*n) | Space: O(m*n) worst case recursion stack

Problem:
    Given a 2D grid of '1' (land) and '0' (water),
    count the number of islands (connected land regions).

Approach:
    For each unvisited '1', increment island count.
    DFS flood fill — mark all connected '1's as visited
    by sinking them to '0' so they aren't counted again.

Why sink instead of separate visited set:
    Modifying the grid avoids O(m*n) extra space for a visited array.
    The grid is restored conceptually by the problem — we are allowed to mutate.
"""


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows  = len(grid)
    cols  = len(grid[0])
    count = 0

    def dfs(r: int, c: int):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'   # sink the land
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# ── Tests ──────────────────────────────────────────────────────────────────────
def g(rows): return [list(r) for r in rows]

def test_one_island():
    assert num_islands(g(['11110','11010','11000','00000'])) == 1

def test_three_islands():
    assert num_islands(g(['11000','11000','00100','00011'])) == 3

def test_all_water():
    assert num_islands(g(['0000','0000'])) == 0

def test_single_land():
    assert num_islands([['1']]) == 1

def test_single_water():
    assert num_islands([['0']]) == 0

def test_diagonal_not_connected():
    assert num_islands(g(['10','01'])) == 2

def test_empty():
    assert num_islands([]) == 0

if __name__ == "__main__":
    print(num_islands(g(['11110','11010','11000','00000'])))  # 1
    print(num_islands(g(['11000','11000','00100','00011'])))  # 3
