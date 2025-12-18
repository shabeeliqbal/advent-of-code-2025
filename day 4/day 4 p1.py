grid = [list(line.strip()) for line in open("input day 4.txt") if line.strip()]

rows = len(grid)
cols = len(grid[0])

dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1),(1,0),(1,1)]

accessible = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue
        cnt = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                cnt += 1
        if cnt < 4:
            accessible += 1

print(accessible)
