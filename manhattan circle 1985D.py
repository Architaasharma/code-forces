t = int(input())
result = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    min_row, max_row = float('inf'), float('-inf')
    min_column, max_column = float('inf'), float('-inf')
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '#':
                if r < min_row:
                    min_row = r
                if r > max_row:
                    max_row = r
                if c < min_column:
                    min_column = c
                if c > max_column:
                    max_column = c
    center_row = (min_row + max_row) // 2 + 1  
    center_column = (min_column + max_column) // 2 + 1
    result.append((center_row, center_column))

for results in result:
    print(results[0], results[1])
