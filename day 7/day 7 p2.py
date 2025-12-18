grid = [line.rstrip('\n') for line in open("input day 7.txt")]

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

cur = [0] * cols
exit_timelines = 0

if sr == rows - 1:
    exit_timelines = 1
else:
    cur[sc] = 1  

for r in range(sr + 1, rows):
    nxt = [0] * cols
    for c in range(cols):
        cnt = cur[c]
        if cnt == 0:
            continue

        ch = grid[r][c]

        if ch == '.' or ch == 'S':
          
            if r + 1 < rows:
                nxt[c] += cnt
            else:
                exit_timelines += cnt

        elif ch == '^':
            if c - 1 >= 0:
                if r + 1 < rows:
                    nxt[c - 1] += cnt
                else:
                    exit_timelines += cnt
            else:
                exit_timelines += cnt

            if c + 1 < cols:
                if r + 1 < rows:
                    nxt[c + 1] += cnt
                else:
                    exit_timelines += cnt
            else:
                exit_timelines += cnt

    cur = nxt

print(exit_timelines)
