grid = [line.rstrip('\n') for line in open("input day 7.txt") if line.strip()]

rows = len(grid)
cols = len(grid[0])

sr = sc = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            sr, sc = r, c
            break
    if sr is not None:
        break

beams = [False] * cols
split_count = 0

if sr + 1 < rows:
    beams[sc] = True

for r in range(sr + 1, rows):
    next_beams = [False] * cols
    for c in range(cols):
        if not beams[c]:
            continue

        cell = grid[r][c]

        if cell == '.' or cell == 'S':
            if r + 1 < rows:
                next_beams[c] = True

        elif cell == '^':
            split_count += 1
            if r + 1 < rows:
                if c - 1 >= 0:
                    next_beams[c - 1] = True
                if c + 1 < cols:
                    next_beams[c + 1] = True

    beams = next_beams

print(split_count)
