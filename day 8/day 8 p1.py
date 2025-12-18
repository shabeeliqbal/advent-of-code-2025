from math import prod

def read_points(filename="input day 8.txt"):
    pts = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            pts.append((x, y, z))
    return pts

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def main():
    points = read_points("input day 8.txt")
    n = len(points)
    edges = []

    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))

    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)
    steps = 0
    for _, a, b in edges:
        if steps == 1000:
            break
        dsu.union(a, b)
        steps += 1

    comp_sizes = {}
    for i in range(n):
        r = dsu.find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1

    largest = sorted(comp_sizes.values(), reverse=True)[:3]
    ans = prod(largest)
    print(ans)

if __name__ == "__main__":
    main()
