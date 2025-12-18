points = []

with open("input day 9.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        points.append((x, y))

n = len(points)
best = 0

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height
        if area > best:
            best = area

print(best)
